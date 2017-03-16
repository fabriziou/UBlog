from framework.handler import Handler
from forms.login import LoginForm
from models.Users import Users


class LoginPage(Handler):
    def get(self):
        """Generate an empty form and render it
        """
        form = LoginForm()
        self.render_login(form)

    def post(self):
        """Validates the form

        If the form is valid, the user is logged

        If an error occurred, the form is displayed with
        details of error
        """
        # Populate the form with user inputs
        form = LoginForm(self.request.POST)

        if form.validate():
            self.redirect("/")
        self.render_login(form)

    def render_login(self, form):
        """Include the form in a template and render it

            :param form:
                A :class:`Form` instance.
        """
        self.render("login/login.html", form=form)
