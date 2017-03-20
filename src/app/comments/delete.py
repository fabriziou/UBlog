from framework.request_handler import Handler
from app.comments.commentpage import CommentPage
from models.comment import Comment


class DeleteComment(CommentPage):

    @Handler.login_required(True)
    @CommentPage.is_edit_authorized
    def get(self, post_key, comment_key):
        """ Delete a comment
        """
        success = Comment.delete_comment(self.user_comment)
        if success:
            self.redirect_to("viewpost", post_key=post_key)
        else:
            self.abort(404)
