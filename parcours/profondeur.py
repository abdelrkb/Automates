#####################################################
#Algorithme de parcours par profondeur
#####################################################

# Fonction pour trouver le sommet minimum dans le graphe
def sommet_min(G):
    # Initialise le minimum à l'infini
    minimum = float('inf')
    
    # Parcourt tous les sommets du graphe pour trouver le minimum
    for arrete in G:
        for s in arrete:
            minimum = min(minimum, s)
    
    return minimum

# Fonction de parcours en profondeur (DFS) avec retour des tables des pères et des profondeurs
def profondeur(G):
    # Trouver le sommet de départ
    s0 = sommet_min(G)
    # Initialisation
    pile = [s0]  # Pile pour stocker les sommets à explorer
    traite = set()  # Ensemble pour garder une trace des sommets visités
    p = {}  # Dictionnaire pour stocker les pères des sommets
    d = {}  # Dictionnaire pour stocker les profondeurs des sommets
    temps = 0  # Variable pour suivre le temps de découverte des sommets

    # Parcours en profondeur
    while pile:
        sommet_courant = pile.pop()  # Prend le sommet en haut de la pile
        if sommet_courant not in traite:
            traite.add(sommet_courant)  # Marque le sommet comme visité
            temps += 1
            d[sommet_courant] = temps  # Enregistre la profondeur du sommet
            
            # Parcourir les voisins du sommet courant et les empiler s'ils ne sont pas visités
            for arrete in G:
                if sommet_courant in arrete:
                    voisin = arrete[1] if arrete[0] == sommet_courant else arrete[0]
                    if voisin not in traite:
                        p[voisin] = sommet_courant  # Enregistre le père du voisin
                        pile.append(voisin)  # Empile le voisin non visité
                        
    return p, d

# Exemple d'utilisation
G = [[1, 3], [2, 3], [1, 4], [1, 6], [1, 5], [4, 5]]
p, d = profondeur(G)
print("Table des pères:", p)
print("Table des profondeurs:", d)