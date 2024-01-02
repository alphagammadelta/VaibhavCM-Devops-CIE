from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Srujan Vinod Sarode 1BM21IS411</h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
