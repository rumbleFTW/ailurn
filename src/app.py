import os
import time

import tqdm
import gradio as gr
from dotenv import load_dotenv
import google.generativeai as genai

from llm import parse_llm
from utils import *


def generate_audio(
    file_url, file_path, language, progress=gr.Progress(track_tqdm=True)
):
    try:
        if file_url and file_path:
            raise gr.Error("Only provide URL to pdf OR upload the PDF file!")
        document = load_document(file_url if file_url else file_path)
        script = ""
        for page in tqdm.tqdm(document, desc="Parsing pages"):
            script += parse_llm(page=page, image=False).text
        if language != "English":
            script = translate(script, target=language[language])
        audio_path = tts(script=script)
        return audio_path
    except Exception as e:
        raise gr.Error(e)


if __name__ == "__main__":
    load_dotenv()
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    iface = gr.Interface(
        fn=generate_audio,
        inputs=[
            gr.Textbox(type="text", label="Enter URL (or)"),
            gr.File(type="filepath", label="PDF"),
            gr.Dropdown(
                languages.keys(),
                value="English",
                multiselect=False,
                label="Language",
            ),
        ],
        outputs="audio",
    )
    iface.launch()
