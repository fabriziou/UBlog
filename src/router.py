from webapp2 import WSGIApplication
from webapp2 import Route

app = WSGIApplication([
    # Home
    Route(r'/',
          handler='app.home.HomePage', name='home'),
    Route(r'/register',
          handler='app.registration.RegistrationPage', name='signup'),
    Route(r'/login',
          handler='app.login.LoginPage', name='login'),
    Route(r'/logout',
          handler='app.logout.LogoutPage', name='logout'),

    # /posts
    Route(r'/posts',
          handler='app.posts.list.ListPosts', name='userposts'),
    Route(r'/posts/view/<post_key:[a-zA-Z0-9-_]+>',
          handler='app.posts.view.ViewPost', name='viewpost'),
    Route(r'/posts/add',
          handler='app.posts.add.AddPost', name='addpost'),
    Route(r'/posts/edit/<post_key:[a-zA-Z0-9-_]+>',
          handler='app.posts.edit.EditPost', name='editpost'),
  Route(r'/posts/like/<post_key:[a-zA-Z0-9-_]+>',
        handler='app.posts.like.LikePost', name='likepost'),

    # /comments
    Route(r'/posts/<post_key:[a-zA-Z0-9-_]+>/comments/edit/<comment_key:[a-zA-Z0-9-_]+>',
          handler='app.comments.edit.EditCommentPage', name='editcomment')
], debug=True)
