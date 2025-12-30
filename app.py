from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, join_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

# This is the "Private Room" only you two can join
PRIVATE_ROOM = "us_two_only"

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('join')
def on_join(data):
    join_room(PRIVATE_ROOM)
    print(f"User connected: {request.sid}")
    # Tell others in the room "I am here"
    emit('ready', room=PRIVATE_ROOM, include_self=False)

@socketio.on('signal')
def on_signal(data):
    # Pass audio data directly to the other person
    emit('signal', data, room=PRIVATE_ROOM, include_self=False)

if __name__ == '__main__':
    # We use eventlet for better performance with WebSockets
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)