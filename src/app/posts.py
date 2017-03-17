from framework.request_handler import Handler
from forms.post import PostForm
from models.Posts import Posts


# UNUSED #
class PostsPage(Handler):
    def get(self):
        self.render("home/home.html")


class AddPostPage(Handler):
    def get(self):
        """Generate an empty form and render it
        """
        form = PostForm()
        self.render_addpost(form)

    def post(self):
        """If the form is valid, the post is created
        and user is redirected to home page

        If an error occurred, form is displayed with
        details of error
        """
        form = PostForm(self.request.POST)

        if form.validate():
            # Post creation
            if Posts.new_post(form.title.data, form.content.data,
                              self.user.key()):
                self.redirect(self.uri_for("home"))
        self.render_addpost(form)

    def render_addpost(self, form):
        """Include the form in a template and render it

            :param form:
                A :class:`Form` instance.
        """
        self.render("posts/add_post.html", form=form)
