print_turn=0
def turn_chose(): # fonction qui permet d'alterner entre le Joueur X et le joueur O
     global grille
     global print_turn
     if print_turn == "O":
          print_turn ="X"
     else:
          print_turn = "O"


def two_players():      #fonction qui demande a l'utilisateur la case qu'il souhaite
    global grille
    global print_turn
    new_value = int(input("Choisir la case: "))
    if grille[new_value] == " ":
            grille[new_value]= print_turn
    else: 
        print("choisissez une case vide")
        case()
        two_players()

def turn():
    global grille
    case()    #display de la grille 
    turn_chose() # changement de joueur
    two_players() # demande la case à jouer  
    case()
    victory() # verifie la victoire 
    turn()
turn()


        
        
    