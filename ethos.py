import requests, json, sys, time
from subprocess import call

webhook_url = 'https://hooks.slack.com/services/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'

def slack( slack_data ):
    response = requests.post(
        webhook_url, data=json.dumps({"text":slack_data}),
        headers={'Content-Type': 'application/json'}
    )
    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
        )
    return


total_hash = requests.get('http://chpchp.ethosdistro.com/?json=yes').json()['total_hash']
print total_hash

if total_hash < 120:
    print "Error"
    slack("Miner problem detected..\nMiner restart in progress.")
    call(["disallow"])
    call(["minestop"])
    time.sleep(60)
    call(["allow"])
    call(["minestart"])
else:
    print "OK"