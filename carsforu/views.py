from django.shortcuts import render
from pandas import DataFrame
from django.views.decorators.csrf import csrf_protect
import joblib 


def index(request):
    return render(request, 'carsforu/index.html', {})




def submit_it(request):
    budget = int(request.POST.get('budget'))
    mileage = int(request.POST.get('mileage'))
    performance = int(request.POST.get('performance'))
    seats = int(request.POST.get('seats'))
    
    data = [[mileage,performance,seats,budget]]
    df_pred = DataFrame(data, columns = ['Mileage', 'Engine_Power', 'Number_of_seats','Price'])

    car_model = joblib.load('carsforu/cars.pkl')
    y_pred = car_model.predict(df_pred)
    
    suggested = str(y_pred)
    suggested = suggested[2:-2]
    print(suggested)
    return render(request, 'carsforu/submit.html', {'suggested':suggested})