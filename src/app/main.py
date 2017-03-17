from framework.request_handler import Handler
from models.Posts import Posts


class MainPage(Handler):
    def get(self):
        posts = Posts.all().order("-creation_date")
        self.render("home/home.html", posts=posts)
