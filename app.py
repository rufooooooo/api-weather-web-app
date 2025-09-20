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
                  'appid' : 'c6c27dfd87f40baad629258b44b173d0'}

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