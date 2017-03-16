from framework.request_handler import Handler


class MainPage(Handler):
    def get(self):
        self.render("home/home.html")
