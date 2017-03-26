from wtforms import Form, StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, Length
from lib.widgets.opt_icon_input import OptIconTextInput, OptIconPasswordInput


class LoginForm(Form):
    email = StringField("Email",
                        [InputRequired(),
                         Email()],
                        widget=OptIconTextInput(icon=True,
                                                name="fa-envelope"))

    password = PasswordField("Password",
                             [InputRequired(),
                              Length(min=4, max=16)],
                             widget=OptIconPasswordInput(icon=True,
                                                         name="fa-key"))

    submit = SubmitField()
