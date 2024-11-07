def two_players(symbol):
    CA=int(input("Quelle case voulez vous jouer ?"))
    if symbol == True :
        symbol="X"
        if CA == 1 and grille[0] == " ":
            grille[0]= "X"
        elif CA == 2 and grille[1]==" ":
            grille[1]= "X"
        elif CA== 3 and grille[2] == " ":
            grille[2]="X"
        elif CA== 4 and grille[3] ==" ":
            grille[3]="X"
        elif CA==5 and grille[4]==" ":
            grille[4]="X"
        elif CA==6 and grille[5]==" ":
            grille[5]="X"
        elif CA==7 and grille[6]==" ":
            grille[6]="X"
        elif CA==8 and grille[7]==" ":
            grille[7]="X"
        elif CA==9 and grille[8]==" ":
            grille[8]="X"
        else:
            print("choisissez une case vide svp")
    else:
        symbol = "O" 
        if CA == 1 and grille[0] == " ":
            grille[0]= "O"
        elif CA == 2 and grille[1]==" ":
            grille[1]= "O"
        elif CA== 3 and grille[2] == " ":
            grille[2]="O"
        elif CA== 4 and grille[3] ==" ":
            grille[3]="O"
        elif CA==5 and grille[4]==" ":
            grille[4]="O"
        elif CA==6 and grille[5]==" ":
            grille[5]="O"
        elif CA==7 and grille[6]==" ":
            grille[6]="O"
        elif CA==8 and grille[7]==" ":
            grille[7]="O"
        elif CA==9 and grille[8]==" ":
            grille[8]="O"
        else:
            print("choisissez une case vide svp")
two_players(symbol = "X" or "O")