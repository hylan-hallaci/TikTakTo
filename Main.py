print_turn=0
kg=0
grille=[" "," "," "," "," "," "," "," "," "]
def turn_chose(): # fonction qui permet d'alterner entre le Joueur X et le joueur O
     global grille
     global print_turn
     if print_turn == "O":
          print_turn ="X"
     else:
          print_turn = "O"

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
          
def victory():
    global grille
    if " " not in grille:
        print("fin de partie, égalité")
        case()
        return exit()
    elif (grille[0] == grille[1] == grille[2] and grille[0] != " ") or (grille[3] == grille[4] == grille[5] and grille[3] != " ") or (grille[6] == grille[7] == grille[8] and grille[6] != " "):
        print(f"victoire en ligne horizontale ! GG")
        case()
        return exit()
    elif (grille[0] == grille[3] == grille[6] and grille[0] != " ") or (grille[1] == grille[4] == grille[7] and grille[1] != " ") or (grille[2] == grille[5] == grille[8] and grille[2] != " "):
        print(f"victoire en ligne verticale ! GG")
        case()
        return exit()
    elif (grille[0] == grille[4] == grille[8] and grille[0] != " ") or (grille[2] == grille[4] == grille[6] and grille[2] != " "):
        print("victoire en diagonale ! GG")
        case()
        return exit()
    else:
        print("manche suivante")

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
def minimax(plateau, profondeur, is_maximizing):
    

    if is_maximizing:
        meilleur_score = -float("inf")
        for i in range(9):
            if plateau[i] == " ":
                plateau[i] = "O"
                score = minimax(plateau, profondeur + 1, False)
                plateau[i] = " "
                meilleur_score = max(score, meilleur_score)
        return meilleur_score
    else:
        meilleur_score = float("inf")
        for i in range(9):
            if plateau[i] == " ":
                plateau[i] = "X"
                score = minimax(plateau, profondeur + 1, True)
                plateau[i] = " "
                meilleur_score = min(score, meilleur_score)
        return meilleur_score

def meilleur_mouvement(plateau):
    meilleur_score = -float("inf")
    coup = -1
    for i in range(9):
        if plateau[i] == " ":
            plateau[i] = "O"
            score = minimax(plateau, 0, False)
            plateau[i] = " "
            if score > meilleur_score:
                meilleur_score = score
                coup = i
    return coup

# Tour du joueur
def player_turn():
    global grille
    coup = int(input("Entrez le numéro de case (0-8) pour placer votre X: "))
    if grille[coup] == " ":
        grille[coup] = "X"
    else:
        print("Case déjà prise. Choisissez une autre case.")
        player_turn()

# Tour de l'IA
def ia_turn():
    global grille
    coup = meilleur_mouvement(grille)
    grille[coup] = "O"
    print("L'IA a joué dans la case", coup)

# Boucle principale du jeu
def jeu():
    tour_joueur = True  # Le joueur commence
    while kg<2 :
        case()
        if tour_joueur:
            player_turn()
            victory()
                
        else:
            ia_turn()
            victory()
        
        tour_joueur = not tour_joueur
        
        
def turn():
    global grille
    case()    #display de la grille 
    turn_chose() # changement de joueur
    two_players() # demande la case à jouer  
    case()
    victory() # verifie la victoire 
    turn()

def start():
    i=int(input("Jouer à deux ou contre une ia impossible à battre ? \n 1 contre l'IA \n 2 contre un autre joueur \n Choix :    "))
    if i == 1:
        jeu()
    elif i == 2:
        turn()
    else:
        print("choisis 1 ou 2 ")
        start()
start()
    