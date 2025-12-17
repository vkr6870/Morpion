def victoire(grille, joueur):
    for ligne in grille:
        if ligne == [joueur]*3:
            return True

    for col in range(3):
        if [grille[i][col] for i in range(3)] == [joueur]*3:
            return True
        
    if grille[0][0] == joueur and grille[1][1] == joueur and grille[2][2] == joueur :
        return True
    
    if grille[0][2] == joueur and grille[1][1] == joueur and grille[2][0] == joueur :
        return True

    return False


def morpion():
    grille = [[" " for j in range(3)] for i in range(3)]

    for tour in range(9):
        if tour % 2 == 0:
            joueur = 'X'
        else:
            joueur = 'O'

        for ligne in grille:
            print(ligne)
            
        x = int(input("ligne : "))
        y = int(input("colonne : "))

        grille[x][y] = joueur

        if victoire(grille, joueur) == True:
            print(joueur, "a gagné")
            break
        
morpion()