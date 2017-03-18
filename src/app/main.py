from framework.request_handler import Handler
from models.posts import Posts


class MainPage(Handler):
    def get(self):
        posts = Posts.get_all()
        self.render("home/page.html", posts=posts)
