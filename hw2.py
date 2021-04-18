import requests
import os
from flask import Flask
from flask import request
app=Flask(__name__)
@app.route('/')
def root():
        st=''
        country = request.args.get('country')
        print('------Enter a country name-----')
        #country=input()
        #country = 'israel'
        resp = requests.get('http://restcountries.eu/rest/v2/name/'+country+'?fullText=true')
        if resp.status_code !=200:
            print ('api error')
            return 'we dont have any information about :'+country+' country'
        else:
          st+='Country Full Name: '+country+'<br />'
          print('Country Full Name: '+country)
          for item in resp.json():
            st+='Country Full Capital: '+item['capital']+'<br />'
            print('Country Full Capital: '+item['capital'])
            for j in item['languages']:
               st+='Country Common Language: '+j['name']+'<br />'
               print('Country Common Language: '+j['name'])
            for j in item['currencies']:
               st+='Country Currency Name: '+j['name']+'<br />'
               print('Country Currency Name: '+j['name'])
               resp2=requests.get('http://data.fixer.io/api/latest?access_key=0f74f9e3e64cb0c2ce6ec5230dc7592d&format=1&symbols='+j['code'])
               rate=resp2.json()
               rates=rate['rates']
               st+='Country Currency Rate: '+str(rates[j['code']])+'<br />'
               print('Country Currency Rate: '+str(rates[j['code']]))
        return st
app.run('0.0.0.0',debug=True)


