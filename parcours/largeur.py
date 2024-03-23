#####################################################
#Algorithme de parcours par largeur
#####################################################
sommets = [1,2,3,4,5,6]
G = [[1, 3],[2, 3],[1, 4], [1,6], [1,5], [4,5]]

#Fonction pour trouver le sommet minimum dans le graphe
def sommet_min(G):
    # Initialise le minimum à l'infini
    minimum = float('inf')
    
    # Parcourt tous les sommets du graphe pour trouver le minimum
    for arrete in G:
        for s in arrete:
            minimum = min(minimum, s)
    
    return minimum

def largeur(G):
    s0 = sommet_min(G)
    # Initialisation
    file = []  #file pour stocker les sommets
    d = {s0: 0}  # Dictionnaire des distances (on initialise s0 à 0 car la distance avec lui même est de 0)
    p = {s0: None}  # Dictionnaire (on met None pour s0 car il n'a pas de prédecesseur)

    # Le sommet de départ de la file sera s0
    file.append(s0)

    # Initialisation des distances et prédécesseurs pour tous les sommets du graphe
    for arrete in G:
        for s in arrete:
            if s not in d:
                d[s] = -1  # Infini pas représentable on mettra donc -1
                p[s] = s0  # Initialisation du prédécesseur à s0

    # Parcours en largeur à partir du sommet de départ
    while file:
        s = file.pop(0)  # prend le premier sommet de la file
        for arrete in G:
            if s in arrete:  # Vérifie si le sommet est l'une des extrémités de l'arête
                t = arrete[1] if arrete[0] == s else arrete[0]  # Récupère l'autre extrémité de l'arête
                if d[t] == -1:  # Vérifie si le sommet n'a pas encore été visité
                    file.append(t)  # Ajoute le sommet à la file pour le visiter plus tard
                    d[t] = d[s] + 1  # Met à jour la distance du sommet par rapport au sommet de départ
                    p[t] = s  # Met à jour le prédécesseur du sommet


    # Retourne les dictionnaires contenant les distances et les prédécesseurs des sommets
    return p, d

p, d = largeur(G)
print("Table des pères:", p)
print("Table des profondeurs:", d)