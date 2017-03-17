import os
from jinja2 import Environment, FileSystemLoader
from webapp2 import RequestHandler
from models.Users import Users


class Handler(RequestHandler):
    template_dir = os.path.join(
        os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)),
        'templates')
    # autoescape = True
    jinja_env = Environment(loader=FileSystemLoader(template_dir),
                            autoescape=True)

    def __init__(self, request=None, response=None):
        RequestHandler.__init__(self, request, response)
        # Retrieve user by his cookie
        self.user = Users.get_by_cookie(self.request.cookies.get("uid"))

    def render(self, template, **kw):
        """Render the HTML page

            :param template:
                HTML file to render
        """
        jinja_template = self.jinja_env.get_template(template)
        html_from_template = jinja_template.render(kw, user=self.user)
        self.response.out.write(html_from_template)

    @staticmethod
    def login_required(func):
        """ Redirect user to login page if he is not connected
            If logged in, we save an instance of Users
        """
        def redirect_visitor(self):
            if not self.user:
                self.redirect(self.uri_for("login"))
            else:
                return func(self)
        return redirect_visitor

    @staticmethod
    def logout_required(func):
        """ Redirect user to home page if he is connected
        """
        def redirect_logged_user(self):
            if self.user:
                self.redirect(self.uri_for("home"))
            else:
                return func(self)
        return redirect_logged_user
