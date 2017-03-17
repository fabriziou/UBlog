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

        self.errors = {}
        # Retrieve user by his cookie
        self.user = Users.get_by_cookie(self.request.cookies.get("uid"))

    def render(self, template, **kw):
        """Render the HTML page

            :param template:
                HTML file to render
        """
        jinja_template = self.jinja_env.get_template(template)
        html_from_template = jinja_template.render(kw, errors=self.errors,
                                                   user=self.user)
        self.response.out.write(html_from_template)

    @staticmethod
    def login_required(is_required=True):
        """ If login is required and user isn't connected:
                User is redirect to login page
            If login isn't required and user is connected:
                User is redirect to home page
            Otherwise, process continue
        """
        def func_login_required(func):
            def check_requirements(self):
                # If user IS authenticated and login IS NOT required
                #   User is redirected to HOME page
                if self.user and not is_required:
                    self.redirect(self.uri_for("home"))
                # If user IS NOT authenticated and login IS required
                #   User is redirected to LOGIN page
                elif not self.user and is_required:
                    self.redirect(self.uri_for("login"))
                # Requirements are met, process can go on
                return func(self)
            return check_requirements
        return func_login_required
