def countWords(words, stopWords):
    """
    Räknar förekomsten av ord i listan 'words', men ignorerar ord som finns i 'stopWords'.
    Returnerar en ordbok {ord: frekvens}.
    """
    frequencies = {}
    for word in words:
        if word in stopWords:
            continue
        elif word not in frequencies:
            frequencies[word] = 1
        else:
            frequencies[word] += 1
    return frequencies

def printTopMost(frequencies, n):
    """
    Skriver ut de n mest frekventa orden ur ordboken 'frequencies'.
    Orden vänsterjusteras i en kolumn på 20 tecken,
    och frekvenserna högerjusteras i en kolumn på 5 tecken.
    """
    # Sortera först på frekvens (fallande), sedan alfabetiskt för stabil ordning
    sorted_items = sorted(frequencies.items(), key=lambda x: (-x[1], x[0]))

    # Skriv bara ut de n första
    for word, freq in sorted_items[:n]:
        print(word.ljust(20), str(freq).rjust(5))


if __name__ == "__main__":
    """
    Exempeltest: demonstrerar funktionerna med en liten lista av ord.
    """
    words = ['it','is','a','book','book','text','word','word','word']
    stopWords = ['a','is','it']

    freqs = countWords(words, stopWords)
    print("Räknade frekvenser:", freqs)

    print("\nTopp 3 ord:")
    printTopMost(freqs, 3)
