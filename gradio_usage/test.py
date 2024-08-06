import gradio as gr


# def greet(name, intensity):
#     return "Hello, " + name + "!" * int(intensity)


def greet(name, is_morning, temperature):
    salutation = "Good morning" if is_morning else "Good evening"
    greeting = f"{salutation} {name}. It is {temperature} degrees today"
    celsius = (temperature - 32) * 5 / 9
    return greeting, round(celsius, 2)


demo = gr.Interface(
    fn=greet,
    # inputs=["text", "slider"],
    # inputs=["text", gr.Slider(value=2, minimum=1, maximum=10, step=1)],
    # outputs=["text"],
    inputs=["text", "checkbox", gr.Slider(0, 100)],
    outputs=["text", "number"],
)

demo.launch(server_name="0.0.0.0")
