import sys
import os
def readintweets(readdir, writedir):
	filelength = file_len(writedir)
	count = filelength 
	#y is yes, n is no u is unknown/undetermined
	with open(readdir, 'r') as inpt, open(writedir, 'a+') as outpt:
		#filelength = sum(1 for line in outpt)
		for number, line in enumerate(inpt):
			os.system('cls' if os.name == 'nt' else 'clear')
			
			
			if number < filelength:
				outpt.flush()
			else:
				count += 1
				print 'Tweet Number: ' + str(count) + '\n'
				username, tweet = line.split('\t')
				print tweet
				var = getinput()
				outpt.write(username.strip() + '\t'+tweet.strip() +'\t'+ var.strip() + '\n')
				outpt.flush()
				

def file_len(fname):
	try:
		num_lines = sum(1 for line in open(fname, 'r'))
	except IOError: 
		f = open(fname, 'a+')
		f.close()
		num_lines = 0
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
	readintweets('test.txt', 'outtest.txt')
