from webapp2 import WSGIApplication
from webapp2 import Route

app = WSGIApplication([
    Route(r'/', handler='app.main.MainPage', name='home'),
    Route(r'/signup', handler='app.signup.SignupPage', name='signup'),
    Route(r'/login', handler='app.login.LoginPage', name='login'),
    Route(r'/logout', handler='app.logout.LogoutPage', name='logout'),
], debug=True)
