################################################################################
# Facebook App
#

import requests
from requests.auth import HTTPBasicAuth
import json

print "Facebook App"

# GET /v2.5/me HTTP/1.1
# Host: graph.facebook.com

url = "https://graph.facebook.com/v2.9/me"
headers = {'user-agent': '/v2.5/me'}
#response = requests.get(url, auth=(access_token))

#url = "https://graph.facebook.com/v2.9/me?access_token="

#response = requests.get(url)

def GetMyStatusUpdates(access_token):
    url = "https://graph.facebook.com/v2.9/me/feed"
    response = requests.get(url + '?access_token=' + access_token)


    print response.status_code
    print

    jsonresponse = response.text
    parsed = json.loads(jsonresponse)
    print json.dumps(parsed, indent=4)

    print "======================"


def GetCurrentUserInfo(access_token):
    #access_token='EAACEdEose0cBAGcQVkyf5S2SE6peb140hiqhBKkVD2ZBl1LmPw0mwPkcGka99WTaB7rmwwZBAszvcYF8KJmVTcIF4HjCnHFPFb9WeBv2ZConNhkWAtpmkTZABCNCdUhVZBno25fgeLbTE1DVQowZA7ZA4VJqv1MG5x3qZCzPs6UUOPySY3Bm64nB'
    url = "https://graph.facebook.com/v2.9/me"
    response = requests.get(url + '?access_token=' + access_token)

    print response.status_code

    jsonresponse = response.text
    parsed = json.loads(jsonresponse)
    print json.dumps(parsed, indent=4)



def GetCurrentUserPhotos(access_token):
    #access_token='EAACEdEose0cBAGcQVkyf5S2SE6peb140hiqhBKkVD2ZBl1LmPw0mwPkcGka99WTaB7rmwwZBAszvcYF8KJmVTcIF4HjCnHFPFb9WeBv2ZConNhkWAtpmkTZABCNCdUhVZBno25fgeLbTE1DVQowZA7ZA4VJqv1MG5x3qZCzPs6UUOPySY3Bm64nB'
    url = "https://graph.facebook.com/v2.9/me/photos"
    response = requests.get(url + '?access_token=' + access_token)

    print response.status_code

    jsonresponse = response.text
    parsed = json.loads(jsonresponse)
    print json.dumps(parsed, indent=4)




access_token = #Insert access token here#

GetCurrentUserInfo(access_token)
GetMyStatusUpdates(access_token)
GetCurrentUserPhotos(access_token)

