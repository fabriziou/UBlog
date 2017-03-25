from lib.request_handler import Handler
from app.posts.postpage import PostPage
from models.comment import Comment


class DeleteComment(PostPage):

    @Handler.login_required(True)
    @PostPage.is_post_valid
    @PostPage.is_comment_author
    def get(self, post_key, comment_key):
        """ Delete a comment

            :param post_key:
                Post to which the comment belongs to
            :param comment_key:
                Comment to delete
        """
        if Comment.delete_comment(self.user_comment):
            self.redirect_to("viewpost", post_key=post_key)
        else:
            self.abort(500)
