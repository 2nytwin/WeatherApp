from django.shortcuts import render
import requests

def index(request):
    appid = '0cca4103265bb8e736a69753d1f5607a'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' +appid

    city = 'Los Angeles'
    res = requests.get(url.format(city))

    print(res.text)

    return render(request, 'weather/index.html')
