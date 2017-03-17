from framework.request_handler import Handler
from forms.post import PostForm
from models.Posts import Posts


# UNUSED #
class PostsPage(Handler):
    def get(self):
        self.render("home/home.html")


class AddPostPage(Handler):
    def get(self):
        form = PostForm()
        self.render_addpost(form)

    def post(self):
        form = PostForm(self.request.POST)

        print self.user.key()
        if form.validate():
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
