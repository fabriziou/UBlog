from framework.request_handler import Handler
from models.post import Post
from forms.comment import CommentForm
from models.comment import Comment


class ViewPostPage(Handler):
    def get(self, post_key, comment_key=None):
        """ Get post in paramater with its comment and render them
            A form to create comments is generated

            :param post_key:
                Key of the post
        """
        # Post
        post = Post.get(post_key)
        # Comments
        form = CommentForm()
        comments = Comment.get_all_by_post(post)
        self.render_viewpost(post, form, comments)

    def post(self, post_key, comment_key=None):
        # Post
        post = Post.get(post_key)
        # Comments
        form = CommentForm(self.request.POST)
        comments = Comment.get_all_by_post(post)
        if form.validate():
            # Post creation
            comment_key = Comment.new_comment(form.content.data, self.user,
                                              post)
            if comment_key:
                self.redirect_to("viewpost", post_key=post_key,
                                 _fragment=str(comment_key))
        self.render_viewpost(post, form, comments)

    def render_viewpost(self, post, form, comments):
        self.render("posts/view.html", post=post, form=form, comments=comments)
