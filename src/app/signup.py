from framework.request_handler import Handler
from forms.registration import RegistrationForm
from models.Users import Users


class SignupPage(Handler):
    @Handler.logout_required
    def get(self):
        """Generate an empty form and render it
        """
        form = RegistrationForm()
        self.render_signup(form)

    @Handler.logout_required
    def post(self):
        """Validate the form

        If the form is valid, a new user is created
        and redirected to the main page.

        If an error occurred, the form is displayed with
        details of error
        """
        # Populate the form with user inputs
        form = RegistrationForm(self.request.POST)

        if form.validate():
            # Format datas, crypt password
            username = form.username.data.title()
            email = form.email.data.lower()
            password = Users.crypt_password(form.password.data)

            user = Users(username=username,
                         email=email,
                         password=password)
            if user.put():
                self.redirect("/")
        self.render_signup(form)

    def render_signup(self, form):
        """Include the form in a template and render it

            :param form:
                A :class:`Form` instance.
        """
        self.render("signup/signup.html", form=form)
