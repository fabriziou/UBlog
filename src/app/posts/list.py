from lib.request_handler import Handler
from app.posts.postpage import PostPage
from models.post import Post
from models.like import Like
from models.comment import Comment
from models.pagination import Pagination


class ListPosts(PostPage):

    @Handler.login_required(True)
    def get(self):
        page_id = None
        if (self.request.GET.get('p') and
             self.request.GET.get('p').isdigit()):
            page_id = int(self.request.GET.get('p'))

        posts = Post.get_all(user=self.user)

        pagination = Pagination(page_id, total_posts=posts.count())

        posts = posts.fetch(limit=pagination.posts_per_page,
                             offset=pagination.offset)

        nb_likes = Like.get_likes_per_posts(posts)
        nb_comments = Comment.get_comments_per_posts(posts)

        self.render("posts/list.html", posts=posts, nb_likes=nb_likes,
                    nb_comments=nb_comments, pagination=pagination)
