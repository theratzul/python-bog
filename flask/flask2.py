#!/usr/bin/python3
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
#function of page
def home():
    return "This is the main page! <h1>Hello<h1>"

@app.route("/<name>")
def user(name):
    return f"Hello {name}"

@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Admin!"))

if __name__ == "__main__":
    app.run()