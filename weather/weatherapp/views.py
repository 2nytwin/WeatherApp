from django.shortcuts import render
import requests


def index(request):
    appid = '0cca4103265bb8e736a69753d1f5607a'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    city = 'Los Angeles'
    res = requests.get(url.format(city)).json()

    city_info = {
        'city': city,
        'temp': res['main']['temp'],
        'icon': res['weather'][0]['icon']
    }

    context = {
        'info': city_info
    }

    return render(request, 'weather/index.html', context)
