import re
import json
import nltk
from nltk.corpus import stopwords
stopwords = set(nltk.corpus.stopwords.words('english'))

f = open("../data/whatsapp.txt", "r")
allMessages = []
words = []

regexp = re.compile(r'\d:\d\d \w\w')
for line in f.read().split("\n"):
    if regexp.search(line):
        if len(line.split(' - ')[1].split(':')) > 1 and line.split(' - ')[1].split(':')[1] != ' <Media omitted>':
            re.sub(r'\W+', '', line)
            message = {
                'sender': line.split(' - ')[1].split(':')[0],
                'text': line.split(' - ')[1].split(':')[1]
            }
            allMessages.append(message)
            temp = []
            temp.append(nltk.word_tokenize(line.split(' - ')[1].split(':')[1]))
            print(temp)
            # temp = [word for word in temp if not word.isnumeric()]
            # temp = [word.lower() for word in words]
            # stemmer = nltk.stem.snowball.SnowballStemmer('english')
            # temp = [stemmer.stem(word) for word in temp]
            # temp = [word for word in temp if word not in all_stopwords]
            # for word in temp:
            #     words.append




# fdist = nltk.FreqDist(words)
# print(fdist)

# with open('data.json', 'w') as outfile:
#     json.dump(allMessages, outfile)