import gradio as gr


def processText(text):
    return f"You entered: {text}"

demo=gr.Interface(
    fn=processText,
    inputs=gr.Textbox(
        label="Enter Text"
    ),
    outputs=gr.Textbox(
        label="Output"
    ),
)

demo.launch()