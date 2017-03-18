from wtforms.validators import ValidationError
from models.user import User


class UsernameIsUnique(object):
    """ Form Validator:
        Raise an error if a User entity already has the username
    """
    def __init__(self, message=None):
        if not message:
            message = u'This username is already used'
        self.message = message

    def __call__(self, form, field):
        # Return a error if the username is found in Users
        if User.all(keys_only=True).filter("username", field.data).get():
            raise ValidationError(self.message)


class EmailIsUnique(object):
    """ Form Validator:
        Raise an error if a User entity already has the email
    """
    def __init__(self, message=None):
        if not message:
            message = u'This email is already used'
        self.message = message

    def __call__(self, form, field):
        # Return a error if the email is found in Users
        if User.all(keys_only=True).filter("email", field.data).get():
            raise ValidationError(self.message)
