from wtforms import Form, TextAreaField
from wtforms.validators import InputRequired, Length


class CommentForm(Form):
    content = TextAreaField('Comment', [InputRequired(), Length(min=5)])
