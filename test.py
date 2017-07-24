import requests, json

total_hash = requests.get('http://chpchp.ethosdistro.com/?json=yes').json()['total_hash']
print total_hash
