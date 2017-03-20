from framework.request_handler import Handler
from models.post import Post
from models.comment import Comment
from models.like import Like


class PostPage(Handler):
    post = None
    comments = None
    nb_likes = 0

    @staticmethod
    def is_post_valid(func):
        """ Check if post is valid

        If post is valid,
            comments and nb likes from this post are retrieved

        An error is thrown if :
            * Post Unknown
            * Post is deleted
        """
        def is_valid(self, post_key):
            self.post = Post.get(post_key)

            # Check Post
            if (not self.post or self.post.is_deleted):
                self.errors.append("Post unknown")
                self.abort(404)

            self.comments = Comment.get_all_by_post(self.post)
            self.nb_likes = Like.get_nb_like(self.post)

            return func(self, post_key)
        return is_valid

    @staticmethod
    def is_author(func):
        """ Check if user is authorized to update this post

        An error is thrown if :
            * User is not the author of the post
        """
        def is_valid(self, post_key):
            # Check author
            if (not self.user or self.post.parent().key() != self.user.key()):
                self.errors.append("You are not authorized to update this post")
                self.abort(404)

            return func(self, post_key)
        return is_valid

    """ Renders
        Include all datas in a template
        and render the page
    """
    def render_addpost(self, form):
        self.render("posts/add.html", form=form)

    def render_editpost(self, form):
        self.render("posts/edit.html", form=form)

    def render_viewpost(self, form, is_liked):
        self.render("posts/view.html", form=form, is_liked=is_liked,
                    nb_likes=self.nb_likes, post=self.post,
                    comments=self.comments)
