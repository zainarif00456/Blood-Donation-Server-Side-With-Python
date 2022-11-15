from flask import Flask
from flask_cors import CORS

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "Flask API for Blood Donation Application"


if __name__ == '__main__':
    app.run("0.0.0.0", debug=True)
