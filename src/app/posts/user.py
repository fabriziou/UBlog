from app.posts.postpage import PostPage
from lib.pagination import Pagination
from models.user import User
from models.post import Post
from models.like import Like
from models.comment import Comment


class UserPosts(PostPage):

    def get(self, user_key):
        """ Get all posts of a given user

            :param user_key:
                Key of the user we want to get all posts
        """
        user = User.get(user_key)
        posts = Post.get_all(user=user)
        pagination = Pagination(self.request.GET.get('p'), posts.count())

        if pagination and pagination.is_valid():
            posts = posts.fetch(limit=pagination.posts_per_page,
                                offset=pagination.offset)

            nb_likes = Like.get_nb_likes_per_posts(posts)
            nb_comments = Comment.get_nb_comments_per_posts(posts)

            self.render("posts/user.html", userposts=user, posts=posts,
                        nb_likes=nb_likes, nb_comments=nb_comments,
                        pagination=pagination)
        else:
            self.abort(404, "Invalid page number")
