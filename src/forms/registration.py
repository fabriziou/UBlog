from wtforms import Form, StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, Length, EqualTo, Regexp
from validators.users import UsernameIsUnique, EmailIsUnique
from lib.widgets.opt_icon_input import OptIconTextInput, OptIconPasswordInput


class RegistrationForm(Form):
    username = StringField("Username",
                           [InputRequired(),
                            Length(min=3),
                            Regexp(regex=r"^[a-zA-Z]{3,24}(?:\s[a-zA-Z]+)*$"),
                            UsernameIsUnique()],
                           widget=OptIconTextInput(icon=True,
                                                   name="fa-user"))

    email = StringField("Email",
                        [InputRequired(),
                         Email(),
                         EmailIsUnique()],
                        widget=OptIconTextInput(icon=True,
                                                name="fa-envelope"))

    password = PasswordField("Password",
                             [InputRequired(),
                              EqualTo("confirm", "Passwords must match"),
                              Length(min=4, max=16)],
                             widget=OptIconPasswordInput(icon=True,
                                                         name="fa-key"))

    confirm = PasswordField("Confirm",
                            [InputRequired()],
                            widget=OptIconPasswordInput(icon=True,
                                                        name="fa-key"))

    submit = SubmitField()
