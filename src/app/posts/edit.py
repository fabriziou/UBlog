from lib.request_handler import Handler
from app.posts.postpage import PostPage
from forms.post import PostForm
from models.post import Post


class EditPost(PostPage):

    @Handler.login_required(True)
    @PostPage.is_post_valid
    @PostPage.is_post_author
    def get(self, post_key):
        """ Display the form to edit a post

            :param post_key:
                Key of the post to edit
        """
        form = PostForm(obj=self.post)

        self.render_editpost(form)

    @Handler.login_required(True)
    @PostPage.is_post_valid
    @PostPage.is_post_author
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
