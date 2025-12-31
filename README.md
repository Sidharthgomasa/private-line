# 🔒 Private Line - Secure P2P Calling App

A private, secure, and encrypted voice calling web application designed for two people. Built with **Flask**, **Socket.IO**, and **WebRTC**, this app establishes a direct Peer-to-Peer (P2P) audio connection that works across different states, countries, and strict mobile networks (Jio, Airtel, etc.).

## 🚀 Features

* **100% Private:** Direct P2P audio connection; no audio is recorded on any server.
* **Secure Access:** Protected by a custom 7-digit PIN ("Gatekeeper").
* **Works Everywhere:** Integrated **TURN Server** (Metered.ca) to bypass strict mobile firewalls (Symmetric NAT) on 4G/5G networks.
* **Smart Notifications:** Automatically sends a **Telegram Alert** when a call starts.
* **Speaker Mode:** Dedicated button to toggle between Earpiece and Loudspeaker (Android optimization).
* **Custom Roast:** Fun error messages for intruders who guess the wrong PIN.

## 🛠️ Tech Stack

* **Backend:** Python (Flask, Flask-SocketIO)
* **Frontend:** HTML5, CSS3, JavaScript (Socket.IO Client)
* **Real-time Logic:** WebSockets (Socket.IO)
* **Audio Streaming:** WebRTC (STUN/TURN)
* **Deployment:** Render (Gunicorn + Eventlet)

## 📂 Project Structure

```text
/private-line
│── app.py                # Main Flask application & SocketIO logic
│── requirements.txt      # Python dependencies
│── templates/
│   └── index.html        # Frontend UI & WebRTC logic
└── README.md             # Project documentation
