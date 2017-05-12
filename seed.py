"""Utility - seeds tables."""

from sqlalchemy import func
from model import connect_to_db, db
from model import ###
from xxx import ###


def seed_table():
    """Seeds a table to the DB"""

    db.session.add(xxx)

    db.session.commit()
    print "Done seeding table"

################################################################################
if __name__ == "__main__":

    from passlib.hash import argon2
    from server import app
    connect_to_db(app)

    # In case tables haven't been created, create them
    db.create_all()
