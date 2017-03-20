from wtforms import Form, StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length


class LoginForm(Form):
    email = StringField("Email",
                        [InputRequired(),
                         Email()])

    password = PasswordField("Password",
                             [InputRequired(),
                              Length(min=4, max=16)])
