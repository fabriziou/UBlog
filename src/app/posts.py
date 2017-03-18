from framework.request_handler import Handler
from forms.post import PostForm
from models.posts import Posts


class PostsPage(Handler):
    def get(self):
        """ Get all user's posts and render them
        """
        posts = Posts.get_all_by_user(self.user)
        self.render("posts/list.html", posts=posts)


class ViewPostPage(Handler):
    def get(self, post_key):
        """ Get post :param post_key: and render it

            :param post_key:
                Key of the post
        """
        post = Posts.get(post_key)
        self.render("posts/view.html", post=post)


class AddPostPage(Handler):
    def get(self):
        """Generate an empty form to add a post and render it
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
            if Posts.new_post(form.title.data, form.content.data, self.user):
                self.redirect_to("home")
        self.render_addpost(form)

    def render_addpost(self, form):
        """Include the form in a template and render it

            :param form:
                A :class:`Form` instance.
        """
        self.render("posts/add.html", form=form)


class EditPostPage(Handler):
    def get(self, post_key):
        """ Display the form to edit a post

            :param post_key:
                Key of the post to edit
        """
        post = Posts.get(post_key)

        # If user is not the author of the post
        #   We redirect to the home page
        if not self.is_the_author(post):
            self.redirect_to("home")

        form = PostForm(obj=post)
        self.render_editpost(form)

    def post(self, post_key):
        """If the form is valid, the post is updated
        and user is redirected to the post

        If user is not authorized to edit the post,
        he is redirected to homepage

        If an error occurred, form is displayed with
        details of error
        """
        post = Posts.get(post_key)

        # If user is not the author of the post
        #   We redirect to the home page
        if not self.is_the_author(post):
            self.redirect_to("home")

        form = PostForm(self.request.POST)

        if form.validate():
            if Posts.update_post(post, form.title.data, form.content.data):
                self.redirect_to("viewpost", post_key=post_key)
        self.render_editpost(form)

    def is_the_author(self, post):
        """ Check if user is the author of the post

            :param post:
                Post entity to edit
            :returns:
                If user is the author, we return True
                Otherwise, we return False
        """
        if (post and not post.is_deleted
                and post.parent().key() == self.user.key()):
            return True
        return False

    def render_editpost(self, form):
        """Include the form in a template and render it

            :param form:
                A :class:`Form` instance.
        """
        self.render("posts/edit.html", form=form)
