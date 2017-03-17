from google.appengine.ext import db
from models.Users import Users


class Posts(db.Model):
    title = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    user = db.ReferenceProperty(Users)
    creation_date = db.DateTimeProperty(auto_now_add=True)
    last_modification = db.DateTimeProperty(auto_now_add=True)
    is_deleted = db.BooleanProperty(default=False)

    @classmethod
    def new_post(cls, title, content, user):
        post = cls(title=title, content=content, user=user)
        return post.put()
