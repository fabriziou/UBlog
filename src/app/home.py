from framework.request_handler import Handler
from models.post import Post
from models.like import Like
from models.pagination import Pagination


class HomePage(Handler):
    def get(self):
        page_id = None
        if (self.request.GET.get('p') and
             self.request.GET.get('p').isdigit()):
            page_id = int(self.request.GET.get('p'))

        posts = Post.get_all()

        total_posts = 0
        if posts:
            total_posts = posts.count()

        pagination = Pagination(page_id, total_posts)
        if not pagination.validate():
            self.errors.append("Invalid page number")
            self.abort(404)

        posts = posts.fetch(limit=pagination.posts_per_page,
                             offset=pagination.offset)

        likes = Like.get_likes_per_posts(posts)

        self.render("home/page.html", posts=posts, nb_likes=likes,
                    pagination=pagination)
