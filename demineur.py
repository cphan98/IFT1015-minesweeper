# Hoang-Thi-Thi Cynthia Phan 20220019
# Vincent Hoang 20183549

# Le code suivant programme...

nbRangees = 0   # nombre de rangees du démineur
nbColonnes = 0  # nombre de colonnes du démineur
tuiles = []     # matrice contenant toutes les tuiles du démineur
nbMines = 0     # nombre de mines présents dans le jeu
mines = []      # liste des tuiles contenant une mine
nbClics = 0     # nombre de clics de la souris sur le jeu


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

    for _ in range(hauteur):
        if len(cellules) == largeur:
            rangees.append(''.join(cellules[0:]))
        elif len(cellules) == 0:
            return rangees
        else:
            rangees.append(''.join(cellules[0:largeur]))
            for _ in range(largeur):
                cellules.pop(0)

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


def matriceTuiles(largeur, hauteur):

    # La fonction matriceTuiles prend deux entiers positifs et retourne une
    # matrice contenant toutes les tuiles du démineur.

    global tuiles
    tuiles = []
    tuile = 0

    for _ in range(hauteur):
        cellules = []

        for _ in range(largeur):
            cellules.append('tuile' + str(tuile))
            tuile += 1

        tuiles.append(cellules)

    return tuiles


def placerMines(largeur, hauteur):

    # La fonction placerMines prend comme paramètres deux entiers positifs et
    # retourne un tableau de texte contenant les tuiles qui cachent une mine.
    # Les tuiles sont choisies aléatoirement.

    global tuiles, nbMines, mines
    mines = []
    repeter = True

    while repeter:
        rangee = math.floor(hauteur * random())
        colonne = math.floor(largeur * random())
        tuile = tuiles[rangee][colonne]

        if tuile not in mines:
            mines.append(tuile)

        repeter = len(mines) < nbMines

    return mines


def calculerNbClics():

    # La fonction calculerNbClics incrémente de 1 le nombre de clics nbClics.

    global nbClics
    nbClics += 1


def init(largeur, hauteur):

    # La procédure init prend deux entiers positifs comme paramètres et
    # ajoute le code HTML à l'élément <div id="main"></div>. La matrice des
    # tuiles du démineur est mise à jour.

    global nbRangees, nbColonnes, nbClics
    nbRangees = hauteur
    nbColonnes = largeur
    nbClics = 0

    if nbColonnes <= 0 or nbRangees <= 0:
        return -1
    else:
        main = document.querySelector('#main')
        images = prechargerImagesHTML()
        tableau = tableauHTML(nbColonnes, nbRangees)
        css = '<style>#main table {border: 1px solid black;} #main table td {width: 25px; height: 25px; border: none;} img {width: 25px; height: 25px;}</style>'
        html = css + images + tableau
        main.innerHTML = html
        global tuiles
        tuiles = matriceTuiles(nbColonnes, nbRangees)


def clic(tuile):

    # La fonction clic prend comme paramètre un texte de l'identifiant d'une
    # tuile cliquée et détermine ce qu'il faut faire selon le type du clic
    # (avec ou sans la touche SHIFT) et selon la tuile cliquée.

    global nbRangees, nbColonnes, mines, nbClics
    calculerNbClics()

    if nbClics == 1:
        mines = placerMines(nbColonnes, nbRangees)

    if event.shiftKey == True:
        pass
    else:
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

    assert tableauHTML(
        1, 1) == '<table><tr><td id="tuile0" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td></tr></table>'
    assert tableauHTML(1, 2) == '<table><tr><td id="tuile0" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td></tr><tr><td id="tuile1" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td></tr></table>'
    assert tableauHTML(2, 1) == '<table><tr><td id="tuile0" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td><td id="tuile1" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td></tr></table>'
    assert tableauHTML(2, 2) == '<table><tr><td id="tuile0" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td><td id="tuile1" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td></tr><tr><td id="tuile2" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td><td id="tuile3" onclick=""><img src="http://codeboot.org/images/minesweeper/blank.png"></td></tr></table>'

    # matriceTuiles

    assert matriceTuiles(1, 1) == [['tuile0']]
    assert matriceTuiles(1, 2) == [['tuile0'], ['tuile1']]
    assert matriceTuiles(2, 1) == [['tuile0', 'tuile1']]
    assert matriceTuiles(2, 2) == [['tuile0', 'tuile1'], ['tuile2', 'tuile3']]


testDemineur()
init(8, 5)
