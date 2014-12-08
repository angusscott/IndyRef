import sys
def readintweets(readdir, writedir):
	#y is yes, n is no u is unknown/undetermined
	filelength = file_len(writedir)

	with open(readdir, 'r') as inpt, open(writedir, 'a') as outpt:
		for number, line in enumerate(inpt):
			if number <= filelength:
				pass
			else:
				username, tweet = line.split('\t')
				print tweet
				var = getinput()
				outpt.write(username.strip() + '\t'+tweet.strip() +'\t'+ var.strip() + '\n')
				outpt.flush()

def file_len(fname):
    num_lines = sum(1 for line in open(fname))
    return num_lines

def getinput():
	allowableInput = ['y','n','u']
	while True:
		var = raw_input("Please classify as y, n or u: ")
		if var == 'q':
			sys.exit(0)
		elif var not in allowableInput:
			print 'Not allowable input'
		else:
			return var

if __name__ == '__main__':
	readintweets('/Users/angusscott/University/4thyear/4th Year Project/Data/indyRef-tweets-18th-Sept-2014-unique.txt', '/Users/angusscott/University/4thyear/4th Year Project/Data/indyRef-tweets-18th-Sept-2014-classified.txt')
