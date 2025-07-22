import gradio as gr


def countFiles(files):
    return f"You entered {len(files)} files"

demo=gr.Interface(
    fn=countFiles,
    inputs=gr.File(
        file_count="multiple",
        type="filepath",
        label="Upload or drag files here"
    ),
    outputs=gr.Textbox(
        label="Output"
    )
)

demo.launch()