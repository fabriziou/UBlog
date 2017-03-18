from google.appengine.ext import db


class Comment(db.Model):
    user = db.ReferenceProperty(required=True)
    content = db.TextProperty(required=True)
    creation_date = db.DateTimeProperty(auto_now_add=True)
    last_modification = db.DateTimeProperty(auto_now=True)
    is_deleted = db.BooleanProperty(default=False)

    @classmethod
    def new_comment(cls, content, user, post):
        """ Create new entity in Datastore

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
    def get_all_by_post(cls, post, order_by="creation_date", before_date=None):
        """ Return all Comments that are not deleted from a given Post

            :param post:
                Post entity
            :param order_by:
                Property to sort on
            :param before_date:
                Get comments created prior to that date
            :returns:
                List of Comments
        """
        comments = cls.all().ancestor(post)
        comments.filter("is_deleted", False)
        if before_date:
            comments.filter("creation_date <", before_date)
        comments.order(order_by)
        return comments

    @staticmethod
    def update_comment(comment, content):
        """ Update the comment

            :param comment:
                Instance of comment
            :param content:
                Comment's content
            :returns:
                The updated instance
        """
        comment.content = content
        return comment.put()
