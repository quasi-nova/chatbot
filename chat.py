import random,re,sys
from textblob import *

def startNewTopic():
	a = ["Did you ever wonder how lonely we are in this universe?",
		 "Ahh! I'm hungry",
		 "You speak well."]
	print a[int(random.random()*len(a))]
def say(s):
	print s

knowledge = [
	[[r'hi',
	  r'hi\s.*'],
		[lambda:say('How do you do?'),
		 lambda:say('Sup with you?'),
		 lambda:say('Hows yo life?'),]],
	[[r'good.*'],
		[startNewTopic,]],
	[[r'what.*'],
		[lambda:say('I don\'t know.'),]], 
	[[r'when.*'],
		[lambda:say('I don\'t exactly remember that.'),]],
	[[r'where.*'],
		[lambda:say('Somewhere near my farmhouse.'),]],
	[[r'who.*'],
		[lambda:say('Well, it wasn\'t me!'),]],
	[[r'bye.*'],
		[lambda:sys.exit(),]]
]

class UserInput(TextBlob):
	def response(self):
		str = self.string
		for i in knowledge:
			for j in i[0]:
				if re.match(j,str,re.M|re.I):
					return i[1][int(random.random()*len(i[1]))]

print "Hello there!"
ui = UserInput(raw_input())
while ui.string.lower():
	res = ui.response()
	if(res): res()
	else: print "I don't get you!"
	ui = UserInput(raw_input())
