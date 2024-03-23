#####################################################
#Algorithme de dijkstra sans poids
#####################################################
def sommet_min(G):
    minimum = float('inf')
    for arrete in G:
        for s in arrete:
            minimum = min(minimum, s)
    return minimum


def dijkstra_sans_poids(G):
    # Nombre de sommets dans le graphe
    n = max(max(arrete) for arrete in G) + 1


    # Trouver le sommet de départ
    s0 = sommet_min(G)

    # Initialisation des tables des pères et des distances
    p = {node: s0 for node in range(n)}
    d = {node: float('inf') for node in range(n)}
    d[s0] = 0

    traite = set()  # Ensemble des sommets visités

    # Algorithme de Dijkstra
    while len(traite) < n:
        # Sélectionne le sommet s non visité avec la plus petite distance d
        s = min((voisin for voisin in range(n) if voisin not in traite), key=lambda x: d[x])

        # Ajoute s à l'ensemble des sommets visités
        traite.add(s)

        # Parcourt les voisins de s pour mettre à jour les distances
        for arrete in G:
            if s in arrete:
                voisin = arrete[0] if arrete[0] != s else arrete[1]
                if voisin not in traite:
                    # Met à jour la distance de voisin si un chemin plus court est trouvé
                    if d[s] + 1 < d[voisin]:  # Pour un graphe sans étiquette, la distance entre s et voisin est toujours égale à 1
                        d[voisin] = d[s] + 1
                        p[voisin] = s

    # Retourne les tables des pères et des distances
    #Suppression du sommet 0 qui s'ajoute dans le dictionnaire
    del p[0]
    del d[0]
    return p, d


# Graphe de test
G = [[1, 2], [1, 4], [2, 3], [3, 5], [4, 5]]

# Exemple d'utilisation
p, d = dijkstra_sans_poids(G)
print("Table des pères:", p)
print("Table des profondeurs:", d)
