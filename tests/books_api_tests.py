# api endpoint tests
# path ../tests/book_api_tests.py

# import os and python unitest modules

import os
import unittest

# import json
import json

from app import create_app


class HellobooksapiTestCase(unittest.TestCase):
    '''This class represents the Hello_Books_Api Testcase'''

    def setup(self):
        '''Define test variables and initialize app.'''


    def test_api_can_add_book(self):
        '''test api can borrow book'''
        pass

    def test_book_info_can_be_modified(self):
        '''test whether book info can be updated'''
        pass

    def test_api_can_remove_book(self):
        '''test api can delete a book'''
        pass


    def test_api_can_get_all_books(self):
        '''test api can get all books'''
        pass

    def test_get_book_by_id(self, parameter_list):
        '''test api can get a single book by its id '''
        pass

    def user_can_borrow_book_test(self, parameter_list):
        '''test a user can borrow  a book-POST request'''
        pass

    def test_user_registration(self, parameter_list):
        '''test user registration works correctly'''
        pass

    def test_user_login(self, parameter_list):
        '''test user can login successfully'''
        pass

    def test_user_logout(self, parameter_list):
        '''test users can logout successfully'''
        pass

    def test_reset_password(self, parameter_list):
        '''test password reset works correctly'''
        pass


if __name__ == "__main__":
    unittest.main()
