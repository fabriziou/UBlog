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
    def get_all_by_post(cls, post, order_by="creation_date"):
        """ Return all comments from a given post that are not deleted

            :param post:
                Post entity
            :param order_by:
                Property to sort on
            :returns:
                List of Comments
        """
        comments = cls.all().ancestor(post)
        comments.filter("is_deleted", False)
        comments.order(order_by)

        return comments

    @classmethod
    def get_nb_comments_per_posts(cls, posts):
        """ Get the number of comments for a given list of posts

            :param posts:
                List of posts
            :returns:
                A dictionary containing
                the key of post and the number of comments
        """
        comments = {}

        for post in posts:
            comments[post.key()] = cls.get_all_by_post(post).count()

        return comments
