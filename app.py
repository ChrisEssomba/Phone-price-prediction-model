from flask import Flask, request, jsonify
import joblib

# Load the serialized model
model = joblib.load('model.pkl')

# Create Flask app
app = Flask('app')

# Define a route for prediction
@app.route('/', methods=['GET'])
def predict():
   return "Hello world"

# Run the Flask app
if __name__ == '__main__':
    app.run(port=3000, debug=True)
