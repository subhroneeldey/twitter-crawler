from __future__ import unicode_literals
import tweepy,sys
#get your consumer key and access key from https://dev.twitter.com/
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

#file input as command to write them in the file
fil=sys.argv[1]
data ={}
class MyStreamListener(tweepy.StreamListener):
    i=1
    def on_status(self, status):
        try:    
            oFile = open(fil,"a")
            data['name'] = status.user.name
            #data['screen_name'] = status.user.screen_name optional
            data['location'] = status.user.location
            data['text'] = status.text
            data['created_at'] = status.created_at 
            #data['geo'] = status.coordinates optional
            #data['source'] = status.source optional
            s=str(MyStreamListener.i)
            data_location = str(data['location'])
            data_text = str(data['text']).encode('utf-16', 'ignore').decode('utf-16','ignore')
            data_time = str(data['created_at'])
            if "Houston" in data_text and "flood" in data_text:
                oFile.write(data_text+">>>>"+data_location+">>>>"+data_time+">>>>"+s+"\n")
                MyStreamListener.i +=1

        except:
            pass
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track=['Houston' and 'flood'])
oFile=open(fil)
oFile.close()
