from google.appengine.ext import db
from hashlib import sha256
from base64 import b64encode
from os import urandom
from lib.cookie_handler import read_cookie


class User(db.Model):
    username = db.StringProperty(required=True)
    email = db.StringProperty(required=True)
    password = db.StringProperty(required=True)
    creation_date = db.DateTimeProperty(auto_now_add=True)
    is_deleted = db.BooleanProperty(default=False)

    @classmethod
    def new_user(cls, email, username, password):
        """ Create a new user

            :param email:
                User's email
            :param username:
                User's username
            :param password:
                User's password (not hashed)
            :returns:
                If successful, the user key is returned
                Otherwise, None is returned
        """
        # Format datas, crypt password
        username = username.title()
        email = email.lower()
        password = cls.crypt_password(password)

        user = cls(username=username,
                   email=email,
                   password=password)

        return user.put()

    @classmethod
    def get_by_email(cls, email):
        """ Get user by its email

            :param email:
                Email of the user
            :returns:
                If successful, an instance of Users is returned
                Otherwise, None is returned
        """
        return cls.all().filter("email", email.lower()).get()

    @classmethod
    def get_by_cookie(cls, cookie):
        """ Get user by his cookie

            :param cookie:
                Cookie that contains the user key
            :returns:
                If successful, an instance of Users is returned
                Otherwise, None is returned
        """
        if cookie:
            user_key = read_cookie(cookie)

            if user_key:
                return cls.get(user_key)

        return None

    @staticmethod
    def crypt_password(password, salt=None):
        """ Crypt password with salt

            A salt is generated if not given

            :param password:
                Password to crypt
            :param salt:
                String of chars
            :returns:
                Hashed password
        """
        if not salt:
            random_bytes = urandom(64)
            salt = b64encode(random_bytes).decode('utf-8')

        hashed_password = salt + sha256(salt + password).hexdigest()

        return hashed_password
