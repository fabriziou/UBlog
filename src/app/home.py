from framework.request_handler import Handler
from models.post import Post
from models.like import Like
from models.pagination import Pagination


class HomePage(Handler):
    def get(self, page_id=1):

        pagination = Pagination(page_id)
        posts = Post.get_all(limit=pagination.posts_per_page,
                             offset=pagination.offset)
        likes = Like.get_likes_per_posts(posts)

        self.render("home/page.html", posts=posts, nb_likes=likes,
                    pagination=pagination)
