from flask import Flask, render_template, jsonify
import main
import socket
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname) 
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/armstrong/<int:number>")
def apinum(number):
    result = {
        "number": number,
        "Armstrong": main.func(number),
        "server IP": IPAddr
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)