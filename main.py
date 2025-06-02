from ollama import Client
from datetime import datetime
import re
import json

client = Client(host='http://localhost:11434')
model = "calendarassistant"

# Obtem a data de hoje para contexto
date_today = datetime.now().strftime("%Y-%m-%d")
history = f"Today is {date_today}.\n"

# Primeira interação
user_input = input("Mark your date to add it to the calendar: ")
history += f"User: {user_input}\n"


def json_is_complete(text):
    try:
        json_str = re.search(r"\{.*\}", text, re.DOTALL).group()
        data = json.loads(json_str)
        required_fields = ["date", "hour", "title"]
        return all(field in data and data[field] and "missing" not in str(data[field]).lower() for field in required_fields)
    except:
        return False

while True:
        response = client.generate(model=model, prompt=history)
        response_text = response['response'].strip()
        print("Assistant:", response_text)

        history += f"Assistant: {response_text}\n"

        # Se estiver completo, termina o ciclo
        if json_is_complete(response_text):
            break

        # Caso contrário, pede input
        follow_up = input("User: ")
        history += f"User: {follow_up}\n"



