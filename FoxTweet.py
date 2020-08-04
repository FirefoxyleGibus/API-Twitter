from twython import Twython
from twython import TwythonStreamer
import json
from random import shuffle

with open(r"D:\Twitter API info\twitter_credentials.json", "r") as file:
    creds = json.load(file)
Consumer_Key = creds['CONSUMER_KEY']
Consumer_Secret = creds['CONSUMER_SECRET']
Fox = Twython(Consumer_Key, Consumer_Secret)
client = Twython(Consumer_Key, Consumer_Secret)

def Connect(client):
    auth = client.get_authentication_tokens()
    OAUTH_TOKEN = auth['oauth_token']
    OAUTH_TOKEN_SECRET = auth['oauth_token_secret']
    auth['auth_url']
    oauth_verifier = request.GET["d8sYM4JZloI9eZuJN0sCaHqdYanWNvp3"]
    client = Twython(Consumer_Key, Consumer_Secret,
                   OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    final_step = client.get_authorized_tokens(oauth_verifier)
    F_OAUTH_TOKEN = final_step['oauth_token']
    F_OAUTH_TOKEN_SECRET = final_step['oauth_token_secret']
    client = Twython(Consumer_Key, Consumer_Secret,
                   F_OAUTH_TOKEN, F_OAUTH_TOKEN_SECRET)
    return client
    User = client.verify_credentials()
    print(User["screen_name"],"succefully connected")

def Post(text):
    post = client.update_status(status=text)
    return "https://twitter.com/"+str(User["screen_name"])+"/statuses/"+str(post["id"])

def Photo_Post(path,text):
    photo = open(path, 'rb')
    response = client.upload_media(media=photo)
    post = client.update_status(status=text, media_ids=[response['media_id']])
    return "https://twitter.com/"+str(User["screen_name"])+"/statuses/"+str(post["id"])

def Video_Post(path,text):
    video = open(path, "rb")
    response = client.upload_video(media=video, media_type="video/mp4")
    post = client.update_status(status=text, media_ids=[response['media_id']])
    return "https://twitter.com/"+str(User["screen_name"])+"/statuses/"+str(post["id"])

def Retweet(lien):
    Id = lien[lien.rfind('/')+1:]
    post = client.retweet(id=Id)
    print("Post retweeté avec succés")

def Like(lien):
    Id = lien[lien.rfind('/')+1:]
    client.create_favorite(id=Id)
    print("Post liké avec succés")

def Get_Timeline(**param):
    TL = client.get_home_timeline(**param)
    for tweet in TL:
        print()
        print("@"+str(tweet["user"]["screen_name"]),":")
        print(tweet['text'])
        print()
        print("Created at :",tweet["created_at"])
        print()
        print("Link : https://twitter.com/"+str(tweet["user"]["screen_name"])+"/statuses/"+str(tweet["id"]))

def Get_retweetersID(Id,counter = 100,cur = -1,strid = "True"):
    Out = client.get_retweeters_ids(id=Id,count=counter,cursor=cur,stringify_ids=strid)
    Out2 = []
    for ids in Out["ids"]:
        Out2.append(ids)
    return Out2

# Fonction Raffle (pioche dans les rt et les follow)
# MAX 100 RT
# MAX 5000 follower
def Raffle(Lien,User):
    Id = Lien[Lien.rfind('/')+1:]
    RT = Get_retweetersID(int(Id),counter = 100,cur = -1,strid = "True")
    shuffle(RT)
    Follow = client.get_followers_ids(screen_name=User,stringify_ids="True")["ids"]
    Win = []
    for ids in RT:
        if ids in Follow:
            Win.append(ids)
            break
    Winner = client.lookup_user(user_id=Win[0])[0]["screen_name"]
    print("Le gagnat est @"+str(Winner))
    print("Lien : https://twitter.com/"+str(Winner))

# Fonction Stream
class TStream(TwythonStreamer):
    def on_success(self, data):
        if ('text' in data):
            if (data['in_reply_to_user_id'] == None) or (data["user"]["screen_name"] == "FirefoxyLeGibus") or ('retweeted_status' not in data):
                A = """
Nouveau tweeet de @"""+str(data["user"]["screen_name"])+""" :
"""+str(data['text'])+"""

Created at : """+data["created_at"]+"""

Link : https://twitter.com/"""+str(data["user"]["screen_name"])+"/statuses/"+str(data["id"])
                print(A)

    def on_error(self, status_code, content, headers):
        print("Oops an error has occured")
        print("ERROR :",status_code)
        for thing in content:
            print(thing)
        self.disconnect()
Streamer = TStream(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'],
                  creds["ACCESS_TOKEN"], creds["ACCESS_SECRET"])

# Fonction Stream mais en plus simple voila
def stream(**param):
    Streamer.statuses.filter(**param)
class Stream():
    def Follow(screen_name,**param):
        Id = client.show_user(screen_name=screen_name)["id"]
        stream(follow=Id,**param)
    def Track(track,**param):
        stream(track=track,**param)

