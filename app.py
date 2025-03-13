import mlflow
import pandas as pd
from flask import Flask, request, jsonify
import argparse
from mlflow.tracking import MlflowClient

def get_latest_model_uri(model_name: str) -> str:
    """Fetch the latest registered model version."""
    client = MlflowClient()
    versions = client.search_model_versions(f"name='{model_name}'")
    if not versions:
        raise ValueError(f"No versions found for model '{model_name}'")
    
    latest_version = max(versions, key=lambda mv: int(mv.version))
    return f"models:/{model_name}/{latest_version.version}"

def create_app(mlflow_tracking_uri: str, model_name: str):
    """Initialize the Flask app and load the latest MLflow model."""
    mlflow.set_tracking_uri(mlflow_tracking_uri)
    model = mlflow.pyfunc.load_model(get_latest_model_uri(model_name))
    app = Flask(__name__)

    @app.route('/predict', methods=['POST'])
    def predict():
        try:
            data = request.get_json(force=True)
            required_fields = [
                "Gender", "Balance", "NumOfProducts", "IsActiveMember",
                "Geography_France", "Geography_Germany", "Geography_Spain", "Age_bin"
            ]

            if not all(key in data for key in required_fields):
                missing = [key for key in required_fields if key not in data]
                return jsonify({"error": f"Missing fields: {', '.join(missing)}"}), 400
            
            input_df = pd.DataFrame([{key: float(data[key]) for key in required_fields}])
            predictions = model.predict(input_df).tolist()
            return jsonify({"predictions": predictions})

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return app

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Flask API for serving MLflow model.")
    parser.add_argument("--mlflow_tracking_uri", type=str, default="http://mlflow.example.com:8080")
    parser.add_argument("--model_name", type=str, default="my_model")
    
    args = parser.parse_args()
    app = create_app(args.mlflow_tracking_uri, args.model_name)
    app.run(host="0.0.0.0", port=5000)
