from lib.request_handler import Handler
from models.post import Post
from models.comment import Comment
from models.like import Like


class PostPage(Handler):
    post = None
    comments = None
    user_comment = None
    nb_likes = 0
    nb_comments = 0

    @staticmethod
    def is_post_valid(func):
        """ Check if post is valid

        If post is valid,
            comments and nb likes from this post are retrieved

        An error is thrown if :
            * Post Unknown
            * Post is deleted
        """
        def is_valid(self, post_key, comment_key=None):
            self.post = Post.get(post_key)

            # Check Post
            if (not self.post or self.post.is_deleted):
                self.errors.append("Post unknown")
                self.abort(404)

            self.comments = Comment.get_all_by_post(self.post)
            self.nb_likes = Like.get_nb_like(self.post)
            self.nb_comments = self.comments.count()

            # Not all GET() and POST() takes a comment_key params
            if comment_key:
                return func(self, post_key, comment_key)
            else:
                return func(self, post_key)

        return is_valid

    @staticmethod
    def is_post_author(func):
        """ Check if user is authorized to update a post

        An error is thrown if :
            * User is not the author of the post
        """
        def is_valid(self, post_key):
            # Check author
            if (not self.user or self.post.parent().key() != self.user.key()):
                self.errors.append("You are not allowed to update this post")
                self.abort(404)

            return func(self, post_key)
        return is_valid

    @staticmethod
    def is_comment_author(func):
        """ Check if user is authorized to update a comment

        An error is thrown if :
            * Comment is unknown
            * Comment is deleted
            * User not the author of the comment
        """
        def is_valid(self, post_key, comment_key):
            self.user_comment = Comment.get(comment_key)

            # Check Comment
            if (not self.user_comment or self.user_comment.is_deleted):
                self.errors.append("Unknown comment")
                self.abort(404)

            # Check Author
            if self.user_comment.user.key() != self.user.key():
                self.errors.append("You are not allowed " +
                                   "to update this comment")
                self.abort(404)

            comment_date = self.user_comment.creation_date
            self.comments = Comment.get_all_by_post(self.post,
                                                    before=comment_date)

            return func(self, post_key, comment_key)
        return is_valid

    """ Renders
        Include all datas in a template
        and render the page
    """
    def render_addpost(self, form):
        self.render("posts/add.html", form=form)

    def render_editpost(self, form):
        self.render("posts/edit.html", form=form, post=self.post)

    def render_viewpost(self, form, is_liked):
        self.render("posts/view.html", form=form, is_liked=is_liked,
                    nb_likes=self.nb_likes, nb_comments=self.nb_comments,
                    post=self.post, comments=self.comments)

    def render_editcomment(self, form):
        self.render("comments/edit.html", form=form, comment=self.user_comment)
