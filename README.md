# Housing Price Prediction Application

This repository contains a housing price prediction application built with a React frontend and a Flask backend. The application allows users to input various features of a house and predict its price using different machine learning algorithms.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Overview
The Housing Price Prediction Application provides an interface for users to enter details about a property and choose a machine learning algorithm to predict the price of the property. The backend is equipped with multiple models, including XGBoost, Linear Regression, Random Forest, and Gradient Boosting.

## Features
- User-friendly interface to input house features
- Dropdown menus for categorical features
- Selection of various machine learning algorithms
- Display of predicted price and model performance metrics (R² scores)
- Real-time prediction using a Flask API

## Technologies Used

### Frontend
- React
- Bootstrap

### Backend
- Flask
- Pandas
- Scikit-learn
- XGBoost
- Flask-CORS

## Installation
Follow these steps to set up the application locally.

### Frontend
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/housing-price-prediction.git
    cd housing-price-prediction/frontend
    ```
2. Install dependencies:
    ```bash
    npm install
    ```
3. Start the React application:
    ```bash
    npm start
    ```

### Backend
1. Navigate to the backend directory:
    ```bash
    cd ../backend
    ```
2. Set up a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Place the dataset (`dataset_etiketlenmis_son.xlsx`) in the backend directory.

5. Start the Flask application:
    ```bash
    flask run
    ```

## Usage
1. Open the frontend application in your browser at [http://localhost:3000](http://localhost:3000).
2. Fill in the form with the necessary house details.
3. Select a machine learning algorithm from the dropdown menu.
4. Click the "Gönder" button to get the price prediction.
5. View the predicted price and model performance metrics displayed on the page.

## Project Structure
```plaintext
housing-price-prediction/
├── frontend/
│   ├── src/
│   │   ├── MainPage.js
│   │   ├── dataset.js
│   │   └── ...
│   ├── public/
│   └── package.json
└── backend/
    ├── app.py
    ├── requirements.txt
    └── dataset_etiketlenmis_son.xlsx
```
### Frontend
- `MainPage.js`: The main component containing the form and logic for handling user input and API requests.
- `dataset.js`: Contains dataset mappings for categorical feature transformations.

### Backend
- `app.py`: The Flask application with endpoints for model training and prediction.
- `requirements.txt`: Lists the Python dependencies for the backend.

## Contributing
Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-branch
    ```
3. Make your changes and commit them:
    ```bash
    git commit -m "Add new feature"
    ```
4. Push to the branch:
    ```bash
    git push origin feature-branch
    ```
5. Submit a pull request.

