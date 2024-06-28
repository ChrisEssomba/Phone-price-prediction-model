import joblib
import numpy as np
from flask import Flask, request, jsonify, render_template
from sklearn.calibration import LabelEncoder

app = Flask(__name__)

#We import our model, the normalizer used and the scaler used
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')
label_encoder = joblib.load('label_encoder.pkl')

#We precise the mapping did to normalized the device brand
device_brand_mapping = {
    'Honor': 0, 'Others': 1, 'HTC': 2, 'Huawei': 3, 'Infinix': 4, 'Lava': 5,
    'Lenovo': 6, 'LG': 7, 'Meizu': 8, 'Micromax': 9, 'Motorola': 10,
    'Nokia': 11, 'OnePlus': 12, 'Oppo': 13, 'Realme': 14, 'Samsung': 15,
    'Vivo': 16, 'Xiaomi': 17, 'ZTE': 18, 'Apple': 19, 'Asus': 20,
    'Coolpad': 21, 'Acer': 22, 'Alcatel': 23, 'BlackBerry': 24, 'Celkon': 25,
    'Gionee': 26, 'Google': 27, 'Karbonn': 28, 'Microsoft': 29,
    'Panasonic': 30, 'Sony': 31, 'Spice': 32, 'XOLO': 33
}

#The home page
@app.route('/')
def home():
    return render_template('index.html')

#The retrieve of data once entered by the user
@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    # Retrieve form data and convert appropriate values to integers or floats
    device_brand = request.form['device_brand_encoded']  
    fourG = request.form['4g'] #the string values are not converted, just taken
    fiveG = request.form['5g']
    screen_size = float(request.form['screen_size'])
    rear_camera_mp = float(request.form['rear_camera_mp'])
    front_camera_mp = float(request.form['front_camera_mp'])
    internal_memory = float(request.form['internal_memory'])
    ram = float(request.form['ram'])
    battery = float(request.form['battery_power'])
    release_year = int(request.form['release_year'])
    days_used = int(request.form['days_used'])
    normalized_new_price = float(request.form['normalized_new_price'])




     #We Encode categorical features 4g and 5g
    fourG = 1 if fourG == 'yes' else 0
    fiveG = 1 if fiveG == 'yes' else 0

    #We Map device brand to its encoded value
    device_brand_encoded = device_brand_mapping[device_brand]
    
    #We Combine all features into a single list
    features = [
        device_brand_encoded, screen_size, fourG, fiveG, rear_camera_mp, front_camera_mp, internal_memory, 
        ram, battery, release_year, days_used,  
        normalized_new_price  
    ]
    
    # Reshape and scale new data using loaded scaler
    X_new_scaled = scaler.transform([features])
    prediction = model.predict(X_new_scaled)

    return render_template('index.html', prediction_text='The price of your phone is : {:.2f} $'.format(prediction[0])) #We make sure to return two digits after the dot.


if __name__ == "__main__":
    app.run(debug=True)
