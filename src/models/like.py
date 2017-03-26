from google.appengine.ext import db


class Like(db.Model):
    user = db.ReferenceProperty(required=True)
    creation_date = db.DateTimeProperty(auto_now_add=True)
    last_modification = db.DateTimeProperty(auto_now=True)
    is_deleted = db.BooleanProperty(default=False)

    @classmethod
    def new_like(cls, user, post):
        """ Create new like

            :param user:
                User entity
            :param post:
                Post entity
            :returns:
                Like entity
        """
        like = cls(parent=post, user=user)

        return like.put()

    @staticmethod
    def delete_like(like):
        """ Set a Like entity as deleted

            :param like:
                Like entity
            :returns:
                The updated entity
        """
        like.is_deleted = True

        return like.put()

    @classmethod
    def is_liked_by_user(cls, user, post):
        """ Check if a post is liked by user

            :param user:
                User entity
            :param post:
                Post entity
            :returns:
                If user likes the post, an instance of Like is returned
                Otherwise, None is returned

        """
        like = cls.all().ancestor(post)

        like.filter("is_deleted", False)
        like.filter("user", user)

        return like.get()

    @classmethod
    def get_nb_like(cls, post):
        """ Get number of likes of a post

            :param post:
                Post entity
            :returns:
                Number of likes of a given post
        """
        likes = cls.all().ancestor(post).filter("is_deleted", False)

        return likes.count()

    @classmethod
    def get_nb_likes_per_posts(cls, posts):
        """ Get the number of likes for a given list of posts

            :param posts:
                List of posts
            :returns:
                A dictionary containing
                the key of post and the number of likes
        """
        likes = {}

        for post in posts:
            likes[post.key()] = cls.get_nb_like(post)

        return likes
