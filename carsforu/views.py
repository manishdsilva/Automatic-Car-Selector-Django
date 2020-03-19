from django.shortcuts import render
from pandas import DataFrame
from sklearn.externals import joblib 


def index(request):
    return render(request, 'carsforu/index.html', {})

def submit_it(request):
    budget = int(request.POST['budget'])
    mileage = int(request.POST['mileage'])
    performance = int(request.POST['performance'])
    seats = int(request.POST['seats'])
    
    data = [[mileage,performance,seats,budget]]
    df_pred = DataFrame(data, columns = ['Mileage', 'Engine_Power', 'Number_of_seats','Price'])

    car_model = joblib.load('carsforu/cars.pkl')
    y_pred = car_model.predict(df_pred)
    
    suggested = str(y_pred)
    suggested = suggested[2:-2]
    return render(request, 'carsforu/submit.html', {'suggested':suggested})