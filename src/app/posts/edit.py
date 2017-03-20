from framework.request_handler import Handler
from forms.post import PostForm
from models.post import Post


class EditPostPage(Handler):
    post = None

    def is_edit_authorized(func):
        """ Check if user is authorized to edit this post

        An error is thrown if :
            * Post is unknown
            * Post is deleted
            * User is not the author of the post
        """
        def is_valid(self, post_key):
            self.post = Post.get(post_key)

            # Check post
            if (not self.post or self.post.is_deleted):
                self.errors.append("Post unknown")
                self.abort(404)

            # Check author
            if (not self.user or self.post.parent().key() != self.user.key()):
                self.errors.append("You are not authorized to edit this post")
                self.abort(404)

            return func(self, post_key)
        return is_valid

    @Handler.login_required(True)
    @is_edit_authorized
    def get(self, post_key):
        """ Display the form to edit a post

            :param post_key:
                Key of the post to edit
        """
        form = PostForm(obj=self.post)

        self.render_editpost(form)

    @Handler.login_required(True)
    @is_edit_authorized
    def post(self, post_key):
        """ Update post and redirect user to the post page

        If error, display form with errors details

            :param post_key:
                Key of the post to edit
        """
        form = PostForm(self.request.POST)

        if form.validate():
            if Post.update_post(self.post, form.title.data, form.content.data):
                self.redirect_to("viewpost", post_key=post_key)

        self.render_editpost(form)

    def render_editpost(self, form):
        """ Include all datas in a template
            and render the page
        """
        self.render("posts/edit.html", form=form)
