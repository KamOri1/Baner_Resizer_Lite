from .connect import SignUp


class SftpSignUp(SignUp):
    def log_in(self, login_data):
        ...

    def missing_data(self):
        ...