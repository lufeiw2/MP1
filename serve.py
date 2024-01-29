from flask import Flask
from subprocess import Popen, PIPE
import socket

app = Flask(__name__)

@app.route("/", methods=["POST"])
def stress_cpu():
    # Run stress_cpu.py in a separate process
    process = Popen(["python3", "stress_cpu.py"], stdout=PIPE, stderr=PIPE)
    std_out, std_err = process.communicate()
    return "CPU stress initiated", 200

@app.route("/", methods=["GET"])
def get_private_ip():
    # Get private IP address of the EC2 instance
    private_ip = socket.gethostbyname(socket.gethostname())
    return private_ip, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
