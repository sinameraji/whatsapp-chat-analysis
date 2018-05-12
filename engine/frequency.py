import re
import json
from pprint import pprint
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
 
stop_words = set(stopwords.words('english'))
stop_words_new = ['haha', 'https', 'hahaha', 'u', 'dr']
for s in stop_words_new:
    stop_words.add(s)

with open('../data/data-js.json') as f:
    data = json.load(f)


allText = ""
# pprint(data)
for key in data:
    text = data[key]['message']
    # text = ''.join(e for e in text if e.isalnum())
    text = re.sub(r'\W+', ' ', text)
    allText = allText + " "+ text


# print allText
word_tokens = word_tokenize(allText)
filtered_sentence = [w for w in word_tokens if not w in stop_words]
 
filtered_sentence = []
 
for w in word_tokens:
    w = w.lower()
    if w not in stop_words:
        filtered_sentence.append(w)
 
# print(word_tokens)
# print(filtered_sentence)
from nltk.probability import FreqDist
freq = FreqDist(filtered_sentence)
for w in freq.most_common(50):
    print ("word: " + w[0] + " frequency: " + str(w[1]))
    print("***")

freq.plot(10,cumulative=False)
