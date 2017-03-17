from wtforms import Form, StringField, TextAreaField
from wtforms.validators import InputRequired, Length


class PostForm(Form):
    title = StringField('Title', [InputRequired(), Length(max=200)])
    content = TextAreaField('Content', [InputRequired(), Length(min=50)])
