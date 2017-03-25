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
    def get_all(cls, user=None, order_by="-creation_date"):
        """ Return posts that are not deleted

            :param user:
                User entity
            :param order_by:
                Property to sort on
            :param limit:
                Number of posts we want to retrieve
            :param offset:
                Optional number of results to skip first
            :returns:
                List of Posts
        """
        res = cls.all()

        if user:
            res = res.ancestor(user)

        res = res.filter("is_deleted", False).order(order_by)

        return res

    @classmethod
    def get_nb_posts(cls, user=None):
        """ Get number of posts

            :param user:
                User entity
            :returns:
                Number of posts
        """
        posts = cls.all()

        if user:
            posts = posts.ancestor(user)

        posts = posts.filter("is_deleted", False)

        return posts.count()

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

    @staticmethod
    def delete_post(post):
        """ Set the post to be deleted

            :param post:
                Instance of post
            :returns:
                The updated instance
        """
        post.is_deleted = True

        return post.put()
