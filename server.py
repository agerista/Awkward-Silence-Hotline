
import os, re;
from flask import Flask, jsonify, render_template, redirect, request, Response, flash, session
# from faker import Factory
# from twilio.jwt.access_token import AccessToken
# from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse




app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("FLASK_SECRET_KEY", "s0Then!stO0dth34ean9a11iw4n7edto9ow4s8ur$7!ntOfL*me5")

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming requests."""
    resp = VoiceResponse()
    resp.say("Uhhhhhh")

    return str(resp)


################################################################################
if __name__ == "__main__":

    DEBUG = "NO_DEBUG" not in os.environ
    PORT = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=PORT)
