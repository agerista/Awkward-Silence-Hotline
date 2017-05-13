"""Awkward Silence Generator."""

import os
from jinja2 import StrictUndefined
from flask import Flask, jsonify, render_template, redirect, request, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db
from twilio.twiml.voice_response import VoiceResponse


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.config['SECRET_KEY'] = os.environ.get("FLASK_SECRET_KEY", "s0Then!stO0dth34ean9a11iw4n7edto9ow4s8ur$7!ntOfL*me5")

# Normally, if you use an undefined variable in Jinja2, it fails
# silently. This is horrible. Fix this so that, instead, it raises an
# error.
app.jinja_env.undefined = StrictUndefined


callers = {
    "+14155555555": "Amanda",
    "+14155555554": "Nathan",
    "+14155555553": "Renee",
}


@app.route("/monkey", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming requests."""

    print "Trying to learn all about the twilio API"

    from_number = request.values.get('From', None)

    # if the caller is someone we know:
    if from_number in callers:

        caller = callers[from_number]
    else:
        caller = "Monkey"

    resp = VoiceResponse()
    # Greet the caller by name
    resp.say("Hello " + callers[from_number] + ", you monkey")
    # Play an MP3
    resp.play("http://awkward-silence-generator.herokuapp.com/monkey.mp3")


    return str(resp)


################################################################################
if __name__ == "__main__":

    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = False
    # make sure templates, etc. are not cached in debug mode
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app, os.environ.get("DATABASE_URL"))

    # Use the DebugToolbar
    # DebugToolbarExtension(app)
    # app.run(port=5000, host='0.0.0.0')

    DEBUG = "NO_DEBUG" not in os.environ
    PORT = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
