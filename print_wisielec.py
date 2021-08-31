import os

#Displaing wisielec

class Mistake():
    def zero_mistake():
        print("No mistakes. Congratulations!")
    def first_mistake():
        #clear()
        print(' /')
    def second_mistake():
        #clear()
        print(" / \\")
    def thrid_mistake():
        print("  |")
        Mistake.second_mistake()
    def fourth_mistake():
        print(" _")
        Mistake.thrid_mistake()
    def fifth_mistake():
        print(" _ _")
        Mistake.thrid_mistake()
    def sixth_mistake():
        print(" _|_")
        Mistake.thrid_mistake()
    def seventh_mistake():
        print("  0")
        Mistake.sixth_mistake()
    def eighth_mistake():
        print("  |")
        Mistake.seventh_mistake()
    def ninth_mistake():
        print('!!! GAME OVER !!!')
        print("\\\ //")
        Mistake.eighth_mistake()
        exit()
    def clean_terminal():
        os.system('cls')
class Get_mistake_method(Mistake):
    def print_mistakes(qty):
        if qty==0: Mistake.zero_mistake()
        elif qty==1:Mistake.first_mistake()
        elif qty==2:Mistake.second_mistake()
        elif qty==3:Mistake.thrid_mistake()
        elif qty==4:Mistake.fourth_mistake()
        elif qty==5:Mistake.fifth_mistake()
        elif qty==6:Mistake.sixth_mistake()
        elif qty==7:Mistake.seventh_mistake()
        elif qty==8:Mistake.eighth_mistake()
        elif qty==9:Mistake.ninth_mistake()
        else: print("ERROR")