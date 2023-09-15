# FrontEnd -> é o que você vê "html, css, javascript"
# Backend -> a lógica de funcionamento por trás do site "python"
# Framework -> Flask -> criar sites

# Ambiente virtual -> local no seu computador com instalações específicas
# Usar o "Command Prompt" para fazer as instalações
# Para criar o ambiente virtual digitar: "Python Create Enviroment" no Command Palette

# Importar o flask
from flask import Flask, render_template
from flask_socketio import SocketIO, send

# Criar um aplicativo com o flask
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Funcionalidade de enviar mensagens
@socketio.on("message")
def gerenciar_mensagem(mensagem):
    send(mensagem, broadcast=True)

# Vamos criar nossa primeira página = primeira rota
# Tudo que vêm depois da URL incluindo a "/" é rota, ex: /blog, /python, /power-bi
@app.route("/")

# Criar uma função para ser executada nessa rota
def homepage():
    return render_template("homepage.html")

# E vamos rodar o nosso aplicativo
socketio.run(app, host="localhost")

# Bloco de código para configurar seu servidor web para ignorar solicitações para favicon.ico;
# Se estiver usando o Flask em Python, você pode fazer algo assim: 
""" if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, threaded=True, use_reloader=False) """

# Instalando o WebSocket
# pip install python-socketio flask-socketio simple-websocket