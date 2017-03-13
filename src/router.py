import webapp2
from webapp2 import Route

app = webapp2.WSGIApplication([
    Route(r'/', handler='main.MainPage', name='home'),
    Route(r'/signup', handler='main.SignupPage', name='signup'),
], debug=True)
