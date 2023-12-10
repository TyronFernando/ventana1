from flask import Flask, render_template_string
app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
    <html>
    <head>
        <title>aqui va el nombre de la ventana pero aun no se que poner</title>
        <style>
            #boton {
                position: absolute;
                top: 50%;
                left: 40%;
                transform: translate(-50%, -50%);
            }
            #boton2 {
                position: absolute;
                top: 50%;
                left: 60%;
                transform: translate(-50%, -50%);
            }
        </style>
        <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        <script>
            $(document).ready(function() {
                $("#boton").mouseenter(function() {
                    var x = Math.floor(Math.random() * ($(window).width() - $(this).width()));
                    var y = Math.floor(Math.random() * ($(window).height() - $(this).height()));
                    $(this).css({left: x + 'px', top: y + 'px'});
                });
            });
        </script>
    </head>
    <body>
        <h1 style="font-family: Helvetica; font-size: 16px; text-align: center;">¿ERES NOVIA DE WILMER?</h1>
        <button id="boton">NO</button>
        <button id="boton2">SI</button>
    </body>
    </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
