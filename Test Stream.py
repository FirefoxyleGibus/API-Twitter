from twython import TwythonStreamer
import json

with open("twitter_credentials.json", "r") as file:
    creds = json.load(file)

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print(data['text'])

    def on_error(self, status_code, content, headers):
        print("Oops an error has occured")
        print("ERROR :",status_code,"("+str(content)+")")
        print()
        print(headers)
        self.disconnect()

client = MyStreamer(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'],
                        creds["ACCESS_TOKEN"], creds["ACCESS_SECRET"])
