# -*- coding: utf-8 -*-
import json
import pickle
import string
import csv

def main(filename):
    # read file into lines
    lines = open('F:\Files\台湾\学术 我要学术\Python\homework\i_have_a_dream.txt').readlines()

    # declare a word list
    all_words = []

    # extract all words from lines
    for line in lines:
        # split a line of text into a list words
        # "I have a dream." => ["I", "have", "a", "dream."]
        line = line.strip()
        words = line.split()

        # check the format of words and append it to "all_words" list
        for word in words:
            # then, remove (strip) unwanted punctuations from every word
            # "dream." => "dream"
            word = word.strip(string.punctuation)
            # check if word is not empty
            if word:
                # append the word to "all_words" list
                all_words.append(word)

    # compute word count from all_words
    from collections import Counter
    wordcount = Counter(all_words)

    # dump to a csv file named "wordcount.csv":
    # word,count
    # a,12345
    # I,23456
    # ...
    with open('counter.csv','w',newline='') as csv_file:
        # create a csv writer from a file object (or descriptor)
        writer = csv.writer(csv_file)
        # write table head
        writer.writerow(['word', 'count'])
        # write all (word, count) pair into the csv writer
        new_wordcount=dict(wordcount)
        for word,count in new_wordcount.items():
            writer.writerow([word, count])

    # dump to a json file named "wordcount.json"
    json.dump(wordcount,open('counter.json','w'))

    # BONUS: dump to a pickle file named "wordcount.pkl"
    pickle.dump(wordcount.most_common,open('counter.pickle','wb'))
    # hint: dump the Counter object directly


if __name__ == '__main__':
    main("i_have_a_dream.txt")
