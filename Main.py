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

def victory(grille):
    if grille(1) !=" " and grille (2) !=" " and grille (3) !=" " and grille (4) !=" " and grille (5) !=" " and grille (6) !=" " and grille(7)!=" " and grille (8) !=" " and grille (9) !=" ":
        print("fin de partie, égalité")
        return
    elif grille(1) == grille(2) == grille(3) and grille(1)!=" " or grille(4) == grille(5) == grille(6) and grille(4)!= " " or grille(7) == grille(8) == grille(9) and grille(8)!=0:
        print(f"victoire en ligne horizontale ! GG")
        return
    elif grille(1) == grille(4) == grille(7) and grille(1) != " " or grille(2) == grille(5) == grille (8) and grille(5) !=" " or grille(3) == grille(6) == grille(9) and grille(3)!= 0:
        print(f"victoire en ligne vertical ! GG")
        return
    elif grille(1) == grille(5) == grille(9) and grille(1)!=" " or grille(3) == grille(5) == grille(7) and grille(5) != " ":
        print("victoire en diagonal ! GG")
        return
        
         
        
        


    