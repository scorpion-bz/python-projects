import random
from animals import animals
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit
from PyQt5.QtGui import QFont
from PyQt5.uic import loadUi


def hangman():
    def reset():
        nonlocal word, guess, tries, trylist
        word = random.choice(animals)
        guess = "-" * len(word)
        tries = 6
        trylist = []
        lblGuess.setText(guess)
        lblTries.setText(str(tries))
        lblTrylist.setText("")
        window.result.setText("")
        txtGuess.setFocus(True)
        btnSubmit.setEnabled(True)

    word = random.choice(animals)
    guess = "-" * len(word)
    tries = 6
    trylist = []

    app = QApplication([])
    window = loadUi("/home/scorpion/python/gui/hangman/hangman.ui")
    window.show()
    window.setWindowTitle("Hangman Game")
    window.guess.setText(guess)
    lblGuess = window.guess
    lblTries = window.tries
    lblTrylist = window.sl
    txtGuess = window.c
    btnSubmit = window.submit

    def handle_submit():
        nonlocal guess, tries
        c = txtGuess.text()
        txtGuess.clear()
        if len(c) != 1:
            window.result.setText("Enter one character only.")
        elif c in trylist:
            window.result.setText("Already suggested, try another.")
        elif not c.isalpha():
            window.result.setText("Try a valid Character.")
        else:
            trylist.append(c)
            lblTrylist.setText(" | ".join(trylist))
            if word.upper().find(c.upper()) != -1:
                guess = change(word, guess, c)
                lblGuess.setText(guess)
                window.result.setText(f"Right!")
                if guess == word:
                    window.result.setText("Congrats! You guessed it right.")
                    btnSubmit.setEnabled(False)
            else:
                tries -= 1
                window.result.setText(f"Wrong!")
                if tries == 0:
                    window.result.setText(f"You Lost! The correct word was {word}.")
                    btnSubmit.setEnabled(False)
            window.tries.setText(str(tries))
            txtGuess.setFocus(True)

    btnSubmit.clicked.connect(handle_submit)
    window.reset.clicked.connect(reset)
    window.show()
    app.exec_()


def change(word, ch, letter):
    for i in range(len(word)):
        if word[i].upper() == letter.upper():
            ch = ch[:i] + word[i] + ch[i + 1 :]
    return ch


hangman()
