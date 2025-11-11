from .connect import SignUp


class FtpSignUp(SignUp):
    def log_in(self, login_data):
        ...

    def missing_data(self):
        ...