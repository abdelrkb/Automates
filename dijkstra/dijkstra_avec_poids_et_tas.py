#####################################################
#Algorithme de dijkstra avec poids et tas
#####################################################

def sommet_min(G):
    # Initialise le minimum à l'infini
    minimum = float('inf')
    
    # Parcourt toutes les arêtes du graphe pour trouver le minimum parmi les sommets
    for arete in G:
        # Parcourt les sommets de chaque arête
        for sommet in arete[:-1]:  # Exclut le poids à la fin de l'arête
            minimum = min(minimum, sommet)
    
    return minimum

# Fonction pour mettre à jour le tas après avoir modifié une distance
def maj_tas(tas, sommet, nouvelle_distance):
    for i in range(len(tas)):
        distance, s = tas[i]
        if s == sommet:
            tas[i] = (nouvelle_distance, sommet)
            break
    else:
        tas.append((nouvelle_distance, sommet))
    tas.sort()  # Trie la liste après chaque modification


def dijkstra_avec_poid_et_tas(graphe):
    # Récupère l'ensemble de tous les sommets du graphe
    sommets = {arete[0] for arete in graphe} | {arete[1] for arete in graphe}
    s0 = sommet_min(G)
    # Initialise les tables des distances (d) et des pères (p)
    d = {sommet: float('inf') for sommet in sommets}
    p = {sommet: None for sommet in sommets}
    
    # La distance du sommet de départ s0 est mise à 0
    d[s0] = 0
    
    # Crée une liste pour stocker les distances relatives des sommets non traités
    tas = [(0, s0)]  # (distance, sommet)

    # Tant qu'il reste des sommets à explorer dans le tas
    while tas:
        # Extrait le sommet avec la plus petite distance relative du tas
        distance_relative, sommet = tas.pop(0)
        
        # Parcourt les arêtes adjacentes au sommet extrait
        for arete in graphe:
            if arete[0] == sommet:
                voisin = arete[1]
            elif arete[1] == sommet:
                voisin = arete[0]
            else:
                continue
            
            # Calcule la nouvelle distance en ajoutant le poids de l'arête à la distance du sommet actuel
            distance_actuel = distance_relative + arete[2]

            # Met à jour la distance et le prédécesseur si la nouvelle distance est plus petite
            if distance_actuel < d[voisin]:
                d[voisin] = distance_actuel
                p[voisin] = sommet
                maj_tas(tas, voisin, distance_actuel)  # Met à jour le tas

    # Retourne les tables des distances et des pères
    return p, d

# Graphe test
G = [[1, 2, 10], [1, 3, 2], [1, 5, 6], [1, 6, 2],
    [2, 3, 4], [2, 5, 0], [3, 5, 2], [3, 4, 1],
    [4, 5, 0], [5, 6, 1]]

# Exemple d'utilisation
p, d = dijkstra_avec_poid_et_tas(G)
print("Table des profondeurs:", d)
print("Table des pères:", p)
