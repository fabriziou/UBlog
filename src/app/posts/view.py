from framework.request_handler import Handler
from models.post import Post
from models.comment import Comment


class ViewPostPage(Handler):
    def get(self, post_key):
        """ Get post :param post_key: and render it

            :param post_key:
                Key of the post
        """
        post = Post.get(post_key)
        comments = Comment.get_all_by_post(post)
        print comments
        self.render("posts/view.html", post=post)
