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

    @classmethod
    def get_all_by_user(cls, user, order_by="-creation_date"):
        return cls.all().filter("user", user.key()).order(order_by)

    @classmethod
    def get_all(cls, order_by="-creation_date"):
        return cls.all().order(order_by)

    @staticmethod
    def update_post(post, title, content):
        post.title = title
        post.content = content
        return post.put()
