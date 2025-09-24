# Webapp for weather information

from flask import Flask, render_template, request

import requests

app = Flask(__name__)

# Create a home page using app.route decorator
@app.route('/')
def home():
    return render_template('winput.html')

# Create submit page and accept the data using request
@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        result = request.form
        
        web_params = {'q' : result['city'],
                  'units' : result['units'],
                  'appid' : 'ENTER YOUR API HERE'}

        web_url = r'http://api.openweathermap.org/data/2.5/weather?'
        
        web_response  = requests.get(url = web_url, params = web_params)
        web_data      = web_response.json()
        
        # Data to be passed - City, Temp, Feels Like Weather, Windspeed
        web_result    = {'city'      :    result['city'],
                         'temp'      :    web_data['main']['temp'],
                         'feels_like':    web_data['main']['feels_like'],
                         'weather'   :    web_data['weather'][0]['description'],
                         'wind'      :    web_data['wind']['speed']}
        
        return render_template('wdisplay.html', result=web_result)
    else:
        return 'Invalid Request'
    
if __name__ == '__main__':
    app.run()
    
    
# The code explained in English:
# In the first line, from flask we import Flask, render_template and request
# We need Flask for the backend, render_template for the html templates and request to handle form data
# Then we import requests to make API calls. These are the essential components for our backend.


# We define two routes using @app.route decorator:
# The first route is the home page which returns the 'winput.html' template - this is what we will see in our home page,
# when we open it.
# The second route '/submit' handles both POST and GET methods, but we primarily use POST for form submission.

# When a POST request is received (user submits the form):
# - We extract form data using request.form
# - Prepare three parameters for the API: city (q), temperature units, and API key (appid) for authentication
# - Construct the API URL and make the GET request to OpenWeatherMap
# - Convert the API response from JSON format to a Python dictionary for easier data access

# The web_result dictionary combines:
# - The city name from the original form submission
# - Four weather metrics extracted from the API response: temperature, feels-like, weather description, and wind speed

# Finally, we render the 'wdisplay.html' template passing the weather results.
# If someone tries to access /submit directly via GET, they see 'Invalid Request'

# The last two lines ensure the app runs when executed directly
