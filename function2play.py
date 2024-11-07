def turn_chose():
     global grille
     global print_turn
     if print_turn == "O":
          print_turn ="X"
     else:
          print_turn = "O"

def turn():
    global grille
    turn_chose()
    case()
    turn_chose()
    case()
       

def two_players():
    global grille
    global print_turn
    new_value = int(input("Choisir la case: "))
    if grille[new_value] == " ":
            grille[new_value]= print_turn
    else:
            print("choisissez une case vide svp")
    victory()
    