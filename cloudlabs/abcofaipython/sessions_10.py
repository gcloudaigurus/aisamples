
# Import necessary libraries
import pickle  # For loading the pre-trained model
import numpy as np # For numerical operations, especially array handling
from flask import Flask, request, jsonify # For creating a web API

# Load the pre-trained model.  Replace 'model.pkl' with your model's filename.
#  Assume the model expects a NumPy array as input and returns a prediction.
try:
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    print("Error: model.pkl not found. Please ensure your model file is named 'model.pkl' and in the same directory.")
    exit(1) #Exit with an error code


# Initialize Flask app
app = Flask(__name__)


# Define API endpoint for prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the request (expecting JSON)
    try:
        data = request.get_json()
        input_data = np.array(data['input']) # Access the input array from the JSON
        #print(input_data) # for debugging purposes
        
        #Check input dimensions. Adjust as needed for your model
        expected_shape = (1,10) #Example: expecting a 1x10 array. Change this to match your model's input shape.
        if input_data.shape != expected_shape:
            return jsonify({'error': f'Invalid input shape. Expected {expected_shape}, got {input_data.shape}'}), 400


    except (KeyError, ValueError):
        return jsonify({'error': 'Invalid input data'}), 400


    # Make prediction using the loaded model
    try:
        prediction = model.predict(input_data)
        #print(prediction) # for debugging purposes

    except Exception as e:
        return jsonify({'error': f'Prediction error: {e}'}), 500


    # Return prediction as JSON response
    return jsonify({'prediction': prediction.tolist()}) # Convert NumPy array to list for JSON serialization


# Run the app (only if the script is run directly, not imported as a module)
if __name__ == '__main__':
    app.run(debug=True) #Set debug=False for production



#To use this:
#1.  Train a model and save it as 'model.pkl' using pickle.dump(model, open('model.pkl', 'wb'))
#2.  Install Flask: pip install Flask
#3. Run this script.
#4. Send a POST request to http://127.0.0.1:5000/predict with a JSON payload like this:
#   { "input": [1,2,3,4,5,6,7,8,9,10] }  (replace with your actual input data)

#Note:  This is a basic example.  Error handling, input validation, and security measures should be significantly improved for production deployment.  Consider using a more robust framework like FastAPI for production-level applications.

