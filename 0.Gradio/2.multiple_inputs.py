import gradio as gr


def processText(number,text):
    return f"You entered: {number} and Text:{text}"

demo=gr.Interface(
    fn=processText,
    inputs=[
        gr.Number(
        label="Enter Number"
        ),
        gr.Textbox(
        label="Enter Text"
        )
    ],
    outputs=gr.Textbox(
        label="Output"
    ),
)

demo.launch()