#import necessary libraries
from g4f.client import Client
import gradio as gr

#Initialize the G4F client
client = Client()

#Define the chatbot response function
def chatbot_response(user_input):
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user", "content": user_input}],
    )
    return response.choices[0].message.content

# Gradio user interface
interface = gr.Interface(
    fn = chatbot_response,
    inputs=gr.Textbox(lines=2, placeholder="Type your question here...."),
    outputs="text",
    title="Iqbal Cloud AI Assistant Chatbot",
    description="Ask any question and the AI assistant will respond."
)

#Launch the interface
if __name__ == "__main__":
    interface.launch()