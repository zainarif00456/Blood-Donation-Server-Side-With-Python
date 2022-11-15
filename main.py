from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def index():
    """
    for Testing the working of API
    :return:
    """
    return "Flask API for Blood Donation Application"


@app.route("/register", methods=["POST"])
def registration():
    payload = request.get_json()
    print(payload)
    return {"details": "Registration Successful"}


if __name__ == '__main__':
    app.run("0.0.0.0", debug=True)  # Running on all IP addresses.
