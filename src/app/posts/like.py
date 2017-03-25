from lib.request_handler import Handler
from app.posts.postpage import PostPage
from models.post import Post
from models.like import Like


class LikePost(PostPage):

    @Handler.login_required(True)
    @PostPage.is_post_valid
    def get(self, post_key):
        """ Like/Unlike a post

            An error is thrown if user likes his own post
        """
        if self.post.parent().key() != self.user.key():
            like_key = Like.is_liked_by_user(self.user, self.post)

            if not like_key:
                success = Like.new_like(self.user, self.post)
            else:
                success = Like.delete_like(like_key)

            if success:
                self.redirect_to("viewpost", post_key=post_key, _fragment="liked")
            else:
                self.abort(404)

        else:
            self.errors.append("You can't like your own post")
            self.abort(404)
