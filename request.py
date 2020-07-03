import requests
import json
from flask import jsonify



url = 'http://127.0.0.1:5000/recommand' 
r = requests.post(url,json={"parameter":"Mademoiselle at Arms"})
print(r.status_code)
if(r.status_code ==200):
     print(r.json())
else:
    print("Not found")
    