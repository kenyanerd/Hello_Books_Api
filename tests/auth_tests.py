import unittest

import json

from app import create_app

class UserAuthTestCase(Unittest.TestCase):
    '''User Authentication TestCase'''

    def setUp(self):
        """Set up test variables. """

        self.app = create_app("testing")

        '''initialize the test client'''
        self.client = self.app.test_client

        '''This is the user test json data with a predefined email and password'''
        self.user_data = {
            'email': 'user@testmail.com',
            'password': 'pass123*'

        }

    def test_user_registration(self):
        '''test user registration works correctly'''


        res = self.client.post('/auth/register', data=self.user_data)

        '''get the results returned in json format'''
        result = json.loads(res.data.decode()

        '''assert that the request contains a success message and a 201 status code'''
        self.assertEqual(result['message'], "Registration successful.")
        self.assertEqual(res.status_code, 201)

    def test_already_registered_user(self):
        """Test that a user cannot be registered twice."""

        res = self.client.post('/auth/register', data=self.user_data)
        self.assertEqual(res.status_code, 201)
        second_res = self.client.post('/auth/register', data=self.user_data)
        self.assertEqual(second_res.status_code, 202)
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

    	self.test_user_login
	    res = self.client.get('/auth/logout', data =self.user_data)
        self.assertIn(b'you logged out', res.data)


    def test_user_password_reset(self):
    """test app if app can allow user to reset their password """

        self.test_user_login()
        reset_result=self.client.post('/auth/password_reset', data={
            'email': 'user@testmail.com,
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
