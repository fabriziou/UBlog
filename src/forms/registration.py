from wtforms import Form, StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length, EqualTo, Regexp


class RegistrationForm(Form):
    username = StringField('Username', [InputRequired(),
                                        Length(min=3),
                                        Regexp(regex=r"^[a-zA-Z]{3,24}" +
                                        r"(?:\s[a-zA-Z]+)*$")])
    email = StringField('Email', [InputRequired(), Email()])
    password = PasswordField('Password', [InputRequired(),
                                          EqualTo('confirm',
                                          message='Passwords must match'),
                                          Length(min=4, max=16)])
    confirm = PasswordField('Confirm', [InputRequired()])
