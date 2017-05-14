"""Awkward Silence Hotline"""

import os, re
from flask import Flask, jsonify, render_template, redirect, request, Response, flash, session
# from faker import Factory
# from twilio.jwt.access_token import AccessToken
from datetime import date
from twilio import twiml
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse, Gather
from twilio.twiml.messaging_response import MessagingResponse
import sms_functions
from jinja2 import StrictUndefined


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("FLASK_SECRET_KEY", "s0Then!stO0dth34ean9a11iw4n7edto9ow4s8ur$7!ntOfL*me5")
app.jinja_env.endefined = StrictUndefined


callers = {
    "+14158675309": "Curious George",
    "+14158675310": "Boots",
    "+14158675311": "Virgil",
}


@app.route("/", methods=['GET', 'POST'])
def awkward_silence_hotline():
    """awkward silence hotline phoneline"""
    # resp = VoiceResponse()
    # resp.say("Uhhhhhh")

    # return str(resp)
    from_number = request.values.get('From', None)
    if from_number in callers:
        caller = callers[from_number]
    else:
        caller = "Stupid Hacker"

    resp = VoiceResponse()
    # Greet the caller by name
    resp.say("Hello " + caller)

    # # Play an mp3
    # resp.play("http://demo.twilio.com/hellomonkey/monkey.mp3")

    # Gather digits.
    g = Gather(timeout="15", numDigits=1, action="/handle-key", method="POST")
    g.say("""I am the Lord Mayor of Awkward Town, press 1.
             Press 2 for I have foot in mouth disease.
             Press 3 for my boyfriend just broke up with me and I'm pregnant.
             Press 4 for I just can't.
             Press 5 to make your own recording
             Press any other key to start over.""")

    resp.append(g)

    return (str(resp), "index.html")


@app.route("/handle-key", methods=['GET', 'POST'])
def awkward_menu():
    """Handle key press from a user."""

    digit_pressed = request.values.get('Digits', None)
    if digit_pressed == "1":

        resp = VoiceResponse()
        # Dial (310) 555-1212 - connect that number to the incoming caller.
        resp.say("Yes well I declare, uhhhhhh, ummmmmm, well")
        resp.pause(10)
        resp.say("I mean I...uhhh...")
        resp.pause(10)
        resp.say("I...uhhh...ummmmmm")

        return str(resp)

    elif digit_pressed == "2":

        resp = VoiceResponse()
        resp.say("My shower cam is no bigger than that fly in your soup.")
        resp.pause(15)
        resp.say("well...")
        resp.pause(15)
        resp.say("yeah...")
        resp.pause(15)
        resp.say("ha ahhh ha...")

        return str(resp)

    elif digit_pressed == "3":

        resp = VoiceResponse()
        resp.say("I believe I'm about to throw up.")
        resp.pause(5)
        resp.say("don't you love me?...")
        resp.pause(15)
        resp.say("you...")
        resp.pause(15)
        resp.say("you said...")
        resp.pause(15)
        resp.say("that that that...")
        resp.pause(30)

        return str(resp)

    elif digit_pressed == "4":

        resp = VoiceResponse()
        resp.say("The secret ingredient is puppy tears.")
        resp.pause(20)
        resp.say("I mean salt")

        return str(resp)

    elif digit_pressed == "5":

        resp = VoiceResponse()
        resp.say("Record your awkward silence after the tone.")
        resp.record(maxLength="30", action="/handle-recording")

        return str(resp)

    # If the caller pressed anything but 1-5, redirect them to the homepage.
    else:
        return redirect("/")


@app.route("/handle-recording", methods=['GET', 'POST'])
def handle_recording():
    """Play back the caller's recording."""

    recording_url = request.values.get("RecordingUrl", None)

    resp = VoiceResponse()
    resp.say("Thanks for that... take a listen to what you recorded.")
    resp.play(recording_url)
    resp.say("Goodbye.")
    return str(resp)


@app.route("/message", methods=['POST'])
def awkward_text():
    """sends text to requested number."""
    # TODO need to create a page with form that accepts users phone input
    phone_raw = request.form.get("recipient", "415-969-4250")

    response = sms_functions.eval_phone(phone_raw)

    return render_template("confirm_sms", response=response)


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    resp = MessagingResponse()

    sms_string = sms_functions.get_message()

    resp.message(sms_string)

    return str(resp)

################################################################################
if __name__ == "__main__":

    DEBUG = "NO_DEBUG" not in os.environ
    PORT = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=PORT)
