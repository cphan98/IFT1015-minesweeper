# Hoang-Thi-Thi Cynthia Phan 20220019
# Vincent Hoang 20183549

def cellulesHTML(largeur, hauteur):

    # La fonction cellulesHTML prend comme paramètre deux entiers positifs et
    # retourne un tableau de texte contenant toutes les cellules HTML du
    # tableau du démineur. Chaque cellule contient une image d'une tuile vide.

    cellules = []
    nbCellules = largeur * hauteur

    for i in range(nbCellules):
        cellules.append('<td id="tuile' + str(i) +
                        '" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td>')

    return cellules


def cellulesParRangeeHTML(largeur, hauteur):

    # La fonction cellulesParRangeeHTML prend comme paramètres deux entiers
    # positif et retourne un tableau de texte contenant les cellules HTML
    # pour chaque rangée du tableau du démineur.

    cellules = cellulesHTML(largeur, hauteur)
    rangees = []
    rangee = 0

    for _ in range(hauteur):
        if rangee >= largeur:
            rangees.append(''.join(cellules[rangee:]))
        else:
            rangees.append(''.join(cellules[rangee: largeur]))
            rangee += (largeur)

        if rangees[-1] == '':
            rangees.pop()

    return rangees


def rangeesHTML(largeur, hauteur):

    # La fonction rangeesHTML prend comme paramètres deux entiers positifs et
    # retourne un texte contenant le code HTML codant chaque rangée du
    # tableau du démineur.

    cellulesParRangee = cellulesParRangeeHTML(largeur, hauteur)
    rangees = ''

    for rangee in cellulesParRangee:
        rangees += ('<tr>' + rangee + '</tr>')

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

    if largeur <= 0 or hauteur <= 0:
        return -1
    else:
        main = document.querySelector('#main')
        images = prechargerImagesHTML()
        tableau = tableauHTML(largeur, hauteur)
        css = '<style>#main table {border: 1px solid black;} #main table td {width: 5px; height: 5px; border: none;} img {width: 5px; height: 5px;}</style>'
        html = css + images + tableau
        main.innerHTML = html


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

    # cellulesParRangeeHTML

    assert cellulesParRangeeHTML(0, 0) == []
    assert cellulesParRangeeHTML(0, 1) == []
    assert cellulesParRangeeHTML(1, 0) == []
    assert cellulesParRangeeHTML(1, 1) == [
        '<td id="tuile0" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td>']
    assert cellulesParRangeeHTML(1, 2) == [
        '<td id="tuile0" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td>', '<td id="tuile1" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td>']
    assert cellulesParRangeeHTML(2, 1) == [
        '<td id="tuile0" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td><td id="tuile1" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td>']
    assert cellulesParRangeeHTML(2, 2) == [
        '<td id="tuile0" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td><td id="tuile1" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td>', '<td id="tuile2" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td><td id="tuile3" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td>']

    # rangeesHTML

    assert rangeesHTML(0, 0) == ''
    assert rangeesHTML(0, 1) == ''
    assert rangeesHTML(1, 0) == ''
    assert rangeesHTML(
        1, 1) == '<tr><td id="tuile0" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td></tr>'
    assert rangeesHTML(1, 2) == '<tr><td id="tuile0" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td></tr><tr><td id="tuile1" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td></tr>'
    assert rangeesHTML(2, 1) == '<tr><td id="tuile0" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td><td id="tuile1" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td></tr>'
    assert rangeesHTML(2, 2) == '<tr><td id="tuile0" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td><td id="tuile1" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td></tr><tr><td id="tuile2" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td><td id="tuile3" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td></tr>'

    # tableauHTML

    assert tableauHTML(-1, -1) == -1
    assert tableauHTML(0, -1) == -1
    assert tableauHTML(1, 0) == -1
    assert tableauHTML(0, 1) == -1
    assert tableauHTML(
        1, 1) == '<table><tr><td id="tuile0" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td></tr></table>'
    assert tableauHTML(1, 2) == '<table><tr><td id="tuile0" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td></tr><tr><td id="tuile1" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td></tr></table>'
    assert tableauHTML(2, 1) == '<table><tr><td id="tuile0" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td><td id="tuile1" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td></tr></table>'
    assert tableauHTML(2, 2) == '<table><tr><td id="tuile0" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td><td id="tuile1" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td></tr><tr><td id="tuile2" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td><td id="tuile3" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td></tr></table>'


testDemineur()
