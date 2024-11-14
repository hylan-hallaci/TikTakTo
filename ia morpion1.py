def bigb(grille, print_turn):
    
    for i in range(0, 9, 3):    #vérifier les lignes pour bloquers le joueur
        if grille[i] == grille[i+1] == "O" and grille[i+2] == " ":
            grille[i+2] = print_turn
            return
        elif grille[i+1] == grille[i+2] == "O" and grille[i] == " ":
            grille[i] = print_turn
            return
        elif grille[i] == grille[i+2] == "O" and grille[i+1] == " ":
            grille[i+1] = print_turn
            return

    for i in range(3):  #vérifier les colonnes pour bloquers le joueur
        if grille[i] == grille[i+3] == "O" and grille[i+6] == " ":
            grille[i+6] = print_turn
            return
        elif grille[i+3] == grille[i+6] == "O" and grille[i] == " ":
            grille[i] = print_turn
            return
        elif grille[i] == grille[i+6] == "O" and grille[i+3] == " ":
            grille[i+3] = print_turn
            return

 #vérifier les diagonales pour bloquers le joueur
    if grille[0] == grille[4] == "O" and grille[8] == " ":
        grille[8] = print_turn
        return
    elif grille[2] == grille[4] == "O" and grille[6] == " ":
        grille[6] = print_turn
        return
    elif grille[4] == grille[8] == "O" and grille[0] == " ":
        grille[0] = print_turn
        return
    elif grille[4] == grille[6] == "O" and grille[2] == " ":
        grille[2] = print_turn
        return


    for i in range(0, 9, 3):  #vérifier les lignes pour gagner
        if grille[i] == grille[i+1] == print_turn and grille[i+2] == " ":
            grille[i+2] = print_turn
            return
        elif grille[i+1] == grille[i+2] == print_turn and grille[i] == " ":
            grille[i] = print_turn
            return
        elif grille[i] == grille[i+2] == print_turn and grille[i+1] == " ":
            grille[i+1] = print_turn
            return

    for i in range(3):  #vérifier les colonnes pour gagner
        if grille[i] == grille[i+3] == print_turn and grille[i+6] == " ":
            grille[i+6] = print_turn
            return
        elif grille[i+3] == grille[i+6] == print_turn and grille[i] == " ":
            grille[i] = print_turn
            return
        elif grille[i] == grille[i+6] == print_turn and grille[i+3] == " ":
            grille[i+3] = print_turn
            return

 #vérifier les diagonales pour gagner
    if grille[0] == grille[4] == print_turn and grille[8] == " ":
        grille[8] = print_turn
        return
    elif grille[2] == grille[4] == print_turn and grille[6] == " ":
        grille[6] = print_turn
        return
    elif grille[4] == grille[8] == print_turn and grille[0] == " ":
        grille[0] = print_turn
        return
    elif grille[4] == grille[6] == print_turn and grille[2] == " ":
        grille[2] = print_turn
        return

#si l'ia ne peut ni gagner, ni bloquer, elle choisit un emplacement stratégique le centre ou un coin
    if grille[4] == " ":
        grille[4] = print_turn
        return

    
    for coin in [0, 2, 6, 8]:
        if grille[coin] == " ":
            grille[coin] = print_turn
            return

#si le centre edt pris et qu'aucun coin n'est disponible, l'ia choisit une case vide aléatoire
    for i in range(9):
        if grille[i] == " ":
            grille[i] = print_turn
            return
