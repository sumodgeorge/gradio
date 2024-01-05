import gradio as gr

def image_generator(textbox, slider, checkbox):
    return "http://www.marketingtool.online/en/face-generator/img/faces/avatar-1151ce9f4b2043de0d2e3b7826127998.jpg", slider, checkbox

demo = gr.Interface(
    fn=image_generator, 
    inputs=[
        gr.Textbox(),
        gr.Accordion("Advanced Options", 
        components=[
            gr.Slider(minimum=1, maximum=10), 
            gr.Checkbox(label="Noise reduction")
        ])
    ],
    outputs=[
        gr.Image(),
        gr.Accordion("Options Used", open=False,
        components=[
            gr.Slider(minimum=1, maximum=10), 
            gr.Checkbox(label="Noise reduction")
        ])
    ]
)

if __name__ == "__main__":
    demo.launch()