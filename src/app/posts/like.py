from framework.request_handler import Handler
from app.posts.postpage import PostPage
from models.post import Post
from models.like import Like


class LikePost(PostPage):

    @Handler.login_required(True)
    @PostPage.is_post_valid
    def get(self, post_key):
        """ Like a post
        """
        if self.post.parent().key is not self.user.key():
            like_key = Like.get_like_by_user(self.user, self.post)

            if not like_key:
                success = Like.new_like(self.user, self.post)
            else:
                success = Like.delete_like(like_key)

            if success:
                self.redirect_to("viewpost", post_key=post_key)
            else:
                abort(404)

        else:
            abort(404, "You can't like your own post")
