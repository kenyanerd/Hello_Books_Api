# api endpoint tests
# path ../tests/book_api_tests.py

# import os and python unitest modules

import os
import unittest

# import json
import json

from app import create_app


class HellobooksCRUDTestCase(unittest.TestCase):
    '''This class represents the Hello_Books_Api Testcase'''

    def setup(self):
        '''Define test variables and initialize app.'''
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()

        # book(dict) variable
        self.book_details = {
            'id': 4,
            'title':'Eloquent Javascript',
            'edition': 'Second',
            'description': '',
            'author': 'Marijn Haverbeke',
            'category':'Javascript',
            'copies': 20

        }

    # executed after each test
    def tearDown(self):
        self.app_context.pop()


    def test_book_info_can_be_modified(self):
        '''test whether book info can be updated'''
        result_post=self.client.post('/api/books/', data = self.book_details)
        self.assertEqual(result_post.status_code, 201)
        new_book_detail = self.book_details['description'] = "A modern introduction to programming"
        result_put = self.client.put('/api/books/4', data = new_book_detail)

    def test_api_can_add_book(self):
        '''test api can borrow book'''
        result = self.client.post('/api/books/', data=self.book_details)
        self.assertEqual(response.status_code, 201)
        self.assertIn('Marijn Haverbeke', str(result.data)


    def test_api_can_remove_book(self):
        '''test api can delete a book'''
        result_post = self.client.post('/api/books/', data=self.book_details)
        self.assertEqual(result_post.status_code, 201)
        result_delete = self.client.delete('api/books/4')
        self.assertEqual(result_delete.status_code, 200)
        result = self.client.get('/api/books/4')
      	self.assertEqual(result.status_code, 404)



    def test_api_can_get_all_books(self):
        '''test api can get all books'''
        result_post = self.client.post('/api/books/', data=self.book_details)
        self.assertEqual(result_post.status_code, 201)
        result_get = self.client.get('/api/books/')
        self.assertEqual(result_get.status_code, 200)
        self.assertIn('Eloquent Javascript', str(result_get)



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
