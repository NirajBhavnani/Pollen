import datetime
import dill
import requests
import pandas as pd
def pred(cty):
    #declare dictionary
    latlong1={
        'Mumbai':['19.0760,72.8777'],
        'Delhi':['28.7041,77.1025'],
        'Kolkata':['22.5726,88.3639'],
        'Jammu':['32.7266,74.8570'],
        'Kanyakumari':['8.0883,77.5385']
    }
    latlong2={
        'Mumbai':['19.0760','72.8777'],
        'Delhi':['28.7041','77.1025'],
        'Kolkata':['22.5726','88.3639'],
        'Jammu':['32.7266','74.8570'],
        'Kanyakumari':['8.0883','77.5385']
    }
    #get weather data
    parameters={
        'q':latlong1[cty][0],
        'num_of_days':'3',
        'tp':'24',
        'format':'json',
        'key':'20af7873b5614dd28f654636210604',
        'cc':'no',
        'mca':'no'
    }
    url = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
    response = requests.request("GET", url, params=parameters)
    data = response.json()
    #print(data)
    date=[]
    city=[]
    lat=[]
    lng=[]
    maxtempC=[]
    mintempC=[]
    avgtempC=[]
    sunHour=[]
    uvIndex=[]
    windspeedKmph=[]
    winddirDegree=[]
    precipMM=[]
    humidity=[]
    visibility=[]
    pressure=[]
    cloudcover=[]
    DewPointC=[]
    for j in data['data']['weather']:
        city.append(cty)
        l=latlong2[cty]
        
        lat.append(l[0])
        lng.append(l[1])
        date.append(j['date'])
        maxtempC.append(j['maxtempC'])
        mintempC.append(j['mintempC'])
        avgtempC.append(j['avgtempC'])
        sunHour.append(j['sunHour'])
        uvIndex.append(j['uvIndex'])
        windspeedKmph.append(j['hourly'][0]['windspeedKmph'])
        winddirDegree.append(j['hourly'][0]['winddirDegree'])
        precipMM.append(j['hourly'][0]['precipMM'])
        humidity.append(j['hourly'][0]['humidity'])
        visibility.append(j['hourly'][0]['visibility'])
        pressure.append(j['hourly'][0]['pressure'])
        cloudcover.append(j['hourly'][0]['cloudcover'])
        DewPointC.append(j['hourly'][0]['DewPointC'])
    dct = {'city': 0, 'latitude': lat, 'longitude': lng, 'maxtempC': maxtempC, 'mintempC': mintempC, 'avgtempC': avgtempC,
        'sunHour': sunHour,'uvIndex': uvIndex,'windspeedKmph': windspeedKmph, 'winddirDegree':winddirDegree,
        'precipMM': precipMM, 'humidity': humidity, 'visibility': visibility, 'pressure': pressure, 'cloudcover': cloudcover, 'DewPointC': DewPointC }      
    df = pd.DataFrame(dct)
    
    x=df.iloc[:,:]
    
    filename=cty.lower()
    ext='.obj'
    path="/Volumes/NRJ'S EHD/Mac/BE Project"+"/"+filename+ext
    regressor=dill.load(open(path,'rb'))
    y_pred = regressor.predict(x)
    y = []
    y.append(y_pred)
    for k in avgtempC:
      y.append(k)
    return(y)