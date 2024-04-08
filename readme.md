# Gemstone Price Prediction

## Overview

This project aims to predict the price of gemstones using machine learning techniques, particularly employing Random Forest Regressor. The trained model achieves around 97% accuracy as measured by the r2 score. The application is deployed on the Render cloud platform.

## **Getting Started**

To access the deployed application, simply visit the following link:

Gemstone Price Prediction

# Project Structure

* app.py: Main Flask application file containing routes and prediction logic.
* Model/modelForPrediction.pkl: Pre-trained machine learning model (Random Forest Regressor) for predicting gemstone prices.
* templates/form.html: HTML template for input form to collect gemstone attributes.
* templates/result.html: HTML template to display the prediction result.

## How to Use

1. Access the deployed application using the provided link.
2. Enter the attributes of the gemstone (carat, cut, color, clarity, depth, table, x, y, z) into the form.
3. Submit the form to get the predicted price of the gemstone.

## Dependencies

* Flask
* scikit-learn
* pickle
* seaborn
* pandas
* numpy

## Deployment

The application is deployed on the Render cloud platform.

## Acknowledgments

* The project utilizes the Random Forest Regressor algorithm for prediction.
* Data preprocessing is done to convert categorical variables into numerical values.
* Flask web framework is used to create a simple user interface for prediction.
