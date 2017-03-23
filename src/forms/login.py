from wtforms import Form, StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, Length
from widgets.optional_icon_input import OptionalIconTextInput, OptionalIconPasswordInput


class LoginForm(Form):
    email = StringField("Email",
                        [InputRequired(),
                         Email()],
                         widget=OptionalIconTextInput(icon=True,
                                                  name="fa-envelope"))

    password = PasswordField("Password",
                             [InputRequired(),
                              Length(min=4, max=16)],
                              widget=OptionalIconPasswordInput(icon=True,
                                                       name="fa-key"))

    submit = SubmitField()
