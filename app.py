"""
Crypto API Flask App

This Flask app provides cryptocurrency price information.
"""

from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Constants
COINSTATS_API_URL = 'https://api.coinstats.app/public/v1/coins/'

@app.route('/health')
def health_check():
    """
    This route return a 200 OK response if your application is healthy
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
        response = requests.get(COINSTATS_API_URL, timeout=10)

        if response.status_code == 200:
            coin_data = response.json()
            coins = coin_data.get('coins', [])

            matching_coin = next((coin for coin in coins if crypto_name.lower() == coin.get('name', '').lower()), None)

            if matching_coin:
                price = matching_coin.get('price', 0)
                return jsonify({'name': crypto_name, 'price': price})
            return jsonify({'error': 'Crypto name not found'}), 404
        return jsonify({'error': 'Failed to fetch cryptocurrency data'}), 400

    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Error fetching cryptocurrency data: {str(e)}'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
