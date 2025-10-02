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
