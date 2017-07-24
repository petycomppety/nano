import json, requests

slack_data = {"text": "Miner problem detected..\nMiner restart in progress."}
webhook_url = 'https://hooks.slack.com/services/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'

response = requests.post(
    webhook_url, data=json.dumps(slack_data),
    headers={'Content-Type': 'application/json'}
)
if response.status_code != 200:
    raise ValueError(
        'Request to slack returned an error %s, the response is:\n%s'
        % (response.status_code, response.text)
    )