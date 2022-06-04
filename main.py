from flask import Flask
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chatappofefe'

socketio = SocketIO(app, cors_allowed_origins="*") #Cors hatası aldığım için ikinci parametreyi vermem gerekti

@socketio.on('message')

def handlemessage(msg):
    send(msg, broadcast = True)

if __name__ == '__main__':
    socketio.run(app)