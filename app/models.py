import random
import string

from app.db import db

USERNAME_LENGTH = 100

# BEGIN MODELS.PY
# Create our database model
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    # the way we name user is different from the key
    # the name is a randomly generated string
    # this way makes it hard for people to guess other's
    # user names
    userid = db.Column(db.String(120), unique=True)

    def __init__(self):
        self.userid = ''.join(random.choices(string.ascii_letters + string.digits, k=USERNAME_LENGTH))
        # while there is already a user with the same user id, try different id, and
        # write a warning to the console
        if db.session.query(User).filter(User.userid == self.userid).count():
            self.userid = ''.join(random.choices(string.ascii_letters + string.digits, k=USERNAME_LENGTH))
            print("WARNING","USER ID COLLISION", self.userid)

    def __repr__(self):
        return '<%r, %s>' % (self.id, self.userid)

