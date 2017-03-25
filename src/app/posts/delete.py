from lib.request_handler import Handler
from app.posts.postpage import PostPage
from models.post import Post


class DeletePost(PostPage):

    @Handler.login_required(True)
    @PostPage.is_post_valid
    @PostPage.is_post_author
    def get(self, post_key):
        """ List all user's posts
        """
        success = Post.delete_post(self.post)
        if success:
            self.redirect_to("userposts")
        else:
            self.abort(404)
