from google.appengine.ext import db


class Users(db.Model):
    username = db.StringProperty(required=True)
    email = db.StringProperty(required=True)
    password = db.StringProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    isDeleted = db.BooleanProperty(default=False)
