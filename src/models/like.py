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
        """
        like = cls(parent=post, user=user)

        return like.put()

    @staticmethod
    def delete_like(like_key):
        like_key.is_deleted = True
        return like_key.put()

    @classmethod
    def get_like_by_user(cls, user, post):
        """ Get like by user
        """
        like = cls.all().ancestor(post)

        like.filter("is_deleted", False)
        like.filter("user", user)

        return like.get()
