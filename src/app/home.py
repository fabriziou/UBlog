from framework.request_handler import Handler
from models.post import Post


class HomePage(Handler):
    def get(self):
        posts = Post.get_all()
        
        self.render("home/page.html", posts=posts)
