"""Models and database functions for Awkward Silence Hotline."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


##############################################################################
# Model definitions

class User(db.Model):
    """User of Awkward Silence Hotline."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    first_name = db.Column(db.String(40))
    last_name = db.Column(db.String(40))
    phone_number = db.Column(db.String(10))

    recordings = db.relationship("Recording")

    def __repr__(self):
        """Provide helpful representation when printed"""

        return "<User user_id=%s email=%s password=%s first_name=%s\
                last_name=%s>" % (self.user_id,
                                  self.email,
                                  self.password,
                                  self.first_name,
                                  self.last_name,
                                  self.phone_number)


class Recording(db.Model):
    """Stores awkward recordings by user"""

    __tablename__ = "recordings"

    recording_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))


##############################################################################
# Helper functions


def connect_to_db(app, db_uri="postgresql:///ash"):
    """Connect the database to our Flask app."""

    # Configure to use PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if you run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."
