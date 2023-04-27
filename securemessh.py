import paramiko
import typer
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    server = request.form['server']
    username = request.form['username']
    password = request.form['password']
    message = request.form['message']

    # Set up the ssh client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

    # Connect to server
    ssh.connect(server, username=username, password=password)

    # Send message
    stdin, stdout, stderr = ssh.exec_command(f'echo "{message}" | nc localhost 443')

    # Get response
    response = stdout.read().decode()

    # Close connection
    ssh.close()

    return jsonify({'response':response})

if __name__ == '__main__':
    app.run(debug=True)