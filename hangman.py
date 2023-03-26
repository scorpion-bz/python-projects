import random


def hangman():
    animals = ["Dog","Cow","Cat","Horse","Donkey","Tiger","Lion","Panther","Cheetah","Bear","Elephant","Turtle","Crocodile","Rabbit","Pigeon","Crow","Fish","Dolphin","Frog","Whale","Alligator","Wolf","Bird","Hamster","Lizard","Snake","Mouse","Rat","Parrot","Goldfish",]
    word = random.choice(animals)
    guess = "-" * len(word)
    tries = 7
    trylist = []
    while guess != word and tries >= 1:
        print("\033[32m" + guess + "\033[37m")
        c = input("suggest a character :    ")
        while len(c) != 1 or c in trylist:
            if len(c) != 1:
                print("enter one caracter only :  ")
            else:
                print("already suggested, try another :   ")
            c = input()
        trylist.append(c)
        print(f"list of suggestions : {' | '.join(trylist)}")
        if word.upper().find(c.upper()) != -1:
            guess = change(word, guess, c)
        else:
            tries -= 1
            print(f"wrong, you have {tries} trie(s) left")
    if guess == word:
        print("\033[35m" + "Congrats! : " + "\033[36m", word)
    else:
        print("\033[91m" + "You Lost, the correct suggestion was " + "\033[36m", word)


def change(word, ch, letter):
    for i in range(len(word)):
        if word[i].upper() == letter.upper():
            ch = ch[:i] + word[i] + ch[i + 1 :]
    return ch


hangman()
