#!/usr/bin/python3
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/<name>")
#function of page
def home(name):
    return render_template("index.html")

if __name__ == "__main__":
    app.run()