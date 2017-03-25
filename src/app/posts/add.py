from lib.request_handler import Handler
from app.posts.postpage import PostPage
from forms.post import PostForm
from models.post import Post


class AddPost(PostPage):

    @Handler.login_required(True)
    def get(self):
        """ Display the form to add a post
        """
        form = PostForm()

        self.render_addpost(form)

    @Handler.login_required(True)
    def post(self):
        """ Create a post and redirect the user to the post

        If error, display form with errors details
        """
        form = PostForm(self.request.POST)

        if form.validate():
            post_key = Post.new_post(form.title.data, form.content.data,
                                     self.user)

            if post_key:
                self.redirect_to("viewpost", post_key=post_key)
            else:
                self.abort(500)

        self.render_addpost(form)
