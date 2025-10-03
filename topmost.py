from lab import wordfreq
import urllib.request
import sys

def main(inp_file, art_file, printAmount):
    #Call everything[2]:

    if "http://" in sys.argv[2] or "https://" in sys.argv[2]:
        response = urllib.request.urlopen(sys.argv[2])
        lines = response.read().decode("utf8").splitlines()
        tokenized_words = wordfreq.tokenize(lines)
    else:
        with open(sys.argv[2], encoding="utf-8") as art_file:
            tokenized_words = wordfreq.tokenize(art_file)

    with open(sys.argv[1], encoding="utf-8") as inp_file:
        tokenized_stopWords = wordfreq.tokenize(inp_file)

    count_words = wordfreq.countWords(tokenized_words, tokenized_stopWords)
    wordfreq.printTopMost(count_words, printAmount)

if __name__=="__main__":
    main(sys.argv[1], sys.argv[2], int(sys.argv[3]))