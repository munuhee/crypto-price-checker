"""
Crypto API Flask App

This Flask app provides cryptocurrency price information.
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

BASE_URL = 'https://api.coincap.io/v2/assets'

@app.route('/health')
def health_check():
    """
    This route returns a 200 OK response if your application is healthy.
    """
    return jsonify({'message': 'Application is healthy'}), 200

@app.route('/')
def get_crypto():
    """
    Returns a welcome message for the Crypto API.
    """
    return jsonify({'message': 'Welcome to the Crypto API!'})

@app.route('/crypto_price', methods=['POST', 'GET'])
def get_crypto_price():
    """
    Get the price of a cryptocurrency by name.
    """
    crypto_name = request.json.get('name')

    if not crypto_name:
        return jsonify({'error': 'Please provide a crypto name'}), 400

    try:
        # Construct the URL to fetch the cryptocurrency data
        url = f'{BASE_URL}/{crypto_name.lower()}'
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            coin_data = response.json()
            if 'data' in coin_data:
                price = coin_data['data'].get('priceUsd', 0)
                return jsonify({'name': crypto_name, 'price': price})
            else:
                return jsonify({'error': 'Crypto name not found'}), 404
        else:
            return jsonify({'error': 'Failed to fetch cryptocurrency data'}), 400

    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Error fetching cryptocurrency data: {str(e)}'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
