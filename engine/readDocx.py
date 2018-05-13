import re
import json
import nltk
from nltk.corpus import stopwords
stopwords = set(nltk.corpus.stopwords.words('english'))

f = open("../whatsapp.txt", "r")
allMessages = {}
words = []
i = 0
regexp = re.compile(r'\d:\d\d \w\w')
for line in f.read().split("\n"):
    if regexp.search(line):
        if len(line.split(' - ')[1].split(':')) > 1 and line.split(' - ')[1].split(':')[1] != ' <Media omitted>':
            line = (line.encode('ascii', 'ignore')).decode("utf-8")
            print (type(line))
            message = {
                'sender': line.split(' - ')[1].split(':')[0],
                'text': line.split(' - ')[1].split(':')[1]
            }

            allMessages[i](message)
            i = i + 1
       




# fdist = nltk.FreqDist(words)
# print(fdist)

with open('data.json', 'w') as outfile:
    json.dump(allMessages, outfile)