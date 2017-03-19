from framework.request_handler import Handler
from forms.comment import CommentForm
from models.post import Post
from models.comment import Comment


class EditCommentPage(Handler):
    def get(self, post_key, comment_key):
        """ Display the form to edit a comment

            :param post_key:
                Key of the post
            :param comment_key:
                Key of the comment
        """
        post = Post.get(post_key)
        comment = Comment.get(comment_key)
        old_comments = Comment.get_all_by_post(post=post, before_date=comment.creation_date)
        form = CommentForm(obj=comment)
        self.render_editcomment(form=form, post=post, comments=old_comments)

    def post(self, post_key, comment_key):
        """ Display the form to edit a comment

            :param post_key:
                Key of the post
            :param comment_key:
                Key of the comment
        """
        post = Post.get(post_key)
        comment = Comment.get(comment_key)
        old_comments = Comment.get_all_by_post(post=post, before_date=comment.creation_date)
        form = CommentForm(self.request.POST)
        if form.validate():
            comment_key = Comment.update_comment(comment, form.content.data)
            if comment_key:
                self.redirect_to("viewpost", post_key=post_key,
                                 _fragment=str(comment_key))

        self.render_editcomment(form=form, post=post, comments=old_comments)

    def render_editcomment(self, form, post, comments):
        """Include the form in a template and render it

            :param form:
                A :class:`Form` instance.
        """
        self.render("comments/edit.html", form=form, post=post, comments=comments)
