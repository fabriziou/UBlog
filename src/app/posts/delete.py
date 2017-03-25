from lib.request_handler import Handler
from app.posts.postpage import PostPage
from models.post import Post


class DeletePost(PostPage):

    @Handler.login_required(True)
    @PostPage.is_post_valid
    @PostPage.is_post_author
    def get(self, post_key):
        """ Delete user post

            :param post_key:
                Key of the post to delete
        """
        if Post.delete_post(self.post):
            self.redirect_to("userposts")
        else:
            self.abort(500)
