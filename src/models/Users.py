from google.appengine.ext import db
from hashlib import sha256
from base64 import b64encode
from os import urandom


class Users(db.Model):
    username = db.StringProperty(required=True)
    email = db.StringProperty(required=True)
    password = db.StringProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    isDeleted = db.BooleanProperty(default=False)

    @staticmethod
    def crypt_password(password):
        random_bytes = urandom(64)
        salt = b64encode(random_bytes).decode('utf-8')
        hashed_password = salt + sha256(salt + password).hexdigest()
        return hashed_password
