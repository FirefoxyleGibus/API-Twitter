# Import the Twython class
from twython import Twython
import json


# Load credentials from json file
with open("twitter_credentials.json", "r") as file:
    creds = json.load(file)

# Instantiate an object
python_tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])

def Search_Tweet(query,Rtype = "recent",count = 10,lang = "all"):
    # Create our query
    query = {'q': str(query),
            'result_type': Rtype,
            'count': count,
            'lang': lang,
            }

    # Search tweets (Custom)
    Twt = []
    Var = 0
    for status in python_tweets.search(**query)['statuses']:
        Twt.append(list())
        Twt[Var].append(status['user']['screen_name'])
        Twt[Var].append(status['created_at'])
        Twt[Var].append(status['text'])
        Twt[Var].append(str(status['favorite_count']))
        Var+=1
    
    for Item in Twt:
            print(Item[0],":",Item[2],"("+Item[3]+")")
            print(Item[1])
            print()
