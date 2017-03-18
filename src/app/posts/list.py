from framework.request_handler import Handler
from models.posts import Posts


class ListPostsPage(Handler):
    def get(self):
        """ Get all user's posts and render them
        """
        posts = Posts.get_all_by_user(self.user)
        self.render("posts/list.html", posts=posts)
