from flask import Flask, request
from random import choice


@app.route('/')
def offer_greeting():
    """Greet user."""

    return "<html><body>awkward....</body></html>" 

if __name__ == "__main__":
    DEBUG = "NO_DEBUG" not in os.environ
    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
