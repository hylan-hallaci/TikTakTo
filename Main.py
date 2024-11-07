# Grille de jeu initiale
grille = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

# Fonction pour afficher la grille
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

# Vérifie la victoire
def verifier_victoire(plateau, joueur):
    combinaisons_gagnantes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Lignes
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colonnes
        [0, 4, 8], [2, 4, 6]              # Diagonales
    ]
    for combinaison in combinaisons_gagnantes:
        if all(plateau[i] == joueur for i in combinaison):
            return True
    return False

# Vérifie l'égalité
def verifier_egalite(plateau):
    return " " not in plateau

# Fonction de l'IA pour son coup
def minimax(plateau, profondeur, is_maximizing):
    if verifier_victoire(plateau, "O"):
        return 1  # Score pour la victoire de l'IA
    if verifier_victoire(plateau, "X"):
        return -1  # Score pour la victoire du joueur
    if verifier_egalite(plateau):
        return 0  # Score pour l'égalité

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
    while True:
        case()
        if tour_joueur:
            player_turn()
            if verifier_victoire(grille, "X"):
                case()
                print("Félicitations ! Vous avez gagné !")
                break
        else:
            ia_turn()
            if verifier_victoire(grille, "O"):
                case()
                print("L'IA a gagné !")
                break
        if verifier_egalite(grille):
            case()
            print("Match nul !")
            break
        tour_joueur = not tour_joueur

# Lancer le jeu
jeu()
