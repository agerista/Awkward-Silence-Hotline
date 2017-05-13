from flask import Flask, request
from random import choice

COMPLIMENTS = ["smart", "clever", "tenacious", "awesome", "Pythonic"]

@app.route('/')
def offer_greeting():
    """Greet user."""

    player = "you"  # ... what the user typed!
    nice_thing = choice(COMPLIMENTS)

    return "<html><body>Hi, %s. I think you're %s!</body></html>" % (
        player, nice_thing)

if __name__ == "__main__":
    DEBUG = "NO_DEBUG" not in os.environ
    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
