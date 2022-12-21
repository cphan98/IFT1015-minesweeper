# Hoang-Thi-Thi Cynthia Phan 20220019
# Vincent Hoang 20183549

def cellulesHTML(longueur):

    # La fonction cellulesHTML prend comme paramètre un entier positif et
    # retourne un texte contenant le code HTML codant le nombre de cellules à
    # ajouter dans chaque rangée tableau. Chaque cellule contient une image
    # d'une tuile vide.

    cellules = ''
    if largeur <= 0:
        return -1
    else:
        for i in range(largeur):
            cellules += ('<td id="tuile' + str(i) +
                         '"><img src="http://codeboot.org/images/minesweeper/blank.png"></td>')
        return cellules


def rangeesHTML(largeur, hauteur):

    # La fonction rangeesHTML prend commes paramètres deux entiers positifs et
    # retourne un texte contenant le code HTML codant le nombre de rangées à
    # inclure dans le tableau. Chaque rangée contient aussi le code qui code
    # les cellules.

    pass


def tableauHTML(longueur, hauteur):

    # La fonction tableauHTML prend comme paramètres deux entiers positifs,
    # largeur et hauteur, et retourne un texte contenant code HTML qui code
    # le tableau.

    pass


def testDemineur():

    # La procédure testDemineur teste les fonctions ci-dessus.

    # cellulesHTML

    assert cellulesHTML(-1) == -1
    assert cellulesHTML(0) == -1
    assert cellulesHTML(
        1) == '<td id="tuile0"><img src="http://codeboot.org/images/minesweeper/blank.png"></td>'
    assert cellulesHTML(
        2) == '<td id="tuile0"><img src="http://codeboot.org/images/minesweeper/blank.png"></td><td id="tuile1"><img src="http://codeboot.org/images/minesweeper/blank.png"></td>'

    # rangeesHTML

    assert rangeesHTML(-1, -1) == -1
    assert rangeesHTML(0, 0) == -1
    assert rangeesHTML(1, 0) == -1
    assert rangeesHTML(0, 1) == -1
    assert rangeesHTML(
        1, 1) == '<tr><td id="tuile0"><img src="http://codeboot.org/images/minesweeper/blank.png"></td></tr>'
    assert rangeesHTML(
        2, 1) == '<tr><td id="tuile0"><img src="http://codeboot.org/images/minesweeper/blank.png"></td><td id="tuile1"><img src="http://codeboot.org/images/minesweeper/blank.png"></td></tr>'
    assert rangeesHTML(1, 2) == '<tr><td id="tuile0"><img src="http://codeboot.org/images/minesweeper/blank.png"></td></tr><tr><td id="tuile0"><img src="http://codeboot.org/images/minesweeper/blank.png"></td></tr>'
