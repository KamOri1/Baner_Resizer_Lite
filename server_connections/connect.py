from abc import ABC, abstractmethod


class SignUp(ABC):
    @abstractmethod
    def log_in(self, login_data):
        ...

    @abstractmethod
    def missing_data(self):
        ...