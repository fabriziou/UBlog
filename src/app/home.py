from framework.request_handler import Handler
from models.post import Post
from models.like import Like


class HomePage(Handler):
    def get(self):
        likes = {}
        posts = Post.get_all()

        for post in posts:
            likes[post.key()] = Like.get_nb_like(post)


        self.render("home/page.html", posts=posts, nb_likes=likes)
