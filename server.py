
import os, re;
from flask import Flask, jsonify, render_template, redirect, request, Response, flash, session
from faker import Factory
from twilio.jwt.access_token import AccessToken, VoiceGrant
from twilio.rest import Client
import twilio.twiml


IDENTITY = 'voice_test'
CALLER_ID = 'quick_start'

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("FLASK_SECRET_KEY", "s0Then!stO0dth34ean9a11iw4n7edto9ow4s8ur$7!ntOfL*me5")
fake = Factory.create()
alphanumeric_only = re.compile('[\W_]+')
phone_pattern = re.compile(r"^[\d\+\-\(\) ]+$")

TWILIO_ACCOUNT_SID = os.environ[TWILIO_ACCOUNT_SID]
TWILIO_TWIML_APP_SID = os.environ[TWILIO_TWIML_APP_SID]
TWILIO_AUTH_TOKEN = os.environ[TWILIO_AUTH_TOKEN]
TWILIO_CALLER_ID = os.environ[TWILIO_CALLER_ID]


@app.route('/')
def index():
    """Shows the homepage"""

    return render_template('index.html')


@app.route('/accessToken')
def token():

    account_sid = os.environ.get("ACCOUNT_SID", ACCOUNT_SID)
    api_key = os.environ.get("API_KEY", API_KEY)
    api_key_secret = os.environ.get("API_KEY_SECRET", API_KEY_SECRET)
    push_credential_sid = os.environ.get("PUSH_CREDENTIAL_SID", PUSH_CREDENTIAL_SID)
    app_sid = os.environ.get("APP_SID", APP_SID)

    grant = VoiceGrant(
        push_credential_sid=push_credential_sid,
        outgoing_application_sid=app_sid
      )

      token = AccessToken(account_sid, api_key, api_key_secret, IDENTITY)
      token.add_grant(grant)

      return str(token)


@app.route('/outgoing', methods=['GET', 'POST'])
def outgoing():

      resp = twilio.twiml.Response()
      resp.say("Congratulations! You have made your first oubound call! Good bye.")
      return str(resp)


@app.route('/incoming', methods=['GET', 'POST'])
def incoming():
  
    resp = twilio.twiml.Response()
    resp.say("Congratulations! You have received your first inbound call! Good bye.")
    return str(resp)


@app.route('/placeCall', methods=['GET', 'POST'])
def placeCall():

    account_sid = os.environ.get("ACCOUNT_SID", ACCOUNT_SID)
    api_key = os.environ.get("API_KEY", API_KEY)
    api_key_secret = os.environ.get("API_KEY_SECRET", API_KEY_SECRET)

    client = Client(api_key, api_key_secret, account_sid)
    call = client.calls.create(url=request.url_root + 'incoming', to='client:' + IDENTITY, from_='client:' + CALLER_ID)
    return str(call.sid)


@app.route('/', methods=['GET', 'POST'])
def welcome():

    resp = twilio.twiml.Response()
    resp.say("Welcome to Twilio")
    return str(resp)

################################################################################
if __name__ == "__main__":

    DEBUG = "NO_DEBUG" not in os.environ
    PORT = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=PORT)
