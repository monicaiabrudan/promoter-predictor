import gradio as gr

def predict(sequence):
    return "Promoter"

demo = gr.Interface(
    fn=predict,
    inputs="text",
    outputs="text",
    title="DNA Promoter Predictor"
)

demo.launch()