import google.generativeai as genai
import gradio as gr

# Configure API key (Use your own generated api key)
genai.configure(api_key="AIzaSyDYB8KOlgtmZidCh3Nb0d6hDT2IZ-1L1O8")

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-pro")

# Define chatbot function
def chatbot(user_input, history=[]):
    response = model.generate_content(user_input)
    return response.text

# Create Gradio interface
iface = gr.Interface(
    fn=chatbot,
    inputs="text",
    outputs="text",
    title="Gemini Chatbot",
    description="Chat with Google Gemini AI"
)

# Launch the web app
iface.launch(share=True)