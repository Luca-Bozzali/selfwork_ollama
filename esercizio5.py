import ollama

input_text = input("Enter text: ")

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "system",
            "content": """
            Genera 5 domande di comprensione sul testo fornito.
            """
        },
        {
            "role": "user",
            "content": input_text
        }
    ]
)

# test: Il Colosseo è uno dei monumenti più famosi di Roma. Fu costruito durante l'Impero Romano e poteva ospitare fino a 50.000 spettatori. Al suo interno si svolgevano combattimenti tra gladiatori e altri spettacoli pubblici.
print(response["message"]["content"])