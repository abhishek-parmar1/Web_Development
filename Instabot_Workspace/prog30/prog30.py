# import the access token from the api_access_token file
from API_access_token import ACCESS_TOKEN
#import the requests to request to the api
import requests
# to get the data in the url use this function urlretrieve
from urllib import urlretrieve
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
        getUserPost(userId)

# get user recent post id
def getUserPost(userId):
    url = BASE_URL + "users/" + str(userId) + "/media/recent/?access_token=" + ACCESS_TOKEN
    info = requests.get(url)
    info = info.json()
    if info['meta']['code'] == 200:
        postId = info['data'][0]['id']
        print "recent post id : " + postId
        getUserPostContent(postId)

# get user recent post content
def getUserPostContent(postId):
    url = BASE_URL + "media/" + str(postId) + "?access_token=" + ACCESS_TOKEN
    info = requests.get(url)
    info = info.json()
    if info['meta']['code'] == 200:
        if info['data']['type'] == "image":
            mediaUrl = info['data']['images']['standard_resolution']['url']
            urlretrieve(mediaUrl,'postImage.png');
            print "post image downloaded"
        elif info['data']['type'] == "video":
            mediaUrl = info['data']['videos']['standard_resolution']['url']
            urlretrieve(mediaUrl, 'postVideo.png');
            print "post video downloaded"

getUserDetail()