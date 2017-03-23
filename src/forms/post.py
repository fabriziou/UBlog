from wtforms import Form, StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Length


class PostForm(Form):
    title = StringField("Title",
                        [InputRequired(),
                         Length(max=200)])

    content = TextAreaField("Content",
                            [InputRequired(),
                             Length(min=50)])

    submit = SubmitField()
