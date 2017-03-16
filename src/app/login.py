from framework.handler import Handler
from wtforms.validators import ValidationError
from forms.login import LoginForm
from models.Users import Users


class LoginPage(Handler):
    errors = {}

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
            if self.valid_login_credentials(form.email.data,
                                            form.password.data):
                self.redirect("/")

        self.render_login(form)

    def valid_login_credentials(self, email, password):
        """Check if (username, password) match with a User in the Datastore

            :param email:
                Email of the user
            :param password:
                Password of the user
            :returns:
                If a user is found, we return True
                Otherwise, we return False
        """
        user = Users.get_by_email(email)
        if user:
            # Get salt from user.password
            salt = user.password[:88]
            # Hash password with the same salt than user
            password_hashed = Users.crypt_password(password,
                                                   salt)
            if password_hashed == user.password:
                return True
            else:
                self.errors["IncorrectPassword"] = "Password doesn't match"
        else:
            self.errors["EmailNotFound"] = "No user found with this email"
        return False

    def render_login(self, form):
        """Include the form in a template and render it

            :param form:
                A :class:`Form` instance.
        """
        self.render("login/login.html", form=form, errors=self.errors)