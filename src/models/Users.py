from google.appengine.ext import db
from hashlib import sha256
from base64 import b64encode
from os import urandom
from framework.cookie_handler import read_cookie


class Users(db.Model):
    username = db.StringProperty(required=True)
    email = db.StringProperty(required=True)
    password = db.StringProperty(required=True)
    creation_date = db.DateTimeProperty(auto_now_add=True)
    is_deleted = db.BooleanProperty(default=False)

    @classmethod
    def new_user(cls, email, username, password):
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
        """Retrieve user by its email

            :param email:
                Email of the user
            :returns:
                If successful, an instance of Users is returned
                Otherwise, None is returned
        """
        return cls.all().filter("email", email.lower()).get()

    @classmethod
    def get_by_cookie(cls, cookie):
        """Retrieve user by his cookie

            :param cookie:
                Cookie that contains the user id
            :returns:
                If successful, an instance of Users is returned
                Otherwise, None is returned
        """
        if cookie:
            uid = int(read_cookie(cookie))
            if uid:
                return cls.get_by_id(uid)
        return None

    @staticmethod
    def crypt_password(password, salt=None):
        """Crypt password with salt

            :param password:
                Password to crypt
            :param salt:
                String of chars
            :returns:
                Return the hashed password
        """
        if not salt:
            random_bytes = urandom(64)
            salt = b64encode(random_bytes).decode('utf-8')
        hashed_password = salt + sha256(salt + password).hexdigest()
        return hashed_password
