import argparse
import tkinter.filedialog
from tkinter import *


def get_output_filename(input_file_name):
    """ replace the suffix of the file with .rst """
    return input_file_name.rpartition(".")[0] + ".rst"


def gui():
    """make the GUI version of this command that is run if no options are
    provided on the command line"""

    def button_go_callback():
        """ what to do when the "Go" button is pressed """
        input_file = entry.get()
        if input_file.rsplit(".")[-1] != "txt":
            statusText.set("Filename must end in `.txt'")
            message.configure(fg="red")
            return
        else:
            # input_file is the file path
            # print(input_file)
            mostFrequentWords(input_file)


    def button_browse_callback():
        """ What to do when the Browse button is pressed """
        filename = tkinter.filedialog.askopenfilename()
        entry.delete(0, END)
        entry.insert(0, filename)

    root = Tk()
    frame = Frame(root)
    frame.pack()

    statusText = StringVar(root)
    statusText.set("Press Browse button or enter .txt filename, "
                   "then press the Go button")

    label = Label(root, text="Whatsapp chat history: ")
    label.pack()
    entry = Entry(root, width=50)
    entry.pack()
    separator = Frame(root, height=2, bd=1, relief=SUNKEN)
    separator.pack(fill=X, padx=5, pady=5)

    button_go = Button(root,
                       text="Go",
                       command=button_go_callback)
    button_browse = Button(root,
                           text="Browse",
                           command=button_browse_callback)
    button_exit = Button(root,
                         text="Exit",
                         command=sys.exit)
    button_go.pack()
    button_browse.pack()
    button_exit.pack()

    separator = Frame(root, height=2, bd=1, relief=SUNKEN)
    separator.pack(fill=X, padx=5, pady=5)

    message = Label(root, textvariable=statusText)
    message.pack()

    mainloop()


def read_txt(filename):
    """ Read the txt file
    """
    f = open(filename,"r")
    return f.read()

def clean(filePath):
    import re
    import json
    import nltk
    from nltk.corpus import stopwords
    stopwords = set(nltk.corpus.stopwords.words('english'))

    f = open(filePath, "r")
    allMessages = {}
    words = []
    i = 0
    regexp = re.compile(r'\d:\d\d \w\w')
    for line in f.read().split("\n"):
        if regexp.search(line):
            if len(line.split(' - ')[1].split(':')) > 1 and line.split(' - ')[1].split(':')[1] != ' <Media omitted>':
                line = (line.encode('ascii', 'ignore')).decode("utf-8")
                message = {
                    'sender': line.split(' - ')[1].split(':')[0],
                    'text': line.split(' - ')[1].split(':')[1]
                }
                allMessages[i] = message
                i = i + 1

    with open('new.json', 'w') as outfile:
        json.dump(allMessages, outfile)
    
def mostFrequentWords(filePath):
    import re
    import json
    import nltk
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    
    clean(filePath)
    stop_words = set(stopwords.words('english'))
    stop_words_new = ['haha', 'https', 'hahaha', 'u', 'btw','dr', 'pm', 'am', 'like','lol','one','na','yeah', "a","a's","able","about","above","according","accordingly","across","actually","after","afterwards","again","against","ain't","all","allow","allows","almost","alone","along","already","also","although","always","am","among","amongst","an","and","another","any","anybody","anyhow","anyone","anything","anyway","anyways","anywhere","apart","appear","appreciate","appropriate","are","aren't","around","as","aside","ask","asking","associated","at","available","away","awfully","b","be","became","because","become","becomes","becoming","been","before","beforehand","behind","being","believe","below","beside","besides","best","better","between","beyond","both","brief","but","by","c","c'mon","c's","came","can","can't","cannot","cant","cause","causes","certain","certainly","changes","clearly","co","com","come","comes","concerning","consequently","consider","considering","contain","containing","contains","corresponding","could","couldn't","course","currently","d","definitely","described","despite","did","didn't","different","do","does","doesn't","doing","don't","done","down","downwards","during","e","each","edu","eg","eight","either","else","elsewhere","enough","entirely","especially","et","etc","even","ever","every","everybody","everyone","everything","everywhere","ex","exactly","example","except","f","far","few","fifth","first","five","followed","following","follows","for","former","formerly","forth","four","from","further","furthermore","g","get","gets","getting","given","gives","go","goes","going","gone","got","gotten","greetings","h","had","hadn't","happens","hardly","has","hasn't","have","haven't","having","he","he's","hello","help","hence","her","here","here's","hereafter","hereby","herein","hereupon","hers","herself","hi","him","himself","his","hither","hopefully","how","howbeit","however","i","i'd","i'll","i'm","i've","ie","if","ignored","immediate","in","inasmuch","inc","indeed","indicate","indicated","indicates","inner","insofar","instead","into","inward","is","isn't","it","it'd","it'll","it's","its","itself","j","just","k","keep","keeps","kept","know","knows","known","l","last","lately","later","latter","latterly","least","less","lest","let","let's","like","liked","likely","little","look","looking","looks","ltd","m","mainly","many","may","maybe","me","mean","meanwhile","merely","might","more","moreover","most","mostly","much","must","my","myself","n","name","namely","nd","near","nearly","necessary","need","needs","neither","never","nevertheless","new","next","nine","no","nobody","non","none","noone","nor","normally","not","nothing","novel","now","nowhere","o","obviously","of","off","often","oh","ok","okay","old","on","once","one","ones","only","onto","or","other","others","otherwise","ought","our","ours","ourselves","out","outside","over","overall","own","p","particular","particularly","per","perhaps","placed","please","plus","possible","presumably","probably","provides","q","que","quite","qv","r","rather","rd","re","really","reasonably","regarding","regardless","regards","relatively","respectively","right","s","said","same","saw","say","saying","says","second","secondly","see","seeing","seem","seemed","seeming","seems","seen","self","selves","sensible","sent","serious","seriously","seven","several","shall","she","should","shouldn't","since","six","so","some","somebody","somehow","someone","something","sometime","sometimes","somewhat","somewhere","soon","sorry","specified","specify","specifying","still","sub","such","sup","sure","t","t's","take","taken","tell","tends","th","than","thank","thanks","thanx","that","that's","thats","the","their","theirs","them","themselves","then","thence","there","there's","thereafter","thereby","therefore","therein","theres","thereupon","these","they","they'd","they'll","they're","they've","think","third","this","thorough","thoroughly","those","though","three","through","throughout","thru","thus","to","together","too","took","toward","towards","tried","tries","truly","try","trying","twice","two","u","un","under","unfortunately","unless","unlikely","until","unto","up","upon","us","use","used","useful","uses","using","usually","uucp","v","value","various","very","via","viz","vs","w","want","wants","was","wasn't","way","we","we'd","we'll","we're","we've","welcome","well","went","were","weren't","what","what's","whatever","when","whence","whenever","where","where's","whereafter","whereas","whereby","wherein","whereupon","wherever","whether","which","while","whither","who","who's","whoever","whole","whom","whose","why","will","willing","wish","with","within","without","won't","wonder","would","would","wouldn't","x","y","yes","yet","you","you'd","you'll","you're","you've","your","yours","yourself","yourselves","z","zero","a",",",".","?","!","|",":","'",";","<NUM>","?","$","km","s","u","&","#","'s","/","dr."]
    for s in stop_words_new:
        stop_words.add(s)

    with open('new.json') as f:
        data = json.load(f)

    allText = ""

    for key in data:
        text = data[key]['text']
        text = re.sub(r'\W+', ' ', text)
        line = re.sub(r"(^|\W)\d+", "", text)
        allText = allText + " "+ text

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
    for w in freq.most_common(10):
        print ("word: " + w[0] + " frequency: " + str(w[1]))
        print("***")

    freq.plot(10,cumulative=False)

if __name__ == "__main__":
    """ Run as a stand-alone script """


    gui()