from framework.request_handler import Handler
from forms.comment import CommentForm
from models.post import Post
from models.comment import Comment


class CommentPage(Handler):
    post = None
    comments = None
    user_comment = None

    @staticmethod
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
                self.errors.append("Unknown post")
                self.abort(404)

            self.user_comment = Comment.get(comment_key)

            # Check Comment
            if (not self.user_comment or self.user_comment.is_deleted):
                self.errors.append("Unknown comment")
                self.abort(404)

            comment_date = self.user_comment.creation_date
            self.comments = Comment.get_all_by_post(self.post,
                                                    before=comment_date)

            return func(self, post_key, comment_key)
        return is_valid

    def render_editcomment(self, form):
        """ Include all datas in a template
            and render the page
        """
        self.render("comments/edit.html", form=form,
                    post=self.post, comments=self.comments)
