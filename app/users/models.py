from werkzeug.security import check_password_hash, generate_password_hash
import datetime

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

