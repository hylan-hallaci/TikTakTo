# Grille 
grille = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
print_turn = "X"  # Le joueur 1 commence avec "X"

#affichage de la grille 
def case():
    n = 0
    global grille
    print("+" + ("-" * 3 + "+") * 3)
    for i in range(3):
        for k in range(3):
            print(f"| {grille[n]} ", end="")
            n += 1
        print("|")
        print("+" + ("-" * 3 + "+") * 3)





def victory():
    global grille
    #  lignes horizontales
    if (grille[0] == grille[1] == grille[2] and grille[0] != " ") or \
       (grille[3] == grille[4] == grille[5] and grille[3] != " ") or \
       (grille[6] == grille[7] == grille[8] and grille[6] != " "):
        return True
    #  lignes verticales
    if (grille[0] == grille[3] == grille[6] and grille[0] != " ") or \
       (grille[1] == grille[4] == grille[7] and grille[1] != " ") or \
       (grille[2] == grille[5] == grille[8] and grille[2] != " "):
        return True
    #  diagonales
    if (grille[0] == grille[4] == grille[8] and grille[0] != " ") or \
       (grille[2] == grille[4] == grille[6] and grille[2] != " "):
        return True
    return False

# algho minimax de l'ia 
def minimax(plateau, profondeur, is_maximizing):
    if victory():  # La victoire est déjà déterminée
        return 1 if print_turn == "O" else -1
    if " " not in plateau:  # Match nul
        return 0

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

def meilleur_mouvement():
    meilleur_score = -float("inf")
    coup = -1
    for i in range(9):
        if grille[i] == " ":
            grille[i] = "O"
            score = minimax(grille, 0, False)
            grille[i] = " "
            if score > meilleur_score:
                meilleur_score = score
                coup = i
    return coup

# partie qui s'occupe du choix des cases du joueur 
def two_players():
    global grille
    global print_turn
    try:
        select = int(input(f"Joueur {print_turn}, choisissez une case (1-9): ")) - 1
        if 0 <= select <= 8 and grille[select] == " ":
            grille[select] = print_turn
        else:
            print("Choisissez une case vide valide.")
            two_players()
    except ValueError:
        print("Veuillez entrer un nombre entre 11 et 9.")
        two_players()

# Tour de l'IA
def ia_turn():
    global grille
    coup = meilleur_mouvement()
    grille[coup] = "O"
    print("L'IA a joué dans la case", coup + 1)

# Changement de tour entre X et O
def turn_chose():
    global print_turn
    print_turn = "O" if print_turn == "X" else "X"
    

#  jeu avec le choix de mode de jeu
def turn():
    mode = input("Choisissez le mode de jeu: '1' pour un joueur contre l'IA, '2' pour deux joueurs: ")
    if mode not in ["1", "2"]:
        print("Choix invalide. Veuillez réessayer.")
        return turn()

    while True:
        case()

        if mode == "2" or (mode == "1" and print_turn == "X"):
            two_players()  # coup du joeur 
            if victory():  # Vérification après le coup
                case()
                print(f"Félicitations ! Le joueur {print_turn} a gagné !")
                break
        else:
            ia_turn()  # coups de l'ia 
            if victory():  # Vérification après le coup de l'IA
                case()
                print("L'IA a gagné !")
                break

        if " " not in grille:  # Vérification de match nul
            case()
            print("Match nul !")
            break

        turn_chose()  # Changement de joueur 

turn()

