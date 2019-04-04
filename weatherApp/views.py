import  requests
from django.shortcuts import render
from .models import  City
from .form import CityForm
def index(request):
    url= 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=ada6155130fb8cb5bfeda5f927805dd7'
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:

        res = requests.get(url.format(city)).json()

        city_weather = {
           'city': city,
           'temperature': res['main']['temp'],
           'description': res['weather'][0]['description'],
           'icon': res['weather'][0]['icon'],

    }
        weather_data.append(city_weather)
    context = {"weather_data": weather_data,'form':form}

    return  render(request,'weather.html',context)


