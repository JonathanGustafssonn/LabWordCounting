def tokenize(lines):
    '''
    Splits a provided text into a sequence of words(tokens)
    '''
    words = []

    for line in lines:
        start = 0

        while start < len(line):
            # Remove any whitespace
            while line[start].isspace():
                start += 1

            # Check type of character
            if line[start].isalpha():
                print(line[start], ' is a letter')

            elif line[start].isdigit():
                print(line[start], ' is a digit')

            elif not line[start].isalnum():
                print(line[start], ' is a symbol')
            
            # Move to next character
            start += 1

    return words
