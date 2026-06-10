import ollama

data = {
    "name": "Giovanni",
    "age": 30,
    "city": "Roma",
    "profession": "Ingegnere"
}

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "system",
            "content": """
            Trasforma il dizionario in una descrizione naturale e completa.
            """
        },
        {
            "role": "user",
            "content": str(data)
        }
    ]
)

print(response["message"]["content"])