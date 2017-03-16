from framework.handler import Handler
from forms.registration import RegistrationForm
from models.Users import Users


class SignupPage(Handler):
    def get(self):
        """Generate an empty form and render it
        """
        form = RegistrationForm()
        self.render_signup(form)

    def post(self):
        """Validates the form

        If the form is valid, a new user is created
        and redirected to the main page.

        If an error occurred, the form is displayed with
        details of error
        """
        # Populate the form with user inputs
        form = RegistrationForm(self.request.POST)

        if form.validate():
            # TODO :
            # Format datas, username.lower(), email.lower(), crypt password
            user = Users(username=form.username.data,
                         email=form.email.data,
                         password=form.password.data)
            if user.put():
                self.redirect("/")
        else:
            self.render_signup(form)

    def render_signup(self, form):
        """Include the form in a template and render it

            :param form:
                A :class:`Form` instance.
        """
        self.render("signup/signup.html", form=form)
