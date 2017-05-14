
import os, re;
from flask import Flask, jsonify, render_template, redirect, request, Response, flash, session
from faker import Factory
from twilio.jwt.client import ClientCapabilityToken
from twilio.twiml.voice_response import VoiceResponse


app = Flask(__name__)
fake = Factory.create()
alphanumeric_only = re.compile('[\W_]+')
phone_pattern = re.compile(r"^[\d\+\-\(\) ]+$")


@app.route('/')
def index():
    """Shows the homepage"""

    return render_template('index.html')

################################################################################
if __name__ == "__main__":

    DEBUG = "NO_DEBUG" not in os.environ
    PORT = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=PORT)
