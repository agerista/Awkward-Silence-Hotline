
from random import choice

import os, re;
from jinja2 import StrictUndefined
from flask import Flask, jsonify, render_template, redirect, request, Response, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db
from faker import Factory
from twilio.jwt.client import ClientCapabilityToken
from twilio.twiml.voice_response import VoiceResponse

COMPLIMENTS = ["smart", "clever", "tenacious", "awesome", "Pythonic"]


@app.route('/')
def offer_greeting():
    """Greet user."""

<<<<<<< HEAD

app = Flask(__name__)
fake = Factory.create()
alphanumeric_only = re.compile('[\W_]+')
phone_pattern = re.compile(r"^[\d\+\-\(\) ]+$")


    player = request.args.get("person")  # ... what the user typed!
=======
    player = "you"  # ... what the user typed!
>>>>>>> 969b2c7e7a4c91240719c47d0cd287f98a7056b5
    nice_thing = choice(COMPLIMENTS)


    return "<html><body>Hi, %s. I think you're %s!</body></html>" % (
        player, nice_thing)

# Normally, if you use an undefined variable in Jinja2, it fails
# silently. This is horrible. Fix this so that, instead, it raises an
# error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    print "Hello World"
    print "trial run"
    print "testing heroku"
    return app.send_static_file('index.html')


@app.route('/token', methods=['GET'])
def token():
    # get credentials for environment variables
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    application_sid = os.environ['TWILIO_TWIML_APP_SID']

    # Generate a random user name
    identity = alphanumeric_only.sub('', fake.user_name())

    # Create a Capability Token
    capability = ClientCapabilityToken(account_sid, auth_token)
    capability.allow_client_outgoing(application_sid)
    capability.allow_client_incoming(identity)
    token = capability.to_jwt()

    # Return token info as JSON
    return jsonify(identity=identity, token=token)


@app.route("/voice", methods=['POST'])
def voice():
    resp = VoiceResponse()
    if "To" in request.form and request.form["To"] != '':
        dial = resp.dial(callerId=os.environ['TWILIO_CALLER_ID'])
        # wrap the phone number or client name in the appropriate TwiML verb
        # by checking if the number given has only digits and format symbols
        if phone_pattern.match(request.form["To"]):
            dial.number(request.form["To"])
        else:
            dial.client(request.form["To"])
    else:
        resp.say("Thanks for calling!")

    return Response(str(resp), mimetype='text/xml')


################################################################################
if __name__ == "__main__":
<<<<<<< HEAD

    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    # app.debug = False
    # make sure templates, etc. are not cached in debug mode
    # app.jinja_env.auto_reload = app.debug

    # Use the DebugToolbar
    # DebugToolbarExtension(app)
    # app.run(port=5000, host='0.0.0.0')

    connect_to_db(app, os.environ.get("DATABASE_URL"))

    DEBUG = "NO_DEBUG" not in os.environ
    PORT = int(os.environ.get("PORT", 5000))

=======
    DEBUG = "NO_DEBUG" not in os.environ
>>>>>>> 969b2c7e7a4c91240719c47d0cd287f98a7056b5
    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
