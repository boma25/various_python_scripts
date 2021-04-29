import random

# list of selected letters
found = []

# function to generate an index to select text from


def generateIndex(text):
    index = random.randint(0, len(text)-1)
    for num in found:
        if num == index:
            return generateIndex(text)
    return index

# function to scramble text


def scramble(text):
    count = 0
    scrambled = ""
    while count < len(text):
        index = generateIndex(text)
        scrambled += text[index]
        found.append(index)
        count += 1
    return print(scrambled)

# main function


def main():
    text = input('input the text you wish to scramble: ')
    scramble(text)


if __name__ == "__main__":
    main()
