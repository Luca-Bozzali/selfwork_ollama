import ollama

input_text = input("Enter text: ")

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "system",
            "content": """
            Traduci dall'italiano all'inglese e dall'inglese all'italiano.
            Restituisci solamente la traduzione.
            """
        },
        {
            "role": "user",
            "content": input_text
        }
    ]
)

# test: Questo smartphone ha una batteria da 5000 mAh e una fotocamera da 50 MP.
print(response["message"]["content"])