# import the access token from the api_access_token file
from API_access_token import ACCESS_TOKEN
#import the requests to request to the api
import requests
#Base url for api
BASE_URL = "https://api.instagram.com/v1/"
# a function to get self details from the instagram api
def getSelfDetails():
    url = BASE_URL + "users/self/?access_token=" + ACCESS_TOKEN
    my_info = requests.get(url)
    my_info = my_info.json()
    if my_info['meta']['code'] == 200:
        #print my_info;
        print "your username is : " + my_info['data']['username']
        print "your id is : " + my_info['data']['id']
        print "your follower count is : " + str(my_info['data']['counts']['follows'])
        print "your are followed by : " + str(my_info['data']['counts']['followed_by'])
# call self details function
getSelfDetails()

# a function to get another user id
def getUserId(userName):
    url = BASE_URL + "users/search?q=" + userName + "&access_token=" + ACCESS_TOKEN
    info = requests.get(url)
    info = info.json()
    if info['meta']['code'] == 200:
        if len(info['data']):
            return info['data'][0]['id']
        else:
            print "user does not exist"
            return "none"
    else:
        print "Status code other than 200 was recieved"
        return "none"

# get user details by its id
def getUserDetail():
    userName = raw_input("enter the user name to check : ")
    userId = getUserId(userName)
    if userId != "none":
        url = BASE_URL + "users/" + str(userId) + "/?access_token=" + ACCESS_TOKEN
        info = requests.get(url)
        info = info.json()
        # print info;
        print "your username is : " + info['data']['username']
        print "your id is : " + info['data']['id']
        print "your follower count is : " + str(info['data']['counts']['follows'])
        print "your are followed by : " + str(info['data']['counts']['followed_by'])

getUserDetail()