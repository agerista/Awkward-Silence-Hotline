# from flask import Flask, request
# from random import choice

# COMPLIMENTS = ["smart", "clever", "tenacious", "awesome", "Pythonic"]

# @app.route('/')
# def offer_greeting():
#     """Greet user."""

#     player = request.args.get("person")  # ... what the user typed!
#     nice_thing = choice(COMPLIMENTS)

#     return "<html><body>Hi, %s. I think you're %s!</body></html>" % (
#         player, nice_thing)