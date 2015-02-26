import re
import operator
import getAllTweets

def gettweets(readdir):
	with open(readdir, 'r') as inpt:
		for line in inpt:
			line = line.strip()
			username = line.split('\t')[0]
			getAllTweets.getAllTweets(username)
			print username
if __name__ == '__main__':
	#pass in the username of the account you want to download
	gettweets('/Users/angusscott/University/4thyear/4th Year Project/Data/indyRef-tweets-18th-Sept-2014-classified.txt')
