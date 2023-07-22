from fastapi import FastAPI
import gradio as gr

from gradio_ui import demo

app = FastAPI()

@app.get('/')
async def root():
    return 'Gradio app is running at /gradio', 200

app = gr.mount_gradio_app(app, demo, path='/gradio')
