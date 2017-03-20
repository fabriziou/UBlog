from framework.request_handler import Handler
from forms.comment import CommentForm
from models.post import Post
from models.comment import Comment


class EditCommentPage(Handler):
    post = None
    comments = None
    user_comment = None

    def is_edit_authorized(func):
        """ Check if user is authorized to edit a comment

        An error is thrown if :
            * Post is unknown
            * Post is deleted
            * Comment is unknown
            * Comment is deleted
            * User not the auther of the comment
        """
        def is_valid(self, post_key, comment_key):
            self.post = Post.get(post_key)

            # Check Post
            if (not self.post or self.post.is_deleted):
                self.abort(404)

            self.user_comment = Comment.get(comment_key)

            # Check Comment
            if (not self.user_comment or self.user_comment.is_deleted):
                self.abort(404)

            comment_date = self.user_comment.creation_date
            self.comments = Comment.get_all_by_post(self.post,
                                                    before=comment_date)

            return func(self, post_key, comment_key)
        return is_valid

    @Handler.login_required(True)
    @is_edit_authorized
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
    @is_edit_authorized
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

        self.render_editcomment(form)

    def render_editcomment(self, form):
        """ Include all datas in a template
            and render the page
        """
        self.render("comments/edit.html", form=form,
                    post=self.post, comments=self.comments)
