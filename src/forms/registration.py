from wtforms import Form, StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, Length, EqualTo, Regexp
from validators.users import UsernameIsUnique, EmailIsUnique
from lib.widgets.optional_icon_input import OptionalIconTextInput, OptionalIconPasswordInput


class RegistrationForm(Form):
    username = StringField("Username",
                           [InputRequired(),
                            Length(min=3),
                            Regexp(regex=r"^[a-zA-Z]{3,24}(?:\s[a-zA-Z]+)*$"),
                            UsernameIsUnique()],
                            widget=OptionalIconTextInput(icon=True,
                                                     name="fa-user"))

    email = StringField("Email",
                        [InputRequired(),
                         Email(),
                         EmailIsUnique()],
                         widget=OptionalIconTextInput(icon=True,
                                                  name="fa-envelope"))

    password = PasswordField("Password",
                             [InputRequired(),
                              EqualTo("confirm", "Passwords must match"),
                              Length(min=4, max=16)],
                              widget=OptionalIconPasswordInput(icon=True,
                                                       name="fa-key"))

    confirm = PasswordField("Confirm",
                            [InputRequired()],
                            widget=OptionalIconPasswordInput(icon=True,
                                                     name="fa-key"))

    submit = SubmitField()
