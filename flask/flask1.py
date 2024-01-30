#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

@app.route("/")
#function of page
def home():
    return "This is the main page! <h1>Hello<h1>"

if __name__ == "__main__":
    app.run()