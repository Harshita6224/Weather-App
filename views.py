from django.shortcuts import render
import  requests

# Create your views here.
def weather(request):
    if request.method == 'POST':
        city=request.POST.get['city']
        
        source="https://api.openweathermap.org/data/2.5/weather?q={city}&appid=6d410a46652b3a30c899faf53ed67a53"
        list_of_data=requests.get(source).json()

        data={
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
            "temp":round((list_of_data['main']['temp']-32) * 5.0/9.0,2),
            "humidity": str(list_of_data['main']['humidity'])
        }
    else:
        data={}
    return render(request, "weather.html",data)    