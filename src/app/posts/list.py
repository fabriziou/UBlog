from framework.request_handler import Handler
from models.post import Post


class ListPostsPage(Handler):
    @Handler.login_required(True)
    def get(self):
        """ List all user's posts
        """
        posts = Post.get_all_by_user(self.user)
        
        self.render("posts/list.html", posts=posts)
