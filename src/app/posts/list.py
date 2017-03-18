from framework.request_handler import Handler
from models.post import Post


class ListPostsPage(Handler):
    def get(self):
        """ Get all user's posts and render them
        """
        posts = Post.get_all_by_user(self.user)
        self.render("posts/list.html", posts=posts)
