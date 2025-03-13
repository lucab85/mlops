# Use an official Python runtime as a parent image
FROM python:slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose port 5000 for the Flask app
EXPOSE 5000

# Set environment variables for MLflow
ENV MLFLOW_TRACKING_URI=http://mlflow.example.com:8080
ENV MODEL_NAME=my_model

# Define the command to run the application
CMD ["sh", "-c", "python app.py --mlflow_tracking_uri $MLFLOW_TRACKING_URI --model_name $MODEL_NAME"]
