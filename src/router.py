from webapp2 import WSGIApplication
from webapp2 import Route

app = WSGIApplication([
    Route(r'/', handler='app.main.MainPage', name='home'),
    Route(r'/signup', handler='app.main.SignupPage', name='signup'),
], debug=True)
