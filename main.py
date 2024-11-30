from flask import Flask,render_template, request
import requests

app = Flask(__name__)

def get_weather_data(city:str):

    API_KEY = '1a828cf671e8fd8e9d2b0ab798f3d988'
    idioma = 'es'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang={idioma}&appid={API_KEY}'
    r = requests.get(url).json()
    return r

@app.route('/kevin.html')
def kevin():
    return render_template('kevin.html')

@app.route("/",methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', ciudad='', humedad='',presion='', descripcion='', icon = '', lat='', lon='',cod = '')

    ciudad= request.form.get('txtCiudad')
    if ciudad:
        data=get_weather_data(ciudad) 
        cod=data.get('cod')
        if cod != 200:
            return render_template('index.html', ciudad='', humedad='',presion='', descripcion='', icon = '' , lat='', lon='', cod = cod)
        lat=data.get('coord').get('lat')
        lon=data.get('coord').get('lon')
        humedad=data.get('main').get('humidity')
        presion=data.get('main').get('pressure')
        descripcion=data.get('weather')[0].get('description')
        icon=data.get('weather')[0].get('icon')
        return render_template('index.html', ciudad=ciudad, humedad=humedad,presion=presion, descripcion=descripcion, icon = icon , lat=lat, lon=lon, cod = cod)
    else:
        return render_template('index.html', ciudad='', humedad='',presion='', descripcion='', icon = '', lat='', lon='',cod = '')


if __name__ == "__main__":
    app.run(debug=True)