import os
from joblib import load
from django.shortcuts import render
from joblib import dump

model_path = os.path.join(os.path.dirname('diabets_project'), 'savedModels', 'model.joblib')
model = load(model_path)
dump(model, model_path, protocol=4)


def predictor(request):
    return render(request, 'index.html')

def predict_diabetes(request):
    
    # Fetch input data from the form
       
    Pregnancies=float(request.GET['Pregnancies'])
    Glucose= float(request.GET['Glucose'])
    BloodPressure= float(request.GET['BloodPressure'])
    SkinThickness=float(request.GET['SkinThicSkness'])
    Insulin=float(request.GET['Insulin'])
    bmi=float(request.GET['bmi'])
    DiabetesPedigreeFunction=float(request.GET['DiabetesPedigreeFunction'])
    Age=float(request.GET['Age'])
        # Add other features...

    # Make a prediction
    prediction = model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,bmi,DiabetesPedigreeFunction,Age]])

    # Map the prediction to a human-readable result
    result = 'Positive' if prediction[0] == 1 else 'Negative'

    return render(request, 'result.html', {'result': result})
