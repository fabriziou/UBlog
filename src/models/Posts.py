from google.appengine.ext import db
from models.Users import Users


class Posts(db.Model):
    title = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    user = db.ReferenceProperty(Users)
    creation_date = db.DateTimeProperty(auto_now_add=True)
    last_modification = db.DateTimeProperty(auto_now=True)
    is_deleted = db.BooleanProperty(default=False)

    @classmethod
    def new_post(cls, title, content, user):
        """ Create new entity in Datastore

            :param title:
                Post's title
            :param content:
                Post's content
            :param user:
                User entity, author of the post
        """
        post = cls(title=title, content=content, user=user)
        return post.put()

    @classmethod
    def get_all_by_user(cls, user, order_by="-creation_date"):
        """ Return all Posts that are not deleted from a given user

            :param user:
                Users entity
            :param order_by:
                Property to sort on
            :returns:
                List of Posts
        """
        posts = cls.all()
        posts.filter("user", user.key()).filter("is_deleted", False)
        posts.order(order_by)
        return posts

    @classmethod
    def get_all(cls, order_by="-creation_date"):
        """ Return all Posts that are not deleted

            :param order_by:
                Property to sort on
            :returns:
                List of Posts
        """
        return cls.all().filter("is_deleted", False).order(order_by)

    @staticmethod
    def update_post(post, title, content):
        """ Update the post

            :param post:
                Instance of post
            :param title:
                Post's title
            :param content:
                Post's content
            :returns:
                The updated instance
        """
        post.title = title
        post.content = content
        return post.put()
