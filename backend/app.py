from flask import Flask

app = Flask(__name__)

@app.route("/profile")
def index():

    user = {
        "fname": "mikasa",
        "lname": "ackerman",
        "email": "ackerman@gmail.com"
    }

    return user