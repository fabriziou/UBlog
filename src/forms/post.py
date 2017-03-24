from wtforms import Form, StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Length
from widgets.optional_icon_input import OptionalIconTextInput


class PostForm(Form):
    title = StringField("Title",
                        [InputRequired(),
                         Length(max=200)],
                         widget=OptionalIconTextInput(icon=True,
                                                      name="fa-font"))

    content = TextAreaField("Content",
                            [InputRequired(),
                             Length(min=50)])

    submit = SubmitField()
