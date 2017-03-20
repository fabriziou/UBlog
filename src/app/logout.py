from framework.request_handler import Handler


class LogoutPage(Handler):
    @Handler.login_required(True)
    def get(self):
        """Create an empty cookie and redirect to home page
        """
        self.response.headers.add_header("Set-Cookie", "uid=;")
        self.redirect_to("home")
