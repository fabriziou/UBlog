from framework.request_handler import Handler
from models.post import Post
from forms.comment import CommentForm
from models.comment import Comment


class ViewPostPage(Handler):
    post = None
    comments = None

    def is_post_valid(func):
        """ Check if post is valid

        An error is thrown if :
            * Post Unknown
            * Post is deleted
        """
        def is_valid(self, post_key):
            self.post = Post.get(post_key)

            # Check Post
            if (not self.post or self.post.is_deleted):
                self.abort(404)

            self.comments = Comment.get_all_by_post(self.post)

            return func(self, post_key)
        return is_valid

    @is_post_valid
    def get(self, post_key):
        """ Display a post and its comments
            Generate a form to post comments

            :param post_key:
                Key of the post to display
        """
        form = CommentForm()

        self.render_viewpost(form)

    @Handler.login_required(True)
    @is_post_valid
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

    def render_viewpost(self, form):
        """ Include all datas in a template
            and render the page
        """
        self.render("posts/view.html", form=form,
                    post=self.post, comments=self.comments)
