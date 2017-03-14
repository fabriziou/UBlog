import os
from jinja2 import Environment, FileSystemLoader
from webapp2 import RequestHandler


class Handler(RequestHandler):
    template_dir = os.path.join(
        os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)),
        'templates')
    jinja_env = Environment(loader=FileSystemLoader(template_dir),
                            autoescape=True)

    def render(self, template, **kw):
        jinja_template = self.jinja_env.get_template(template)
        html_from_template = jinja_template.render(kw)
        self.response.out.write(html_from_template)
