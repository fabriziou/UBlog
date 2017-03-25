from lib.request_handler import Handler
from app.posts.postpage import PostPage
from models.comment import Comment
from forms.comment import CommentForm


class EditComment(PostPage):

    @Handler.login_required(True)
    @PostPage.is_post_valid
    @PostPage.is_comment_author
    def get(self, post_key, comment_key):
        """ Display the form to edit a comment

            :param post_key:
                Key of the post which the comment belongs to
            :param comment_key:
                Key of the comment
        """
        form = CommentForm(obj=self.user_comment)

        self.render_editcomment(form)

    @Handler.login_required(True)
    @PostPage.is_post_valid
    @PostPage.is_comment_author
    def post(self, post_key, comment_key):
        """ Update comment and redirect user to the post page

        If error, display form with errors details

            :param post_key:
                Key of the post which the comment belongs to
            :param comment_key:
                Key of the comment
        """
        form = CommentForm(self.request.POST)

        if form.validate():
            comment_key = Comment.update_comment(self.user_comment,
                                                 form.content.data)
            # UPDATE success
            if comment_key:
                self.redirect_to("viewpost", post_key=post_key,
                                 _fragment=str(comment_key))
            else:
                self.abort(500)

        self.render_editcomment(form)
