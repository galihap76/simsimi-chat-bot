import requests

while True:
    me = input('galih ap : ')
    url = f'https://api.simsimi.net/v2/?text={me}&lc=id'
    response = requests.get(url)
    if response.status_code == 200:
        print('bot simsimi : ', response.json().get('success'))
    else:
        print('bad request!')