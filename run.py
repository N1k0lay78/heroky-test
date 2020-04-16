from flask import Flask

app = Flask(__name__)


@app.rout('/')
def index():
    return "HELLO"


if __name__ == '__main__':
    app.run()