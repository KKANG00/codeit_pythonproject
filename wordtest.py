"""
with open('data/vocabulary.txt', 'r', encoding='UTF8') as f:
    for line in f:
        l = line.split(" ")
        answer = input(l[0]+" ")
        if answer == l[1].strip():
            print("맞았습니다!")
        else:
            print("아쉽습니다. 정답은 "+l[1].strip()+"입니다.")
"""
import random
word_dict = {}
with open('data/vocabulary.txt', 'r', encoding='UTF8') as f:
    for line in f:
        word = line.split(" ")
        k = word[0]
        e = word[1].strip()

        word_dict[k] = e

wordlen = len(word_dict)

while True:
    wordnum = random.randint(0, wordlen - 1)
    word = list(word_dict.keys())[wordnum]
    user = input(word+" ")

    if user == "q":
        break

    if user == word_dict[word]:
        print("맞았습니다!")
    else:
        print("아쉽습니다. 정답은 "+word_dict[word]+"입니다.")
