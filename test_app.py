import unittest
import json
from flask_testing import TestCase
from app import app

class CryptoAPITestCase(TestCase):
    """
    Test cases for the Crypto API.
    """

    def create_app(self):
        """
        Create a Flask app for testing purposes.
        """
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        return app

    def test_welcome_message(self):
        """
        Test the welcome message at the root endpoint.
        """
        response = self.client.get('/')
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, {'message': 'Welcome to the Crypto API!'})

    def test_get_crypto_price_valid(self):
        """
        Test getting the price of a valid cryptocurrency.
        """
        crypto_name = "Bitcoin"
        response = self.client.post('/crypto_price', json={'name': crypto_name})
        print("Response Status Code:", response.status_code)
        print("Response Data:", response.data.decode('utf-8'))
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['name'], crypto_name)


    def test_get_crypto_price_invalid(self):
        """
        Test getting the price of an invalid cryptocurrency.
        """
        crypto_name = 'InvalidCrypto'
        response = self.client.post('/crypto_price', json={'name': crypto_name})
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['error'], 'Crypto name not found')

    def test_get_crypto_price_no_name(self):
        """
        Test getting the price without providing a crypto name.
        """
        response = self.client.post('/crypto_price', json={})
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'Please provide a crypto name')

    def test_failed_to_fetch_crypto_data(self):
        """
        Test when there's no matching crypto name.
        """
        crypto_name = 'NonExistentCrypto'
        response = self.client.post('/crypto_price', json={'name': crypto_name})
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['error'], 'Crypto name not found')

if __name__ == '__main__':
    unittest.main()