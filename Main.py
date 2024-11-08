print_turn=0
import random
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
                                                          #affichage grille pour les 2 modes
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
          
def victory():                                      #systeme de victoire pour les 2 modes, compares les combinaisons gagnantes aux donnees de la grille
    global grille
    if " " not in grille:
        print("fin de partie, égalité")
        
        return exit()
    elif (grille[0] == grille[1] == grille[2] and grille[0] != " ") or (grille[3] == grille[4] == grille[5] and grille[3] != " ") or (grille[6] == grille[7] == grille[8] and grille[6] != " "):
        print(f"victoire des {print_turn} en ligne horizontale ! GG")
        
        return exit()
    elif (grille[0] == grille[3] == grille[6] and grille[0] != " ") or (grille[1] == grille[4] == grille[7] and grille[1] != " ") or (grille[2] == grille[5] == grille[8] and grille[2] != " "):
        print(f"victoire des {print_turn} en ligne verticale ! GG")
        
        return exit()
    elif (grille[0] == grille[4] == grille[8] and grille[0] != " ") or (grille[2] == grille[4] == grille[6] and grille[2] != " "):
        print(f"victoire des {print_turn} en diagonale ! GG")
        
        return exit()
    else:
        print("manche suivante")
        

def two_players():      #fonction qui demande a l'utilisateur la case qu'il souhaite seulement pour le mode 2 joueurs
    global grille
    global print_turn
    new_value = int(input("Choisir la case: "))
    if grille[new_value] == " ":
            grille[new_value]= print_turn
    else: 
        print("choisissez une case vide")
        case()
        two_players()

def bigb():
    global grille
    ia = random.randint(0,8)
    if grille[ia] == " ":
        grille[ia] = print_turn
    else:
        bigb()


def player_turn():                              #fonction joueur IA
    global grille
    case()
    coup = int(input("Entrez le numéro de case (0-8) pour placer votre X: "))
    if grille[coup] == " ":
        grille[coup] = print_turn
    else:
        print("Case déjà prise. Choisissez une autre case.")
        player_turn()

def ia_turn():                                  #fonction IA playing
    global grille
    bigb()
    print("L'IA a joué " )
tour_joueur = True
def jeu():                                                   #fonction IA JEU
    
    global tour_joueur
    if tour_joueur ==True:
        turn_chose()
        player_turn()
        case()
        victory()
        tour_joueur = not tour_joueur
        
        jeu()
            
    else:
        turn_chose()
        ia_turn()
        case()
        victory()
        tour_joueur = not tour_joueur
        
        jeu()
    
        
def turn():                                       #fonction 2 joueurs JEU
    global grille
    case()    #display de la grille 
    turn_chose() # changement de joueur
    two_players() # demande la case à jouer  
    case()
    victory() # verifie la victoire 
    turn()

def start():                                       #initialisation choix du mode de jeu
    i=int(input("Jouer à deux ou contre une ia impossible à battre ? \n 1 contre l'IA \n 2 contre un autre joueur \n Choix :    "))
    if i == 1:
        jeu()
    elif i == 2:
        turn()
    else:
        print("choisis 1 ou 2 ")
        start()
start()
    