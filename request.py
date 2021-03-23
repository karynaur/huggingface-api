import requests
import json

url='https://intense-refuge-52907.herokuapp.com/app.py'

data={'text':'My name is Aditya and I love music'}
j_data=json.dumps(data)
headers={'content-type': 'application/json','Accept-Charset': 'UTF-8'}
r=requests.post(url,data=data)

print(r.json()['out'])
