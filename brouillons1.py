import random

grille=[" "," "," "," "," "," "," "," "," "]

def case():                                               #grille avec support des variables dans le terminal
 
    long = 1
    larg = 1
    n=0
    global grille

    print("+" + ("-" * long + "+") * 4)

    for i in range(3):
        
        for k in range(3):
            print(( f"|{grille[n]}|"),end='')
            n+=1
        print (end="\n") 

    print("+" + ("-" * long + "+")*4)
def turn(verif):
    if verif == True:
        symbol="X"
    else:
        symbol = "O" 

case()


def minimax(plateau , profondeur , maximizing):
    if victory(plateau,"0"):
            return 1
    elif victory(plateau ,"x"):
        return -1
    elif victory(plateau):
        return 0


    if maximizing:
        meilleur_score = -float("inf")
        for i in range(9):
            if plateau[i] == " ":
                plateau[i] = "O"
                score = minimax(plateau, profondeur + 1, False)
                plateau[i] = " "
                meilleur_score = max(score, meilleur_score)
        return meilleur_score