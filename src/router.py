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
          handler='app.posts.list.ListPostsPage', name='userposts'),
    Route(r'/posts/view/<post_key:[a-zA-Z0-9-_]+>',
          handler='app.posts.view.ViewPostPage', name='viewpost'),
    Route(r'/posts/add',
          handler='app.posts.add.AddPostPage', name='addpost'),
    Route(r'/posts/edit/<post_key:[a-zA-Z0-9-_]+>',
          handler='app.posts.edit.EditPostPage', name='editpost')
], debug=True)
