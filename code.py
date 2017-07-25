import requests, json, sys, time
from subprocess import call


r = requests.get('http://chpchp.ethosdistro.com/?json=yes')
parse = r.json()
json_str = json.dumps(parse)
resp = json.loads(json_str)
total_hash = resp['total_hash']
print (resp['total_hash'])

if total_hash < 120: 
    print "Error"
    call(["/opt/ethos/bin/disallow"])
    call(["/opt/ethos/bin/minestop"])
    time.sleep(60)
    call(["/opt/ethos/bin/allow"])
    call(["/opt/ethos/bin/minestart"])
else:
    print "OK"