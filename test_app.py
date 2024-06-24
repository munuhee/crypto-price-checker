"""
This module contains unit tests for the CryptoAPI application.

Classes:
    TestCryptoAPI - Contains test cases for the CryptoAPI application.

Functions:
    setUp() - Sets up the test client for testing.
    test_health_check() - Tests the health check endpoint.
    test_welcome_message() - Tests the welcome message endpoint.
    test_get_crypto_price_success(mock_get) - Tests successful retrieval of crypto price.
    test_get_crypto_price_crypto_not_found(mock_get) - Tests handling of nonexistent cryptocurrency.
    test_get_crypto_price_request_exception(mock_get) - Tests handling of request exceptions.
    tearDown() - Cleans up after tests.
"""

import unittest
import json
from unittest.mock import patch, MagicMock
import requests
from app import app

class TestCryptoAPI(unittest.TestCase):
    """Test cases for the CryptoAPI application."""

    def setUp(self):
        """Set up the test client."""
        self.app = app.test_client()
        self.app.testing = True

    def test_health_check(self):
        """Test the health check endpoint."""
        response = self.app.get('/health')
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Application is healthy')

    def test_welcome_message(self):
        """Test the welcome message endpoint."""
        response = self.app.get('/')
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Welcome to the Crypto API!')

    @patch('app.requests.get')
    def test_get_crypto_price_success(self, mock_get):
        """Test successful retrieval of crypto price."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'data': {
                'id': 'bitcoin',
                'symbol': 'BTC',
                'priceUsd': '60000.00'
            }
        }
        mock_get.return_value = mock_response

        crypto_name = 'bitcoin'
        response = self.app.post('/crypto_price', json={'name': crypto_name})
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['name'], crypto_name)
        self.assertEqual(data['price'], '60000.00')

    @patch('app.requests.get')
    def test_get_crypto_price_crypto_not_found(self, mock_get):
        """Test handling of nonexistent cryptocurrency."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'data': None}
        mock_get.return_value = mock_response

        crypto_name = 'nonexistentcoin'
        response = self.app.post('/crypto_price', json={'name': crypto_name})
        data = response.get_json()

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['error'], 'Crypto name not found')

    @patch('app.requests.get', side_effect=requests.exceptions.RequestException('Connection error'))
    def test_get_crypto_price_request_exception(self, mock_get):
        """Test handling of request exceptions."""
        crypto_name = 'bitcoin'
        response = self.app.post('/crypto_price', json={'name': crypto_name})
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 400)
        self.assertIn('Error fetching cryptocurrency data', data['error'])

if __name__ == '__main__':
    unittest.main()
