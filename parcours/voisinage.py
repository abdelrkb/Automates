#####################################################
#Algorithme de parcours par voisinage
#####################################################
def sommet_min(G):
    # Initialise le minimum à l'infini
    minimum = float('inf')
    
    # Parcourt tous les sommets du graphe pour trouver le minimum
    for arrete in G:
        for s in arrete:
            minimum = min(minimum, s)
    
    return minimum


def voisinage(G):
    # Initialisation
    d = {}  # Dictionnaire des distances
    p = {}  # Dictionnaire des prédécesseurs
    sommets_atteints = set()  # Ensemble des sommets déjà atteints

    # Trouver le sommet de départ
    s0 = sommet_min(G)

    # Ajout du sommet de départ à la liste des sommets atteints avec une distance de 0
    d[s0] = 0
    p[s0] = None
    sommets_atteints.add(s0)

    # Parcours en largeur
    while sommets_atteints:
        sommet_courant = sommets_atteints.pop()  # Prend le prochain sommet à explorer

        # Parcourir les voisins du sommet courant
        for arrete in G:
            if sommet_courant in arrete:
                voisin = arrete[1] if arrete[0] == sommet_courant else arrete[0]
                if voisin not in d:  # Si le voisin n'a pas encore été visité
                    d[voisin] = d[sommet_courant] + 1
                    p[voisin] = sommet_courant
                    sommets_atteints.add(voisin)

    return p, d

# Exemple d'utilisation
G = [[1, 3], [2, 3], [1, 4], [1, 6], [1, 5], [4, 5]]
p, d = voisinage(G)
print("Table des pères:", p)
print("Table des profondeurs:", d)
