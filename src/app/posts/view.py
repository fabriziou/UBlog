from framework.request_handler import Handler
from models.post import Post


class ViewPostPage(Handler):
    def get(self, post_key):
        """ Get post :param post_key: and render it

            :param post_key:
                Key of the post
        """
        post = Post.get(post_key)
        self.render("posts/view.html", post=post)
