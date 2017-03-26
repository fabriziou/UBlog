from wtforms import Form, StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Length
from lib.widgets.opt_icon_input import OptIconTextInput


class PostForm(Form):
    title = StringField("Title",
                        [InputRequired(),
                         Length(max=200)],
                        widget=OptIconTextInput(icon=True,
                                                name="fa-font"))

    content = TextAreaField("Content",
                            [InputRequired(),
                             Length(min=50)])

    submit = SubmitField()
