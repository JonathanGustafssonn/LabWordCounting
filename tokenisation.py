'''Tar bort alla symboler/ord i eng_stopwords.txt från artikeln man väljer'''

article = "article1.txt"

def removeSymbols(article):
    with open(article, "r", encoding="utf-8") as file:
        content = file.read().replace("\n", "").lower() # läser hela artikeln som man skriver i article-variabeln och gör den till små bokstäver för att vara i samma format som eng_stopwords.txt
        with open("eng_stopwords.txt", "r", encoding="utf-8") as symbol_file:
            symbols_content = symbol_file.read().replace("\n", "") # tar bort alla nya rader från eng_stopwords.txt
            symbols = list(symbols_content[:35]) # tar de första 35 karaktärerna från eng_stopwords.txt (de som är symboler)
            for symbol in symbols:
                content = content.replace(symbol, " ") # loopar genom alla symboler i artikeln och ersätter de med mellanrum 
            removed_symbols = content.split() 
            
    return removed_symbols

def removeUnwantedWords():
    removed_symbols = removeSymbols(article) # får texten utan symboler från removeSymbols funktionen
    with open("eng_stopwords.txt", "r", encoding="utf-8") as file:
        content = file.read().splitlines()
        unwanted_words = list(content[35:]) # den här gången tar man de karaktärer/ord som är efter 35 (siffror och ord)
        wanted_words = []
        for word in removed_symbols: 
            if word not in unwanted_words:
                wanted_words.append(word) # loopar igenom alla ord i texten (som nu inte har symboler) och lägger till dem som inte finns i unwanted_words i wanted_words

    return wanted_words

print(removeUnwantedWords())