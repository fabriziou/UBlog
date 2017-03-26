from wtforms import Form, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Length


class CommentForm(Form):
    content = TextAreaField("Comment",
                            [InputRequired(),
                             Length(min=5)],
                            id="comment")

    submit = SubmitField()
