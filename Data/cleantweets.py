import re
import operator

def gettweets(readdir, writedir):
	with open(readdir, 'r') as inpt, open(writedir, 'w') as outpt:
		for line in inpt:
			if not re.match('^#', line):
				outpt.write(line)

def gethashtags(readdir, writedir):
	with open(readdir, 'r') as inpt, open(writedir, 'w') as outpt:
		for line in inpt:
			if re.match('^#', line):
				outpt.write(line)

def gethashtagscounts(readdir, writedir):
	with open(readdir, 'r') as inpt, open(writedir, 'w') as outpt:
		dic = {}
		for line in inpt:
			match = re.match('^#[\w]+', line).group()
			print str(match)
			if match is not None:
				if match in dic:
					dic[match] +=1
				else:
					dic[match] = 1
		else:
			print "No match on " + line
		sorted_x = sorted(dic.items(), key=operator.itemgetter(1), reverse = True)

		for (key, value) in sorted_x:
			outpt.write(str(key) + ': ' + str(value) + '\n') 

def getusertweetcounts(readdir, writedir):
	with open(readdir, 'r') as inpt, open(writedir, 'w') as outpt:
		dic = {}
		for line in inpt:
			match = re.match('^[\w]+', line).group()
			print str(match)
			if match is not None:
				if match in dic:
					dic[match] +=1
				else:
					dic[match] = 1
		else:
			print "No match on " + line
		sorted_x = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
		for (key, value) in sorted_x:
			outpt.write(str(key) + ': ' + str(value) + '\n') 

def seperatetweetsbydate(readdir, writedir):
	with open(readdir, 'r') as inpt, open(writedir, 'w') as outpt:
		for line in inpt:
			username, time, tweet = line.split('\t')[:3]
			if int(time) >1410998400 and int(time) < 1411084800:
				outpt.write(username + '\t' + tweet + '\n')

if __name__ == '__main__':
	gettweets('/Users/angusscott/University/4thyear/4th Year Project/Data/indyRef-tweets.txt','/Users/angusscott/University/4thyear/4th Year Project/Data/indyRef-tweets-tweets.txt')
	gethashtags('/Users/angusscott/University/4thyear/4th Year Project/Data/indyRef-tweets.txt','/Users/angusscott/University/4thyear/4th Year Project/Data/indyRef-tweets-hashtags.txt')
	gethashtagscounts('/Users/angusscott/University/4thyear/4th Year Project/Data/indyRef-tweets-hashtags.txt','/Users/angusscott/University/4thyear/4th Year Project/Data/indyRef-tweets-hashtags-counts.txt')
	getusertweetcounts('/Users/angusscott/University/4thyear/4th Year Project/Data/indyRef-tweets-tweets.txt','/Users/angusscott/University/4thyear/4th Year Project/Data/indyRef-tweets-usertweet-counts.txt')
	seperatetweetsbydate('/Users/angusscott/University/4thyear/4th Year Project/Data/indyRef-tweets-tweets.txt','/Users/angusscott/University/4thyear/4th Year Project/Data/indyRef-tweets-18th-Sept-2014.txt')
