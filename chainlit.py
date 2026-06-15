import chainlit as cl
import ollama


@cl.on_message
async def main(message: cl.Message):

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": """
                Sei un assistente AI utile, educato e professionale.
                Rispondi sempre in italiano.
                """
            },
            {
                "role": "user",
                "content": message.content
            }
        ]
    )

    await cl.Message(
        content=response["message"]["content"]
    ).send()