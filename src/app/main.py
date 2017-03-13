from framework.handler import Handler

class MainPage(Handler):
    def get(self):
        self.render("index.html")

class SignupPage(Handler):
    def get(self):
        self.render("signup.html")
