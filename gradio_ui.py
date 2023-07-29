import gradio as gr


def greet(text: str) -> str:
    return text


demo = gr.Interface(
    fn=greet,
    inputs=gr.components.Textbox(label='Input'),
    outputs=gr.components.Textbox(label='Output'),
    allow_flagging='never'
)
