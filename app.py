from flask import Flask
from random import randint

app = Flask(__name__)

@app.route("/")
def index():
    return f"<img src=\"https://avatars.githubusercontent.com/u/{randint(1,99999999)}\">"

if __name__ == '__main__':
    app.run()