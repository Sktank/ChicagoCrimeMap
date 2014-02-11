__author__ = 'spencertank'

from flask import Flask
from flask import render_template
from twilio.rest import TwilioRestClient
import twilio.twiml
from flask import request


app = Flask(__name__)


@app.route("/")
def index(template = 'index.html'):
    return render_template(template)


if __name__ == "__main__":
    app.run(port=5001, debug=True)
