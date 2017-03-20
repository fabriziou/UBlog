from framework.request_handler import Handler
from app.posts.postpage import PostPage
from models.post import Post
from models.comment import Comment
from forms.comment import CommentForm


class ViewPost(PostPage):
    @PostPage.is_post_valid
    def get(self, post_key):
        """ Display a post and its comments
            Generate a form to post comments

            :param post_key:
                Key of the post to display
        """
        form = CommentForm()

        self.render_viewpost(form)

    @Handler.login_required(True)
    @PostPage.is_post_valid
    def post(self, post_key):
        """ Create a new comment and redirect user to the post page

        If error, display form with error details

            :param post_key:
                Key of the post to display
        """
        form = CommentForm(self.request.POST)

        if form.validate():
            comment_key = Comment.new_comment(form.content.data, self.user,
                                              self.post)

            if comment_key:
                self.redirect_to("viewpost", post_key=post_key,
                                 _fragment=str(comment_key))

        self.render_viewpost(form)
