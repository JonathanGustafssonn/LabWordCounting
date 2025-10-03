def tokenize(lines):
    '''
    Splits a provided text into a sequence of words(tokens)
    
    takes a list of tokens as an arg

    Returns a list of words from provided text
    '''
    words = []

    for line in lines:
        start = 0
        length = len(line)
        while start < length:
            # Remove any whitespace
            while start < length and line[start].isspace():
                start += 1
            if start >= length:
                break

            # Handle alphabetical tokens
            if line[start].isalpha():
                end = start
                while end < length and line[end].isalpha():
                    end += 1
                words.append(line[start:end].lower())
                start = end

            #Handle digit tokens
            elif line[start].isdigit():
                end = start
                while end < length and line[end].isdigit():
                    end += 1
                words.append(line[start:end])
                start = end

            #Handle other tokens (single character)
            else:
                words.append(line[start])
                start += 1

    return words

def countWords(words, stopWords):
    '''
    Counts the occurrence of words in the list 'words', but ignores words that are in 'stopWords'.
    Returns a dictionary {word: frequency}.
    '''

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
    '''
    Prints the n most frequent words from the dictionary
    'frequencies'. The words are left-aligned in a column
    of 20 characters, and the frequencies are right-aligned
    in a column of 5 characters.
    '''
    # First sort by frequency (descending), then alphabetically for stable ordering
    sorted_items = sorted(frequencies.items(), key=lambda x: (-x[1], x[0]))

    # Only print the first 'n' words
    for word, freq in sorted_items[:n]:
        print(word.ljust(20) + str(freq).rjust(5))





