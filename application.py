from flask import Flask, request, render_template, redirect
from flask_cors import CORS, cross_origin
import pickle

app = Flask(__name__)
CORS(app)

# Load the trained model
model = pickle.load(open("Model/ModelForPrediction.pkl", "rb"))

def preprocess_input(carat, cut, color, clarity, depth, table, x, y, z):
    # Define mapping dictionaries
    cut_map = {"Fair": 1, "Good": 2, "Very Good": 3, "Premium": 4, "Ideal": 5}
    color_map = {"D": 1, "E": 2, "F": 3, "G": 4, "H": 5, "I": 6, "J": 7}
    clarity_map = {"I1": 1, "SI2": 2, "SI1": 3, "VS2": 4, "VS1": 5, "VVS2": 6, "VVS1": 7, "IF": 8}

    # Map categorical variables to numerical values
    cut_encoded = cut_map[cut]
    color_encoded = color_map[color]
    clarity_encoded = clarity_map[clarity]

    # Create feature array
    features = [[carat, cut_encoded, color_encoded, clarity_encoded, depth, table, x, y, z]]

    return features


# Route for landing directly on prediction form
@app.route('/')
@cross_origin()
def index():
    return redirect('/predict')

# Route for prediction form page
@app.route('/predict', methods=['GET', 'POST'])
@cross_origin()
def predict_form():
    if request.method == 'POST':
        # Get input data from form
        carat = float(request.form['carat'])
        cut = request.form['cut']
        color = request.form['color']
        clarity = request.form['clarity']
        depth = float(request.form['depth'])
        table = float(request.form['table'])
        x = float(request.form['x'])
        y = float(request.form['y'])
        z = float(request.form['z'])

        # Preprocess input data
        features = preprocess_input(carat, cut, color, clarity, depth, table, x, y, z)

        # Make prediction
        prediction = model.predict(features)

        # Display prediction
        return render_template('result.html', prediction=prediction[0])

    return render_template('form.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
