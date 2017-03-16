import os
from jinja2 import Environment, FileSystemLoader
from webapp2 import RequestHandler
from framework.cookie_handler import read_cookie


class Handler(RequestHandler):
    template_dir = os.path.join(
        os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)),
        'templates')
    # autoescape = True
    jinja_env = Environment(loader=FileSystemLoader(template_dir),
                            autoescape=True)

    def render(self, template, **kw):
        """Render the HTML page

            :param template:
                HTML file to render
        """
        jinja_template = self.jinja_env.get_template(template)
        html_from_template = jinja_template.render(kw)
        self.response.out.write(html_from_template)

    def user_is_logged(self):
        """Check if user is logged in
        """
        auth_cookie = self.request.cookies.get("uid")
        if auth_cookie:
            return read_cookie(auth_cookie)
        return None
