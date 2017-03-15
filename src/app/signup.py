from framework.handler import Handler
from models.Users import Users


class SignupPage(Handler):
    def render_signup(self, datas={}, errors={}):
        self.render("signup/signup.html", datas=datas, errors=errors)

    def get(self):
        self.render_signup()

    def post(self):
        errors = {}
        datas = {}

        # Get datas
        datas["email"] = self.request.get("email")
        datas["username"] = self.request.get("username")
        datas["password"] = self.request.get("password")
        datas["verify"] = self.request.get("verify")

        # Check valid datas
        Users.is_email_valid(datas["email"], errors)
        Users.is_username_valid(datas["username"], errors)
        Users.is_password_valid(datas["password"], errors)

        if errors:
            print errors
            self.render_signup(datas=datas, errors=errors)
        else:
            self.redirect("/")

    def valid_passwords(self, password1, password2, error=None):
        """ Check if two passwords are valid and identical.

            A valid password is not empty

            :param password1:
                Password to check
            :param password2:
                Password to check
            :param error:
                If error, error["password"] will be set with an error message
            :returns:
                If passwords are valid and identical, we return True
                Otherwise, we return False
        """

        if password1:
            if password2 and password1 == password2:
                return True
            error["password"] = "Passwords don't match"
        else:
            error["password"] = "Password must not be empty"
        return False
