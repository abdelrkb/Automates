#####################################################
#Algorithme de dijkstra avec poids
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

def dijkstra_avec_poids(graphe):
    # Récupère l'ensemble de tous les a_traiter du graphe en prenant le premier et le deuxième élément de chaque arête
    a_traiter = {arete[0] for arete in graphe} | {arete[1] for arete in graphe}
    s0 = sommet_min(G)
    # Initialise les tables des distances (d) et des pères (p)
    d = {}
    p = {}

    # Initialise les distances de tous les a_traiter à l'infini et les pères à None
    for sommet in a_traiter:
        d[sommet] = float('inf')
        p[sommet] = s0
    
    # La distance du sommet de départ s1 est mise à 0
    d[s0] = 0

    # Tant qu'il reste des a_traiter à explorer
    while a_traiter:
        # Sélectionne le sommet non exploré avec la plus petite distance
        sommet = min(a_traiter, key=lambda s: d[s])
        a_traiter.remove(sommet)  #
        
        # Parcourt toutes les arêtes du graphe
        for arete in graphe:
            # Vérifie si le sommet est adjacent a l'autre sommet
            if arete[0] == sommet:
                voisin = arete[1]
            elif arete[1] == sommet:
                voisin = arete[0]
            else:
                continue  # Passe à l'arête suivante s'il ne concerne pas le sommet actuel

            # Vérifie si le voisin est encore à traiter
            if voisin in a_traiter:
                # Calcule la nouvelle distance en ajoutant le poids de l'arête à la distance du sommet actuel
                distance_actuel = d[sommet] + arete[2]

                # Met à jour la distance et le prédécesseur si la nouvelle distance est plus petite
                if distance_actuel < d[voisin]:
                    d[voisin] = distance_actuel
                    p[voisin] = sommet

    # Retourne les tables des distances et des pères
    return p, d

# Graphe de test
G = [
    [1, 2, 10], [1, 3, 2], [1, 5, 6], [1, 6, 2],
    [2, 3, 4], [2, 5, 0], [3, 5, 2], [3, 4, 1],
    [4, 5, 0], [5, 6, 1]
]

# Exemple d'utilisation
p, d = dijkstra_avec_poids(G)
print("Table des profondeurs:", d)
print("Table des pères:", p)
