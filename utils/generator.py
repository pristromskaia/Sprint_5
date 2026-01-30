import random


class UserDataGenerator:
    @staticmethod
    def random_email():
        return f"EMAIL{random.randint(100, 999)}@gmail.com"

    @staticmethod
    def random_password():
        return f"PASSWORD{random.randint(100, 999)}"

    @staticmethod
    def invalid_email():
        return f"EMAIL{random.randint(100, 999)}yandex.ru"
