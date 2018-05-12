# Find the most frequent words in your WhatsApp conversations

In ```run.py``` line 104 I'm running my clean.js file, because I had a problem with string encoding and data cleaning in python. it was injecting these weird ```\u1234``` stuff and I found it easier to just redo the whole thing in Nodejs rather than trying to fix the encoding in Python. I'm a simple man.

## Dependencies
* Python 2.7 
* Nodejs (any respectable version)

## How to use
1. export conversation history from WhatsApp (you can email it to yourself)
2. Run ```python run.py```
3. Browse and hit Go


> Note: make sure there are no spaces in the filename. i'm too lazy to handle that