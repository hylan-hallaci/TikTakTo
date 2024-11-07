grille=[" "," "," "," "," "," "," "," "," "]
print_turn=0

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
          
def turn_chooser():
    global print_turn
   
    if print_turn == "O":
        print_turn="X"      
    else:
        print_turn="O"
          
def victory():
    global grille
    if " " not in grille:
        print("fin de partie, égalité")
        return exit()
    elif (grille[0] == grille[1] == grille[2] and grille[0] != " ") or (grille[3] == grille[4] == grille[5] and grille[3] != " ") or (grille[6] == grille[7] == grille[8] and grille[6] != " "):
        print(f"victoire en ligne horizontale ! GG")
        return exit()
    elif (grille[0] == grille[3] == grille[6] and grille[0] != " ") or (grille[1] == grille[4] == grille[7] and grille[1] != " ") or (grille[2] == grille[5] == grille[8] and grille[2] != " "):
        print(f"victoire en ligne verticale ! GG")
        return exit()
    elif (grille[0] == grille[4] == grille[8] and grille[0] != " ") or (grille[2] == grille[4] == grille[6] and grille[2] != " "):
        print("victoire en diagonale ! GG")
        return exit()
    else:
        print("manche suivante")

def choose():       #demande la case qu'il souhaite
    global grille
    global print_turn
    select=(int(input("Joueur 1 choisissez une case")))
    if grille[select] ==" ":
        grille[select] = print_turn
    else: 
        print("choisissez une case vide")
        case()
        choose()

def turn():
    global print_turn
    global grille
    turn_chooser() #change turn each times
    case() #display
    choose()
        
    case() #display
    victory() #check victory
    turn()
turn()
    
    
        
    
        

         
        
        


    