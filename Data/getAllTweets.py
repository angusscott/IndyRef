import tweepy
import datetime
import os.path
import time 
import os
import json

consumer_key = 'bu1ycAmiJKaTTksHe9a4JDCOk'
consumer_secret = 'socCx40HGIXc0XHSB21QGgC4KuxKzpKcsIfDihU0ZbglIjGClC'
access_key = '2397795404-gETgGpC7blNhAcaUBfIPsSzfGgTNRVLdpyo8wuy'
access_secret = '940OruTlEcPNdboz0qVxVLe9RWetBRGU037iP4NtFmjLB'

def getAllTweets(user):
	userdirectory = '/Users/angusscott/University/4thyear/4th Year Project/Data/UsersTweets/'+ user + '.txt'
	if os.path.isfile(userdirectory) == False:
	
		#authorize twitter, initialize tweepy
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_key, access_secret)
		api = tweepy.API(auth)

		#initialize a list to hold all the tweepy Tweets
		alltweets = []	
		try:
			#make initial request for most recent tweets (200 is the maximum allowed count)
			new_tweets = api.user_timeline(screen_name = user,count=200)

			#save most recent tweets
			alltweets.extend(new_tweets)
			
			#save the id of the oldest tweet less one
			oldest = alltweets[-1].id - 1
			
			#keep grabbing tweets until there are no tweets left to grab
			while len(new_tweets) > 0:
				print "getting tweets before %s" % (oldest)
				
				#all subsiquent requests use the max_id param to prevent duplicates
				new_tweets = api.user_timeline(screen_name = user,count=200,max_id=oldest)
				
				#save most recent tweets
				alltweets.extend(new_tweets)
				
				#update the id of the oldest tweet less one
				oldest = alltweets[-1].id - 1
				
				print "...%s tweets downloaded so far" % (len(alltweets))

			with open('/Users/angusscott/University/4thyear/4th Year Project/Data/UsersTweets/'+ user + '.txt', 'a+') as outpt:	
				for numb,tweet in enumerate(alltweets):
					print tweet
					date = tweet.created_at 
					if date > datetime.datetime(2014, 2, 1, 0, 0, 0) and date < datetime.datetime(2014, 9, 18, 0, 0, 0):
						outpt.write(json.dumps(tweet._json) + '\n')

		except tweepy.TweepError as e:
			print e.message
			if e.message == 'Not authorized.':
				pass
			elif e.message == [{u'message': u'Rate limit exceeded', u'code': 88}]:
				print "Start : %s" % time.ctime()
				try:
					os.remove('/Users/angusscott/University/4thyear/4th Year Project/Data/UsersTweets/'+ user + '.txt')
				except:
					pass
				time.sleep(930)
				print "End : %s" % time.ctime()
			else:
				pass
	return user

# if __name__ == '__main__':
# 	#pass in the username of the account you want to download
# 	getAllTweets("niamhcanttweet")