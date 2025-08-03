import gradio as gr
from dialog_agent import get_ai_response

order_state = {}

def respond(user_input, history):
    response, updated_state = get_ai_response(user_input, order_state)
    return response

gr.ChatInterface(respond).launch(share=True)
