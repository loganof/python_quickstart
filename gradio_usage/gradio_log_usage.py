import gradio as gr
from gradio_log import Log

log_file_path = "/data/pengzc/project/agents/autoagents/output.log"

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column(scale=2):
            chatbot = gr.Chatbot(label="Chatbot 1")
        with gr.Column(scale=1):
            Log(log_file_path, dark=True, xterm_font_size=12)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0")
