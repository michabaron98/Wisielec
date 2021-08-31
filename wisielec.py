from print_wisielec import Get_mistake_method as mist
import word_operation as wrd

#main page
def check_letter(letter, mistakes=0):
    if letter in wrd.word:    return letter, mistakes
    else: 
        mistakes+=1
        #mist.print_mistakes(mistakes)
        return letter, mistakes
def correct_letters(letters):
    correct_letters=[]
    for letter in letters:
        if letter in wrd.word: correct_letters.append(letter)
    return correct_letters
def play_game():
    quantity_of_mistakes=0
    letters=[]
    good_letters=[]
    wrd.get_word()
    cvd_word=wrd.covered_word(good_letters)
    while(cvd_word!=wrd.word):
        letter=wrd.get_letter()
        letter, quantity_of_mistakes=check_letter(letter,quantity_of_mistakes)
        letters.append(letter)
        good_letters=correct_letters(letters)
        wrd.clean_terminal()
        print("Entered letters {}".format(sorted(letters)))
        cvd_word=wrd.covered_word(good_letters)
        mist.print_mistakes(quantity_of_mistakes)
    
play_game()