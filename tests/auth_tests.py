import unittest
<<<<<<< HEAD

import json

from app import create_app

class UserAuthTestCase(Unittest.TestCase):
=======
#import sys

import json

#sys.path.append('..')
from Hello_Books_Api.app import create_app

class UserAuthTestCase(unittest.TestCase):
>>>>>>> api_endpoints
    '''User Authentication TestCase'''

    def setUp(self):
        """Set up test variables. """

<<<<<<< HEAD
        self.app = create_app("testing")

        '''initialize the test client'''
        self.client = self.app.test_client
=======
        self.app = create_app()

        '''initialize the test client'''
        self.client = self.app.test_client()
>>>>>>> api_endpoints

        '''This is the user test json data with a predefined email and password'''
        self.user_data = {
            'email': 'user@testmail.com',
            'password': 'pass123*'

        }
<<<<<<< HEAD
        def tearDown(self):
            self.app_context.pop()

    def test_user_registration(self):
        '''test user registration works correctly'''


        res = self.client.post('/auth/register', data=self.user_data)

        '''get the results returned in json format'''
        result = json.loads(res.data.decode()
=======

    def test_user_registration(self):
        '''test user registration works correctly'''
        res = self.client.post('/auth/register', data=self.user_data)

        '''get the results returned in json format'''
        result = json.loads(res.data.decode())
>>>>>>> api_endpoints

        '''assert that the request contains a success message and a 201 status code'''
        self.assertEqual(result['message'], "Registration successful.")
        self.assertEqual(res.status_code, 201)

    def test_already_registered_user(self):
        """Test that a user cannot be registered twice."""

        res = self.client.post('/auth/register', data=self.user_data)
        self.assertEqual(res.status_code, 201)
        second_res = self.client.post('/auth/register', data=self.user_data)
<<<<<<< HEAD
        self.assertEqual(second_res.status_code, 202)
=======
        self.assertEqual(second_res.status_code, 409)
>>>>>>> api_endpoints
        result = json.loads(second_res.data.decode())
        self.assertEqual(result['message'], "This  account already  Exists. Please login.")


    def test_user_login(self):
        '''test user can login successfully'''

        res = self.client.post('/auth/register', data=self.user_data)
        self.assertEqual(res.status_code, 201)
        login_res = self.client.post('/auth/login', data=self.user_data)
        result = json.loads(login_res.data.decode())
        self.assertEqual(result['message'], "You logged in successfully.")
        self.assertEqual(login_res.status_code, 200)
        self.assertTrue(result['access_token'])


    def test_user_logout(self):
        ''' test if a user can log-out'''
<<<<<<< HEAD

    	self.test_user_login
	    res = self.client.get('/auth/logout', data =self.user_data)
=======
        self.test_user_login()
        res = self.client.get('/auth/logout', data =self.user_data)
>>>>>>> api_endpoints
        self.assertIn(b'you logged out', res.data)


    def test_user_password_reset(self):
<<<<<<< HEAD
    """test app if app can allow user to reset their password """

        self.test_user_login()
        reset_result=self.client.post('/auth/password_reset', data = {
            'email': 'user@testmail.com,
=======
        """test app if app can allow user to reset their password """
        self.test_user_login()
        res =self.client.post('/auth/password_reset', data = {
            'email': 'user@testmail.com',
>>>>>>> api_endpoints
            'old_password': 'pass123*',
            'new_password': 'PAss123*'
         })
        login_result=self.client.post('/auth/login', data={
            'email': 'user@testmail.com',
            'password': 'PAss123*'
        })
        self.assertEqual(login_result.status_code, 200)


if __name__ == "__main__":
    unittest.main()
