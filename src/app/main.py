from framework.request_handler import Handler
from models.Posts import Posts


class MainPage(Handler):
    def get(self):
        posts = Posts.all()
        print posts
        self.render("home/home.html", posts=posts)
