from django.shortcuts import render
from django.http import HttpResponse
from .models import Data
from django.utils import timezone
from django.db.models import Avg

def home(request):
    all_data = Data.objects.order_by('-date')
    Temp_Avg = Data.objects.aggregate(Avg('temp'))
    Temp_Avg = Temp_Avg["temp__avg"] 
    Humidity_Avg = Data.objects.aggregate(Avg('humidity'))
    Humidity_Avg = Humidity_Avg["humidity__avg"]
    last_pk = all_data.count()

    context = {
        'all_data':all_data,
        'Temp_Avg':Temp_Avg,
        'Humidity_Avg':Humidity_Avg,
        'last_pk':last_pk,
        }

    return render(request, 'data/home.html',context)



def add_data(request):
    if request.method == 'POST':
        if request.POST['humidity'] and request.POST['temp']:
            data = Data()
            data.humidity = request.POST['humidity']
            data.temp = request.POST['temp']
            data.tozih = request.POST['tozih']
            data.date = timezone.datetime.now()
            data.save()
            return render(request,'data/home.html')
    else:
        return render(request, 'data/add_data.html')

        
        