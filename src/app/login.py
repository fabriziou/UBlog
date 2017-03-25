from lib.request_handler import Handler
from lib.cookie_handler import create_cookie
from wtforms.validators import ValidationError
from forms.login import LoginForm
from models.user import User


class LoginPage(Handler):
    @Handler.login_required(False)
    def get(self):
        """ Display the form to login
        """
        form = LoginForm()

        self.render_login(form)

    @Handler.login_required(False)
    def post(self):
        """ Connect user and redirect user to home page

        If credentials are valid,
            a cookie is created to keep the user logged

        If error,
            display form with errors details
        """
        form = LoginForm(self.request.POST)
        errors = []

        if form.validate():
            user_key = self.valid_login_credentials(form.email.data,
                                                    form.password.data)

            if user_key:
                # Create an auth cookie
                cookie = create_cookie("uid", user_key)
                self.response.headers.add_header("Set-Cookie", cookie)
                self.redirect_to("home")
            else:
                errors.append("""Sorry, the <b>email</b> and <b>password</b>
                              you entered do not match. Please try again.""")

        self.render_login(form, errors)

    def valid_login_credentials(self, email, password):
        """Validate if email and password belongs to an account

            :param email:
                Email of the user
            :param password:
                Password of the user
            :returns:
                If credentials are valid, the user key is returned
                Otherwise, we return False
        """
        user = User.get_by_email(email)

        if user:
            salt = user.password[:88]
            password_hashed = User.crypt_password(password, salt)

            if password_hashed == user.password:
                return user.key()

        return False

    def render_login(self, form, errors=None):
        """ Include all datas in a template
            and render the page
        """
        self.render("login/page.html", form=form, errors=errors)
