# api endpoint tests
# path ../tests/book_api_tests.py

# import os and python unittest modules
<<<<<<< HEAD

=======
#import sys
>>>>>>> api_endpoints
import unittest

# import json
import json

<<<<<<< HEAD
from app import create_app
=======
#sys.path.append('..')
from Hello_Books_Api.app import create_app
>>>>>>> api_endpoints




class HellobooksCRUDTestCase(unittest.TestCase):
    '''This class represents the Hello_Books_Api CRUD Testcase'''

    def setUp(self):

        '''Define test variables and initialize app.'''
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
<<<<<<< HEAD

=======
        self.client = self.app.test_client()
>>>>>>> api_endpoints
        # book(dict) variable
        self.book_details = {
            'id': 4,
            'title':'Eloquent Javascript',
            'edition': 'Second',
            'description': 'a javascript book',
            'author': 'Marijn Haverbeke',
            'category':'Javascript',
            'copies': 20

        }

        #intialize the test client
<<<<<<< HEAD
        self.client = self.app.test_client
=======

>>>>>>> api_endpoints

    def tearDown(self):
        self.app_context.pop()


    def test_book_info_can_be_modified(self):
        '''test whether book info can be updated'''

        result_post=self.client.post('/app/books/', data = self.book_details)
        self.assertEqual(result_post.status_code, 201)
        new_book_detail = self.book_details['description'] = "A modern introduction to programming"
        result_put = self.client.put('/app/books/4', data = new_book_detail)
<<<<<<< HEAD
        self.assertEqual(response_put.status_code, 200)
=======
        self.assertEqual(result_put.status_code, 200)
>>>>>>> api_endpoints
        result_get = self.client.get('/app/books/4')
        self.assertIn('A modern introduction to programming',str(result_get.data))

    def test_api_can_remove_book(self):
        '''test api can delete a book'''

        result_post = self.client.post('/app/books/', data=self.book_details)
        self.assertEqual(result_post.status_code, 201)
        result_delete = self.client.delete('app/books/4')
        self.assertEqual(result_delete.status_code, 200)
        result = self.client.get('/app/books/4')
<<<<<<< HEAD
      	self.assertEqual(result.status_code, 404)
=======
        self.assertEqual(result.status_code, 404)
>>>>>>> api_endpoints

    def test_get_book_by_id(self):
        '''test api can get a single book by its id '''

        result = self.client.post('/app/books/', data = self.book_details)
        self.assertEqual(result.status_code, 201)
        json_result= json.loads(result.data.decode('utf-8'))

<<<<<<< HEAD
        result_get = self.client.get(
                        '/app/books/{}'.format(json_result['id']
                         ))
=======
        result_get = self.client.get('/app/books/{}'.format(json_result['id']))
>>>>>>> api_endpoints
        self.assertEqual(result_get.status_code, 200)
        self.assertIn('Eloquent Javascript', result_get.data)

    def test_api_can_add_book(self):
        '''test api can borrow book'''

        result = self.client.post('/app/books/', data = self.book_details)
<<<<<<< HEAD
        self.assertEqual(response.status_code, 201)
        self.assertIn('Marijn Haverbeke', str(result.data)


    def test_api_can_remove_book(self):
        '''test api can delete a book'''

        result_post = self.client.post('/app/books/', data = self.book_details)
        self.assertEqual(result_post.status_code, 201)
        result_delete = self.client.delete('app/books/4')
        self.assertEqual(result_delete.status_code, 200)
        result = self.client.get('/app/books/4')
      	self.assertEqual(result.status_code, 404)
=======
        self.assertEqual(result.status_code, 201)
        self.assertIn('Marijn Haverbeke', str(result.data))
>>>>>>> api_endpoints


    def test_api_can_get_all_books(self):
        '''test api can get all books'''

        result_post = self.client.post('/app/books/', data = self.book_details)
        self.assertEqual(result_post.status_code, 201)
        result_get = self.client.get('/app/books/')
        self.assertEqual(result_get.status_code, 200)
<<<<<<< HEAD
        self.assertIn('Eloquent Javascript', str(result_get)


=======
        self.assertIn('Eloquent Javascript', str(result_get))
>>>>>>> api_endpoints


if __name__ == "__main__":
    unittest.main()
