from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello Dear MT! I see you preparing for your new job at Pento, GO FOR IT!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
