from google.appengine.ext import db


class Comment(db.Model):
    user = db.ReferenceProperty(required=True)
    content = db.TextProperty(required=True)
    creation_date = db.DateTimeProperty(auto_now_add=True)
    last_modification = db.DateTimeProperty(auto_now=True)
    is_deleted = db.BooleanProperty(default=False)

    @classmethod
    def new_comment(cls, content, user, post):
        """ Create new comment

            :param content:
                Comment's content
            :param user:
                User entity, author of the comment
            :param post:
                Post entity
        """
        comment = cls(parent=post, user=user, content=content)

        return comment.put()

    @classmethod
    def get_all_by_post(cls, post, order_by="creation_date", before=None):
        """ Return all comments from a given post that are not deleted

            :param post:
                Post entity
            :param order_by:
                Property to sort on
            :param before:
                Get comments created prior to that date
            :returns:
                List of Comments
        """
        comments = cls.all().ancestor(post)
        comments.filter("is_deleted", False)
        if before:
            comments.filter("creation_date <", before)

        comments.order(order_by)

        return comments

    @staticmethod
    def update_comment(comment, content):
        """ Update comment

            :param comment:
                Instance of comment
            :param content:
                Comment's content
            :returns:
                The updated instance
        """
        comment.content = content

        return comment.put()

    @staticmethod
    def delete_comment(comment):
        """ Delete comment

            :param comment:
                Instance of comment
            :returns:
                The updated instance
        """
        comment.is_deleted = True

        return comment.put()

    @classmethod
    def get_nb_comments(cls, post):
        """ Get number of comments of a post

            :param post:
                Post entity
            :returns:
                Number of comments of a given post
        """
        comments = cls.all().ancestor(post).filter("is_deleted", False)

        return comments.count()

    @classmethod
    def get_comments_per_posts(cls, posts):
        """ Get the number of comments for a given list of posts

            :param posts:
                List of posts
            :returns:
                A dictionary containing
                the key of post and the number of comments
        """
        comments = {}

        for post in posts:
            comments[post.key()] = cls.get_nb_comments(post)

        return comments
