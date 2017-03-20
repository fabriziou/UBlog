from google.appengine.ext import db


class Post(db.Model):
    title = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    creation_date = db.DateTimeProperty(auto_now_add=True)
    last_modification = db.DateTimeProperty(auto_now=True)
    is_deleted = db.BooleanProperty(default=False)

    @classmethod
    def new_post(cls, title, content, user):
        """ Create new post

            :param title:
                Post's title
            :param content:
                Post's content
            :param user:
                User entity, author of the post
            :returns:
                Post entity
        """
        post = cls(parent=user, title=title, content=content, user=user)

        return post.put()

    @classmethod
    def get_all_by_user(cls, user, order_by="-creation_date"):
        """ Return all posts from a given user that are not deleted

            :param user:
                Users entity
            :param order_by:
                Property to sort on
            :returns:
                List of Posts
        """
        posts = cls.all().ancestor(user)

        posts.filter("is_deleted", False)

        posts.order(order_by)

        return posts

    @classmethod
    def get_all(cls, order_by="-creation_date"):
        """ Return all posts that are not deleted

            :param order_by:
                Property to sort on
            :returns:
                List of Posts
        """
        return cls.all().filter("is_deleted", False).order(order_by)

    @staticmethod
    def update_post(post, title, content):
        """ Update post

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
