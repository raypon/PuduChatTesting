from flask import Flask, render_template
from flask_socketio import SocketIO,emit

app= Flask(__name__)

#Cree la llave
app.config['SECRET_KEY'] = "secret!"
socketio= SocketIO(app)


@app.route("/")
def hellow_world():
    return render_template("test.html")

#Enviar mensaje a cliente
@socketio.on('event')
def event(json):
    print("ESTO ES VENTO"+json)
    emit('event', json)


if __name__ == '__main__':
    app.run(debug=True)
  