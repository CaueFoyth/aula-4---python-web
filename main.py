# site com os scripts: https://cdnjs.com/

from flask import Flask, render_template
from flask_socketio import SocketIO, send
# Criando o app
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_orings="*")

@socketio.on("message")
def gerenciar_mensagem(mensagem):
    send(mensagem, braodcast=True)
# Criar primeira pagina = primeira rota
@app.route("/")
def homepage():
    return render_template("index.html")


socketio.run(app, host="localhost")
# Rodar nosso app
app.run()