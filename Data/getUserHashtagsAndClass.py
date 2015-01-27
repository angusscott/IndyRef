from nltk.corpus import stopwords
import itertools
import json
import re
stop = stopwords.words('english')
stop.remove('no')
stop = stop + ['#indyref','rt']

def processClassifiedTweetsHashtags(usernames, usertweetsdir, writedir):
	with open(usernames, 'r') as inpt:
		for user in inpt:
			user = user.split('\t')
			user[0] = user[0].strip()
			user[1] = user[1].strip()
			user[2] = user[2].strip()
			try:
				with open(usertweetsdir + user[0] + '.txt') as statuses, open(writedir+user[2]+ '/'+ user[0]+'.txt', 'w') as outpt:
					for status in statuses:
						status = json.loads(status)
						hashtags = status[u'text']
						hashtags = ' '.join(re.findall(r'#[A-Za-z0-9]*', hashtags))
						outpt.write(hashtags.encode('utf-8').lower()+ ' ')
			except IOError:
				print 'Can\'t find user ' + user[0]	

def processClassifiedTweets(usernames, usertweetsdir, writedir):
	with open(usernames, 'r') as inpt:
		for user in inpt:
			user = user.split('\t')
			user[0] = user[0].strip()
			user[1] = user[1].strip()
			user[2] = user[2].strip()
			try:
				with open(usertweetsdir + user[0] + '.txt') as statuses, open(writedir+user[2]+ '/'+ user[0]+'.txt', 'w') as outpt:
					for status in statuses:
						status = json.loads(status)
						hashtags = status[u'text'].strip()
						outpt.write(hashtags.encode('utf-8').lower()+ ' ')
			except IOError:
				print 'Can\'t find user ' + user[0]	

if __name__ == '__main__':
	#processClassifiedTweetsHashtags('/Users/angusscott/University/4thyear/4th Year Project/Data/indyRef-tweets-18th-Sept-2014-classified.txt', '/Users/angusscott/University/4thyear/4th Year Project/Data/UsersTweets/', '/Users/angusscott/University/4thyear/4th Year Project/Data/UsersHashtags/')
	processClassifiedTweets('/Users/angusscott/University/4thyear/4th Year Project/Data/indyRef-tweets-18th-Sept-2014-classified.txt', '/Users/angusscott/University/4thyear/4th Year Project/Data/UsersTweets/', '/Users/angusscott/University/4thyear/4th Year Project/Data/UsersTweetsClass/')

