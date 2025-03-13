# Bank Churn Prediction API

## Overview

This repository contains a Flask-based API for serving an MLflow model to predict customer churn in a banking dataset. The API loads the latest version of the registered model from MLflow and exposes a REST endpoint for making predictions.

## Features

- Fetches the latest version of a registered model from MLflow.
- Exposes a `/predict` endpoint to make predictions using a trained model.
- Dockerized for easy deployment.
- CI/CD pipeline using Jenkins.

## Project Structure

```plaintext
├── app.py                   # Flask application
├── Dockerfile               # Docker container setup
├── requirements.txt         # Python dependencies
├── Jenkinsfile              # CI/CD pipeline setup
└── README.md                # Project documentation
```

## Installation & Setup

### Prerequisites

- Python 3.8+
- Docker
- MLflow server with a registered model

### Install Dependencies

```sh
pip install -r requirements.txt
```

### Run the Flask App

```sh
python app.py --mlflow_tracking_uri http://mlflow.example.com:8080 --model_name my_model
```

## API Usage

### Endpoint: `/predict`

- **Method**: `POST`
- **Content-Type**: `application/json`
- **Request Body**:

```json
{
    "Gender": 1,
    "Balance": 12000.5,
    "NumOfProducts": 2,
    "IsActiveMember": 1,
    "Geography_France": 1,
    "Geography_Germany": 0,
    "Geography_Spain": 0,
    "Age_bin": 3
}
```

- **Response**:

```json
{
    "predictions": [0.8]
}
```

## Docker Deployment

### Build Docker Image

```sh
docker build -t bank-churn-api .
```

### Run Docker Container

```sh
docker run -d -p 5000:5000 --name bank-churn-container bank-churn-api
```

## CI/CD Pipeline (Jenkins)

This project includes a Jenkins pipeline (`Jenkinsfile`) to automate building, tagging, and deploying the Docker container. The pipeline consists of the following stages:

1. Clone Repository
2. Build Docker Image
3. Tag Image
4. Push Image to Registry
5. Run Container

## Environment Variables

| Variable              | Description                     | Default Value                    |
| --------------------- | ------------------------------- | -------------------------------- |
| `MLFLOW_TRACKING_URI` | MLflow tracking server URL      | `http://mlflow.example.com:8080` |
| `MODEL_NAME`          | Name of the registered ML model | `my_model`                       |

## Dependencies

- Flask
- MLflow
- pandas
- scikit-learn
- cloudpickle
- numpy
- psutil
- scipy

## License

This project is licensed under the MIT License.

