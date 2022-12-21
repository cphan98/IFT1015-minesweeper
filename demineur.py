# Hoang-Thi-Thi Cynthia Phan 20220019
# Vincent Hoang 20183549

def cellulesHTML(largeur, hauteur):

    # La fonction cellulesHTML prend comme paramètre deux entiers positifs et
    # retourne un tableau contenant toutes les cellules du tableau du
    # démineur. Chaque cellule contient une image d'une tuile vide.

    cellules = []
    nbCellules = largeur * hauteur

    for i in range(nbCellules):
        cellules.append('<td id="tuile' + str(i) +
                        '" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td>')
    return cellules


def rangeesHTML(largeur, hauteur):

    # La fonction rangeesHTML prend commes paramètres deux entiers positifs et
    # retourne un texte contenant le code HTML codant le nombre de rangées à
    # inclure dans le tableau. Chaque rangée contient aussi le code qui code
    # les cellules.

    rangees = ''
    cellules = cellulesHTML(largeur)

    for _ in range(hauteur):
        rangees += ('<tr>' + cellules + '</tr>')
    return rangees


def tableauHTML(largeur, hauteur):

    # La fonction tableauHTML prend comme paramètres deux entiers positifs,
    # largeur et hauteur, et retourne un texte contenant code HTML qui code
    # le tableau.

    tableau = ''

    if largeur <= 0 or hauteur <= 0:
        return -1
    else:
        rangees = rangeesHTML(largeur, hauteur)
        tableau += ('<table>' + rangees + '</table>')
    return tableau


def prechargerImagesHTML():

    # La fonction prechargerImagesHTML retourne un texte contenant les
    # préchargements HTML de chaque image du démineur.

    images = ''
    prefixe = '<link rel="preload" href="http://codeboot.org/images/minesweeper/'
    suffixe = '.png">'
    tuilesSpeciales = ['blank', 'flag', 'mine', 'mine-red', 'mine-red-x']

    for i in range(9):
        images += (prefixe + str(i) + suffixe)

    for j in tuilesSpeciales:
        images += (prefixe + j + suffixe)

    return images


def ajouterHTML(largeur, hauteur):

    # La procédure prend deux entiers positifs comme paramètres et ajoute le
    # code HTML à l'élément <div id="main"></div>.

    pass


def testDemineur():

    # La procédure testDemineur teste les fonctions ci-dessus.

    # cellulesHTML

    assert cellulesHTML(0, 0) == []
    assert cellulesHTML(0, 1) == []
    assert cellulesHTML(1, 0) == []
    assert cellulesHTML(1, 1) == [
        '<td id="tuile0" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td>']
    assert cellulesHTML(1, 2) == [
        '<td id="tuile0" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td>', '<td id="tuile1" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td>']

    # rangeesHTML

    assert rangeesHTML(
        1, 1) == '<tr><td id="tuile0" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td></tr>'
    assert rangeesHTML(
        2, 1) == '<tr><td id="tuile0" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td><td id="tuile1" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td></tr>'
    assert rangeesHTML(1, 2) == '<tr><td id="tuile0" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td></tr><tr><td id="tuile0" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td></tr>'

    # tableauHTML

    assert tableauHTML(-1, -1) == -1
    assert tableauHTML(0, -1) == -1
    assert tableauHTML(1, 0) == -1
    assert tableauHTML(0, 1) == -1
    assert tableauHTML(
        1, 1) == '<table><tr><td id="tuile0" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td></tr></table>'
    assert tableauHTML(2, 1) == '<table><tr><td id="tuile0" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td><td id="tuile1" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td></tr></table>'
    assert tableauHTML(1, 2) == '<table><tr><td id="tuile0" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td></tr><tr><td id="tuile0" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td></tr></table>'


testDemineur()
