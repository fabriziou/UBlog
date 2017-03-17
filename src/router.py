from webapp2 import WSGIApplication
from webapp2 import Route

app = WSGIApplication([
    # Home
    Route(r'/', handler='app.main.MainPage', name='home'),

    # Logout pages
    Route(r'/signup', handler='app.signup.SignupPage', name='signup'),
    Route(r'/login', handler='app.login.LoginPage', name='login'),

    # Login pages
    Route(r'/logout', handler='app.logout.LogoutPage', name='logout'),
    Route(r'/posts/add', handler='app.posts.AddPostPage', name='addpost'),
], debug=True)
