from google.appengine.ext import db
import re


class Users(db.Model):
    email = db.StringProperty(required=True)
    username = db.StringProperty(required=True)
    password = db.StringProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    isDeleted = db.BooleanProperty(default=False)

    @classmethod
    def create_user(cls, email, username, password):
        user = User(email=email, username=username, password=password)
        user.put()
        return user

    @staticmethod
    def is_email_valid(email, error=None):
        """ Check if email is valid

            Regular expression used:
            r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

            :param email:
                Email to check
            :param error:
                If error, error["email"] will be set with an error message
            :returns:
                If email is valid, we return True
                Otherwise, we return False
        """
        if email:
            if (re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
                         email)):
                return True
            error['email'] = "Invalid email"
        else:
            error['email'] = "Email must not be empty"
        return False

    @staticmethod
    def is_username_valid(username, error=None):
        """ Check if username is valid.

            A valid username is a least 2 chars long

            Regular expression used:
            r"(^[a-zA-Z]{2,}(?:\s[a-zA-Z]+)*$)"

            :param username:
                Username to check
            :param error:
                If error, error["username"] will be set with an error message
            :returns:
                If username is valid, we return True
                Otherwise, we return False
        """

        if username:
            if (re.match(r"^[a-zA-Z]{2,}(?:\s[a-zA-Z]+)*$",
                         username)):
                return True
            else:
                error["username"] = "Invalid username"
        else:
            error["username"] = "Username must not be empty"
        return False

    @staticmethod
    def is_password_valid(password, error=None):
        """ Check if password is valid

            A valid password is between 4 and 8 digits long and
            include at least one numeric digit

            Regular expression used:
            r"(^(?=.*\d).{4,8}$)

            :param password:
                Email to check
            :param error:
                If error, error["password"] will be set with an error message
            :returns:
                If password is valid, we return True
                Otherwise, we return False
        """
        if password:
            if (re.match(r"^(?=.*\d).{4,8}$",
                         password)):
                return True
            error['password'] = """Invalid password: it must be between
            4 and 8 digits long include at least one numeric digit"""
        else:
            error['password'] = "Password must not be empty"
        return False
