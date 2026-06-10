import ollama

input_text = input("Enter text: ")

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "system",
            "content": """
            Riassumi il testo in massimo 255 caratteri.
            """
        },
        {
            "role": "user",
            "content": input_text
        }
    ]
)

# test: Modena investirà nel trasporto pubblico con autobus elettrici e nuove piste ciclabili. I lavori inizieranno il prossimo anno e dureranno circa due anni.
print(response["message"]["content"])