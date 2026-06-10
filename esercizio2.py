import ollama

input_text = input("Enter text: ")

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "system",
            "content": """
            Estrai:
            - Nome
            - Età
            - Professione

            Rispondi nel formato:

            Nome:
            Età:
            Professione:
            """
        },
        {
            "role": "user",
            "content": input_text
        }
    ]
)
# test:Giulia Rossi ha 32 anni ed è un'architetta che vive a Milano.
print(response["message"]["content"])