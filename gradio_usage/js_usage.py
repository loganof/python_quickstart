import gradio as gr

bot_avatar = "<img src='https://cdn-icons-png.flaticon.com/512/630/630426.png' alt='Bot' style='vertical-align:middle; margin-right: 8px;border-radius: 50%; width: 30px; height: 30px;'>"


def welcome(name):
    return f"Welcome to Gradio, {name}!"


js = """
function createGradioAnimation() {
    var container = document.createElement('div');
    container.id = 'gradio-animation';
    container.style.fontSize = '2em';
    container.style.fontWeight = 'bold';
    container.style.textAlign = 'center';
    container.style.marginBottom = '20px';

    var text = "欢迎使用聊天机器人";
    for (var i = 0; i < text.length; i++) {
        (function(i){
            setTimeout(function(){
                var letter = document.createElement('span');
                letter.style.opacity = '0';
                letter.style.transition = 'opacity 0.5s';
                letter.innerText = text[i];

                container.appendChild(letter);

                setTimeout(function() {
                    letter.style.opacity = '1';
                }, 50);
            }, i * 250);
        })(i);
    }

    var gradioContainer = document.querySelector('.gradio-container');
    gradioContainer.insertBefore(container, gradioContainer.firstChild);

    return 'Animation created';
}
"""
with gr.Blocks(js=js) as demo:
    with gr.Row():
        gr.Markdown(f"<h3><center>{bot_avatar}聊天机器人</center></h3>")
    inp = gr.Textbox(placeholder="What is your name?")
    out = gr.Textbox()
    inp.change(welcome, inp, out)

demo.launch(server_name="0.0.0.0")
