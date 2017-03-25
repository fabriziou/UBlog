from lib.request_handler import Handler
from lib.cookie_handler import create_cookie
from forms.registration import RegistrationForm
from models.user import User


class RegistrationPage(Handler):
    @Handler.login_required(False)
    def get(self):
        """ Display the form to register
        """
        form = RegistrationForm()
        self.render_signup(form)

    @Handler.login_required(False)
    def post(self):
        """ Create new user and redirect user to home page

        If error,
            display form with errors details
        """
        form = RegistrationForm(self.request.POST)

        if form.validate():
            user_key = User.new_user(form.email.data, form.username.data,
                                     form.password.data)
            if user_key:
                cookie = create_cookie("uid", user_key)
                self.response.headers.add_header("Set-Cookie", cookie)
                self.redirect_to("home")
            else:
                self.abort(500)

        self.render_signup(form)

    def render_signup(self, form):
        """ Include all datas in a template
            and render the page
        """
        self.render("signup/page.html", form=form)
