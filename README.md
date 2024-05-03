# Crypto Price Checker
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python Version](https://img.shields.io/badge/Python-3.10-green)](https://www.python.org/downloads/)

## Description

The Crypto Price Checker is a Flask application that provides cryptocurrency price information. It allows users to fetch the price of a cryptocurrency by name through a simple API. This README.md file will guide you through the installation, usage, configuration, and deployment of the application.

## Installation

Before you can run the application, ensure you have the following prerequisites and dependencies:

- Docker
- Kubernetes (optional, for deployment)

To install the application, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/munuhee/crypto-price-checker-microservice.git
   cd crypto-price-checker
2. Build the Docker image:

    ```bash
    docker build -t crypto-price-checker

3. Run the Docker container:

    ```bash
    docker run -p 5000:5000 crypto-price-checker

Now, the Crypto Price Checker application is running locally on port 5000.

## Usage

API Endpoints
**GET /health**: Checks the health of the application. It returns a 200 OK response if the application is healthy.

**GET /**: Returns a welcome message for the Crypto API.

**POST /crypto_price**: Get the price of a cryptocurrency by providing its name in the request body.
**Example Request:**

```bash
   curl -X POST -H "Content-Type: application/json" -d '{"name": "Bitcoin"}' http://localhost:5000/crypto_price
```
**Example Response:**

```json
    { "name": "Bitcoin","price": 45000.0 }
```

If the cryptocurrency name is not found or if there is an error, appropriate error messages will be returned.

## Configuration
The application does not require extensive configuration, but you can customize some settings:

- `Dockerfile`: The Dockerfile contains instructions for building the Docker image of the application. You can modify it as needed.

- `docker-compose.yml`: This file defines the Docker Compose configuration for running the application. You can adjust the ports and health checks as necessary.

- `deployment.yaml`: If you want to deploy the application in a Kubernetes cluster, the deployment.yaml file specifies the deployment settings.

- `service.yaml`: The service.yaml file defines a Kubernetes Service to expose the application. You can modify it for your Kubernetes environment.

## Features
Check the health of the application using the /health endpoint.
Fetch the price of a cryptocurrency by providing its name through the /crypto_price endpoint.

### Code Examples
You can find code examples in the provided Python files:

- `app.py`: Contains the Flask application code, including API endpoints for health checks and cryptocurrency price retrieval.

- `test_app.py`: Contains unit tests for the Flask application to ensure its functionality.

## Deployment

**Docker**
To deploy the application using Docker, follow the installation instructions provided earlier. The Dockerfile and docker-compose.yml files are configured for easy deployment.

**Kubernetes**
If you want to deploy the application in a Kubernetes cluster, follow these steps:

Apply the Kubernetes deployment and service configurations:

```bash
    kubectl apply -f deployment.yaml
    kubectl apply -f service.yaml
```
