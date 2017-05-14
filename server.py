
import os, re;
from flask import Flask, jsonify, render_template, redirect, request, Response, flash, session
from faker import Factory
from twilio.jwt.client import ClientCapabilityToken
from twilio.twiml.voice_response import VoiceResponse


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("FLASK_SECRET_KEY", "s0Then!stO0dth34ean9a11iw4n7edto9ow4s8ur$7!ntOfL*me5")
fake = Factory.create()
alphanumeric_only = re.compile('[\W_]+')
phone_pattern = re.compile(r"^[\d\+\-\(\) ]+$")


@app.route('/')
def index():
    """Shows the homepage"""

    return render_template('index.html')


@app.route("/voice", methods=['GET', 'POST'])
def voice():
    """Respond to incoming phone calls with a 'Hello world' message"""
    # Start our TwiML response
    resp = VoiceResponse()

    # Read a message aloud to the caller
    resp.say("hello world!", voice='alice')

    return str(resp)
################################################################################
if __name__ == "__main__":

    DEBUG = "NO_DEBUG" not in os.environ
    PORT = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=PORT)
