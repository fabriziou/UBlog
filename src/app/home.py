from framework.request_handler import Handler
from models.post import Post
from models.like import Like
from math import ceil



class HomePage(Handler):
    def get(self, page_id=None):
        if not page_id:
            page_id = 1
        page_id = int(page_id)
        nb_posts_page = 4
        nb_total_posts = Post.get_nb_posts()

        offset = (page_id*nb_posts_page)-nb_posts_page
        print offset
        posts = Post.get_all(limit=nb_posts_page, offset=offset)

        likes = {}
        for post in posts:
            likes[post.key()] = Like.get_nb_like(post)


        pages = int(ceil(float(nb_total_posts) / float(nb_posts_page)))



        self.render("home/page.html", posts=posts, nb_likes=likes)
