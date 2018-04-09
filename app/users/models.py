from werkzeug.security import check_password_hash, generate_password_hash
import datetime

# import a the Book Model
from app.books.models  import Book

# create a list of users
users = []

class User:
    '''a model class for  a User'''

    def __init__(self):
        self.id = None
        self.name = None
        self.email = None
        self.password = None
        self.admin = False
        self.books_borrowed = []

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def save(self):
        users.append(self)

    # method to get all users in the list
    @staticmethod
    def get_user_by_mail(email):
        for user in users:
            if user.email == email:
                return user



