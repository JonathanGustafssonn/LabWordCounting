import sys
from counting_and_printing_test import printTopMost
from counting_and_printing_test import countWords
from wordfreq import tokenize

inp_file = open(sys.argv[1], encoding="utf-8")
art_file = open(sys.argv[2], encoding="utf-8")
printAmount = sys.argv[3]

def main(inp_file, art_file, printAmount):
    tokenized_words = tokenize(art_file)
    art_file.close()
    count_words = countWords(tokenized_words, inp_file)
    inp_file.close()
    printTopMost(count_words, printAmount)


main(inp_file, art_file, printAmount)
