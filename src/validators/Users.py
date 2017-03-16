from wtforms.validators import ValidationError
from models.Users import Users


class UsernameIsUnique(object):
    def __init__(self, message=None):
        if not message:
            message = u'This username is already used'
        self.message = message

    def __call__(self, form, field):
        # Return a error if a user with the same username is found
        if Users.all(keys_only=True).filter("username", field.data).get():
            raise ValidationError(self.message)
