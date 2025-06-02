from ollama import Client

client = Client(host='http://localhost:11434')
print(client.list())
