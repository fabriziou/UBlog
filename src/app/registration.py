from framework.request_handler import Handler
from framework.cookie_handler import create_cookie
from forms.registration import RegistrationForm
from models.user import User


class RegistrationPage(Handler):
    @Handler.login_required(False)
    def get(self):
        """Generate an empty form and render it
        """
        form = RegistrationForm()
        self.render_signup(form)

    @Handler.login_required(False)
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
            user_key = User.new_user(form.email.data, form.username.data,
                                     form.password.data)
            if user_key:
                # Cookie creation and redirection
                self.response.headers.add_header("Set-Cookie",
                                                 create_cookie("uid",
                                                               user_key))
                self.redirect_to("home")
        self.render_signup(form)

    def render_signup(self, form):
        """Include the form in a template and render it

            :param form:
                A :class:`Form` instance.
        """
        self.render("signup/page.html", form=form)
