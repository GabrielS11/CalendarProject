from msal import PublicClientApplication
from dotenv import load_dotenv
import requests
import os

load_dotenv()


def AddEventToCalendar(event_data):
    CLIENT_ID = os.getenv('CLIENT_ID')
    TENANT_ID = os.getenv('TENANT_ID')
    AUTHORITY = os.getenv('AUTHORITY')
    SCOPES = os.getenv('SCOPES')


    app = PublicClientApplication(client_id=CLIENT_ID, authority=AUTHORITY)

    accounts = app.get_accounts()
    if accounts:
        result = app.acquire_token_silent(SCOPES, account=accounts[0])
    else:
        result = app.acquire_token_interactive(scopes=SCOPES)


    if "access_token" in result:
        token = result["access_token"]

        event = {
        "subject": event_data["title"],
        "body": {
            "contentType": "HTML",
            "content": event_data["description"]
        },
        "start": {
            "dateTime": f"{event_data['date']}T{event_data['hour']}:00",
            "timeZone": "Europe/Lisbon"
        },
        "end": {
            "dateTime": f"{event_data['date']}T{event_data['hour'][:-2]}{str(int(event_data['hour'][-2:]) + 30).zfill(2)}:00",
            "timeZone": "Europe/Lisbon"
        },
        "location": {
            "displayName": "Local padrão"
        }
    }

        # Enviar para o calendário
        response = requests.post(
            url="https://graph.microsoft.com/v1.0/me/events",
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
            },
            json=event
        )

        if response.status_code == 201:
            print("Evento criado com sucesso!")
        else:
            print("Erro ao criar evento:", response.status_code)
            print(response.json())

    else:
        print("Erro ao obter token:", result.get("error_description"))