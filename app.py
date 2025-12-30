import os
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, join_room

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default_secret')
# Allow all origins to prevent CORS errors
socketio = SocketIO(app, cors_allowed_origins="*")

PRIVATE_ROOM = "us_two_only"

# --- YOUR CUSTOM PIN ---
SECRET_PIN = "7652004" 
# -----------------------

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('join')
def on_join(data):
    # 1. Check the PIN sent from the phone
    user_pin = data.get('pin')
    
    if user_pin == SECRET_PIN:
        # 2. If PIN is correct, let them in
        join_room(PRIVATE_ROOM)
        print(f"User joined with correct PIN: {request.sid}")
        emit('ready', room=PRIVATE_ROOM, include_self=False)
    else:
        # 3. If wrong, kick them out with the ROAST
        print(f"User tried to join with WRONG PIN: {user_pin}")
        # The Custom Message:
        emit('auth_error', {'message': 'neku loverrr unda? mari enduku ra neeku 😂'}, to=request.sid)

@socketio.on('signal')
def on_signal(data):
    emit('signal', data, room=PRIVATE_ROOM, include_self=False)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
