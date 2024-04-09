from django.shortcuts import render
import requests
import datetime
from django.contrib import messages
# # Create your views here.

      
      
def home(request):
    # condition for finding city 
    if 'city' in request.POST:
        city = request.POST['city']
        print('before', city)
    else:
        city = 'Dalhousie'
        print('after', city)
        
    # configuring Weather API key I have used Free Weather API 
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=1885ff97309b29aaf6bd478cf93cedd5'
    PARAMS = {'units':'metric'}
    
    # ADDING GOOGLE CITY IMAGES API AND GOOGLE SEARCH ENGINE API
    API_KEY = 'Your API key '
    SEARCH_ENGINE_ID = 'SEarch Engine ID'
    query = city + "1920x1080"
    page = 1
    start = (page-1) * 10 + 1
    searchType = 'image'
    city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"
    
    try:
        # Getting data from the Google Custom Search API
        data = requests.get(city_url).json()
        search_items = data.get("items")
        
        if search_items:
            image_url = search_items[0]['link']  # Assuming you want the first image
            
        # Getting data from the Weather API
        data = requests.get(url, PARAMS).json()
        
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        
        day = datetime.date.today()
        
        return render(request, 'WeatherApp/index.html', {
            'description': description, 'icon': icon, 'temp': temp, 'day': day, 'city': city,
            'exception_occurred': False, 'image_url': image_url,
        })
    
    except Exception as e:
        messages.error(request, 'An error occurred: ' + str(e))
        return render(request, 'WeatherApp/index.html', {
            'description': 'Clear Sky', 'icon': '01d', 'temp': '', 'day': '', 'city': 'Dalhousie',
            'exception_occurred': True,
        })
