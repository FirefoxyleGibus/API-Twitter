from twython import Twython
import json

with open("twitter_credentials.json", "r") as file:
    creds = json.load(file)

client = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'],
                        creds["ACCESS_TOKEN"], creds["ACCESS_SECRET"])

User = client.get_account_settings()

def Post(text):
    post = client.update_status(status=text)
    print("Lien du tweet")
    print("https://twitter.com/"+str(User["screen_name"])+"/statuses/"+str(post["id"]))

def Photo_Post(path,text):
    photo = open(path, 'rb')
    response = client.upload_media(media=photo)
    post = client.update_status(status=text, media_ids=[response['media_id']])
    print("Lien du tweet")
    print("https://twitter.com/"+str(User["screen_name"])+"/statuses/"+str(post["id"]))

def Video_Post(path,text):
    video = open(path, "rb")
    response = client.upload_video(media=video, media_type="video/mp4")
    post = client.update_status(status=text, media_ids=[response['media_id']])
    print("Lien du tweet")
    print("https://twitter.com/"+str(User["screen_name"])+"/statuses/"+str(post["id"]))
