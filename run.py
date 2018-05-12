import argparse
import csv
import tkFileDialog
from Tkinter import *
from Naked.toolshed.shell import execute_js


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
            mostFrequentWords(input_file)


    def button_browse_callback():
        """ What to do when the Browse button is pressed """
        filename = tkFileDialog.askopenfilename()
        entry.delete(0, END)
        entry.insert(0, filename)

    root = Tk()
    frame = Frame(root)
    frame.pack()

    statusText = StringVar(root)
    statusText.set("Press Browse button or enter CSV filename, "
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




def command_line(args):
    """ Run the command-line version
    """
    if args.output is None:
        args.output = get_output_filename(args.input)

    table_contents = read_txt(args.input)

    if write_table(args.output, table_contents):
        print "rst table is in file `{}'".format(args.output)
    else:
        print "Writing file `{}' did not succeed.".format(args.output)


def read_txt(filename):
    """ Read the txt file
    """
    f = open(filename,"r")
    return f.read()


def mostFrequentWords(filePath):
    import re
    import json
    import nltk
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    import subprocess
    
    # data = read_txt(filename)
    subprocess.call('node clean.js ' + filePath, shell=True)
    stop_words = set(stopwords.words('english'))
    stop_words_new = ['haha', 'https', 'hahaha', 'u', 'dr', 'pm', 'am']
    for s in stop_words_new:
        stop_words.add(s)

    with open('new.json') as f:
        data = json.load(f)

    allText = ""

    for key in data:
        text = data[key]['message']
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