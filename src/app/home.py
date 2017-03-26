from lib.request_handler import Handler
from models.post import Post
from models.like import Like
from models.comment import Comment
from models.pagination import Pagination


class HomePage(Handler):
    def get(self):
        posts = Post.get_all()
        pagination = Pagination(self.request.GET.get('p'), posts.count())

        if pagination.is_valid():
            posts = posts.fetch(limit=pagination.posts_per_page,
                                offset=pagination.offset)

            nb_likes = Like.get_likes_per_posts(posts)
            nb_comments = Comment.get_comments_per_posts(posts)

            self.render("home/page.html", posts=posts, nb_likes=nb_likes,
                        nb_comments=nb_comments, pagination=pagination)
        else:
            self.abort(404, "Invalid page number")
