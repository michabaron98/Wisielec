import string
import os
letters=list(string.ascii_lowercase)

#Operations
def clean_terminal():
    os.system('cls')
def get_word():
    global word
    buffor=0
    while(buffor==0):
        buffor=input("Enter word: ")
        buffor=check(buffor)
    clean_terminal()
    word=buffor.lower()
    print(word)
    #return word
def check(buffor_word):
    for letter in buffor_word:
        if not letter in letters:
            clean_terminal()
            print("Eneter correct input\nYou can use only this charaters: {}".format(letters))
            return 0
    return buffor_word
def covered_word(correct_letters):
    cvd_word=list()
    for i in word:
        if i in correct_letters: cvd_word.append(i)
        else: cvd_word.append("_ ")
    print("".join(cvd_word))
    return "".join(cvd_word)
def get_letter():
    buffor=0
    while(buffor==0):
        buffor=input("Enter letter: ")
        buffor=check(buffor)
    letter=buffor.lower()
    return letter[0]
