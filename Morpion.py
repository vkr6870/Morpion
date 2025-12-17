def morpion():
    grille = [[" "]*3]*3
    joueur = "X"

    for tour in range(9):
        print(grille)
        x = int(input("ligne : "))
        y = int(input("colonne : "))

        grille[x][y] = joueur

        if grille[0][0] == joueur:
            print(joueur, "a gagné")
            break

        if joueur == "X":
            joueur = "X"
        else:
            joueur = "O"

morpion()