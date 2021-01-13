import requests


def change_desc(desc):
    headers = {
        'authority': 'twitter.com',
        'x-twitter-client-language': 'tr',
        'x-csrf-token': 'token',
        'authorization': 'Bearer #',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
        'x-twitter-auth-type': 'OAuth2Session',
        'x-twitter-active-user': 'yes',
        'origin': 'https://twitter.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://twitter.com/settings/profile',
        'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': '',
    }

    data = {
      'description': desc
    }

    response = requests.post('https://twitter.com/i/api/1.1/account/update_profile.json', headers=headers, data=data)

