from flask import Flask
from flask import request
from flask import render_template

server = Flask(__name__)

@server.route("/")
def main():
    return render_template("login.html")

@server.route("/registration.html")
def registration():
    return render_template("registration.html")

if __name__ == "__main__":
    server.run(host="localhost", port=5000)
