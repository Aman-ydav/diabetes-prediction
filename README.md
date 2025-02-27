# Diabetes-Predictor

## Title: Improving Diabetes Prediction Accuracy Using Data Validation and Machine Learning.

## Problem Statement
Diabetes is a chronic disease that affects millions worldwide, requiring early detection and continuous monitoring. However, many healthcare systems struggle with:
Inconsistent and incomplete patient data
Misclassification of diabetes risk factors
Limited predictive accuracy in traditional diagnostic methods

## Features
- User-friendly web interface
- Input fields for health parameters
- Machine learning model prediction via FastAPI backend
- Dynamic data visualization with a doughnut chart
- Error handling and validation

## Technologies Used
- *Frontend:* HTML, CSS, JavaScript
- *Backend:* FastAPI (Python)
- *Machine Learning Model:* Logistic Regression (Scikit-Learn)
- *Database:* CSV dataset
- *Chart Visualization:* Chart.js

## Installation & Setup

### Backend Setup
1. *Clone the repository:*
   sh
   git clone https://github.com/your-repo/health-prediction.git
   cd health-prediction/Backend
   

2. *Create a virtual environment:*
   sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   

3. *Install dependencies:*
   sh
   pip install -r requirements.txt
   

4. *Train and save the model:*
   sh
   python model.py
   

5. *Run the FastAPI server:*
   sh
   uvicorn main:app --reload
   

### Frontend Setup
1. *Navigate to the frontend folder:*
   sh
   cd ../Frontend
   

2. *Open index.html in a browser*
   sh
   open index.html  # or manually open in a browser
   

## API Endpoints
- *POST /predict*: Accepts JSON input and returns a prediction.
  - *Request Format:*
    json
    {
      "highBP": 1,
      "highChol": 1,
      "bmi": 25.3,
      "stroke": 0,
      "heartDisease": 1,
      "physActivity": 1,
      "genHlth": 3,
      "physHlth": 10,
      "diffWalk": 0,
      "age": 30
    }
    
  - *Response Format:*
    json
    {
      "prediction": "Disease"
    }
    

## Troubleshooting
- *Chart not displaying?*
  - Ensure Chart.js is correctly linked in the HTML.
  - Check the console for errors and ensure resultChart ID exists in index.html.

- *Model not predicting correctly?*
  - Check if lifestyle_model.pkl is correctly saved and loaded.
  - Ensure feature scaling and data preprocessing are aligned in both training and prediction.

## Future Enhancements
- Improve UI/UX with better design and animations
- Enhance the machine learning model for better accuracy
- Store user data and past predictions in a database
- Deploy the application on a cloud platform
