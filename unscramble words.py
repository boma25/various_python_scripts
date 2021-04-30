import random


found = []  # list of found letters
bagOfWords = ""  # contains all the words in the english dictionary
acceptedWords = []  # list of all the words that has been found

# wordlist can be found at https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt

with open('../wordlist.txt', 'r') as file:
    bagOfWords += file.read()


# function to generate an index to select text from

def generateIndex(text):
    index = random.randint(0, len(text)-1) if len(text) > 1 else 0
    for num in found:
        if num == index:
            return generateIndex(text)
    return index


# function to unscramble text

def unscramble(text, number):
    count = 0
    unscrambled = ""
    while count < len(text):
        index = generateIndex(text)
        unscrambled += text[index]
        found.append(index)
        count += 1
    if(unscrambled in bagOfWords):
        if(unscrambled in acceptedWords):
            acceptedWords.index(unscrambled)
        else:
            acceptedWords.append(unscrambled)
            print(unscrambled)
    found.clear()
    if number == 100:
        return
    return unscramble(text, number=number+1)


# main function

def main():
    word = input('enter the word you would like to unscramble: ')
    acceptedWords.append(word)
    unscramble(word, 0)


if __name__ == "__main__":
    main()
