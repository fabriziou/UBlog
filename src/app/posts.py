from framework.request_handler import Handler

## UNUSED ##
class PostsPage(Handler):
    def get(self):
        self.render("home/home.html")

class AddPostPage(Handler):
    def get(self):
        self.render("home/home.html")
