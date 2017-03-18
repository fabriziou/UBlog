from framework.request_handler import Handler
from forms.post import PostForm
from models.Posts import Posts


class PostsPage(Handler):
    def get(self):
        """ Get all user's posts and render them
        """
        posts = Posts.get_all_by_user(self.user)
        self.render("posts/posts.html", posts=posts)

class ViewPostPage(Handler):
    def get(self, post_id):
        """ Get post :param post_id: and render it

            :param post_id:
                ID of the post
        """
        post = Posts.get_by_id(int(post_id))
        self.render("posts/post_details.html", post=post)

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
            if Posts.new_post(form.title.data, form.content.data,
                              self.user.key()):
                self.redirect_to("home")
        self.render_addpost(form)

    def render_addpost(self, form):
        """Include the form in a template and render it

            :param form:
                A :class:`Form` instance.
        """
        self.render("posts/add_post.html", form=form)

class EditPostPage(Handler):
    def get(self, post_id):
        """ Display the form to edit a post

            :param post_id:
                ID of the post to edit
        """
        post = Posts.get_by_id(int(post_id))

        # If user is not the author of the post
        #   We redirect to the home page
        if not self.is_the_author(post):
            self.redirect_to("home")

        form = PostForm(obj=post)
        self.render_editpost(form)

    def post(self, post_id):
        """If the form is valid, the post is updated
        and user is redirected to the post

        If user is not authorized to edit the post,
        he is redirected to homepage

        If an error occurred, form is displayed with
        details of error
        """
        post = Posts.get_by_id(int(post_id))

        # If user is not the author of the post
        #   We redirect to the home page
        if not self.is_the_author(post):
            self.redirect_to("home")

        form = PostForm(self.request.POST)

        if form.validate():
            if Posts.update_post(post, form.title.data, form.content.data):
                self.redirect_to("viewpost", post_id=post_id)
        self.render_editpost(form)

    def render_editpost(self, form):
        """Include the form in a template and render it

            :param form:
                A :class:`Form` instance.
        """
        self.render("posts/edit_post.html", form=form)

    def is_the_author(self, post):
        """ Check if user is the author of the post

            :param post:
                Post entity to edit
            :returns:
                If user is the author, we return True
                Otherwise, we return False
        """
        if post and post.user.key() == self.user.key():
            return True
        return False
