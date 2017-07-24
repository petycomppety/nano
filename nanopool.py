import requests


user = requests.get('https://api.nanopool.org/v1/eth/user/0x38d95452cC882eF1D7c59EC77a9c21a3aa0DD1bB').json()

h6 = user['data']['avgHashrate']['h6']
h24 = user['data']['avgHashrate']['h24']
hashrate = user['data']['hashrate']
balance = user['data']['balance']
response = requests.get('https://api.nanopool.org/v1/eth/balance_hashrate/0x38d95452cC882eF1D7c59EC77a9c21a3aa0DD1bB').json()

#hashrate = response['data']['hashrate']
#balance = response['data']['balance']

print 'Actual hashrate:', hashrate
print 'Hashrate - 6 hours avg:', h6
print 'Hashrate - 24 hours avg:', h24
print 'Actual balance:', balance



#total_hash = requests.get('https://api.nanopool.org/v1/eth/balance_hashrate/0x38d95452cC882eF1D7c59EC77a9c21a3aa0DD1bB').json()['data']['hashrate']
#print total_hash
