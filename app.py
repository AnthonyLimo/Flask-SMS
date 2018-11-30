from flask import Flask, request, render_template

import africastalking


app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')