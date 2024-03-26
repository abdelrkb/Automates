def pere(parent, i):
    # Si le parent de l'élément n'est pas lui-même, on recherche récursivement le pere de son parent
    if parent[i] != i:
        parent[i] = pere(parent, parent[i])  # Compression de chemin: on met à jour le parent directement au pere
    return parent[i]  # Retourne le pere de l'élément

def attache(parent, rang, s1, s2):
    #Fais deux arbres en un en fusionnant le moins profond au premier
    # Recherche des parents de s1 et s2
    ps1 = pere(parent, s1)
    ps2 = pere(parent, s2)

    # Comparaison des rangs pour déterminer comment fusionner les CC
    if rang[ps1] < rang[ps2]:
        parent[ps1] = ps2  # Attache l'arbre de s1 à celui de s2
    elif rang[ps1] > rang[ps2]:
        parent[ps2] = ps1  # Attache l'arbre de s2 à celui de s1
    else:
        parent[ps2] = ps1  # Attache l'arbre de s2 à celui de s1
        rang[ps1] += 1  # Augmente le rang de l'arbre attaché

def pasKruskal(graph):
    graph.sort(key=lambda x: x[2])  # Tri des arêtes par poids
    parent = {}  # Dictionnaire pour stocker les pères
    rang = {}    # Dictionnaire pour stocker les rangs

    # Initialisation des parents et rangs pour chaque sommet
    for edge in graph:
        sommet1, sommet2, poids = edge
        if sommet1 not in parent:
            parent[sommet1] = sommet1
            rang[sommet1] = 0
        if sommet2 not in parent:
            parent[sommet2] = sommet2
            rang[sommet2] = 0

    arbre_couvrant = []  # Liste pour stocker les arêtes de l'arbre couvrant minimal

    # Parcours des arêtes triées par poids
    for arrete in graph:
        sommet1, sommet2, poids = arrete
        pere1 = pere(parent, sommet1)  # pere de s1
        pere2 = pere(parent, sommet2)  # pere de s2
        if pere1 != pere2:
            arbre_couvrant.append(arrete)  # Ajout de l'arête à l'arbre couvrant
            attache(parent, rang, sommet1, sommet2)  # Fusion des CC

    return arbre_couvrant

# Exemple d'utilisation avec le graphe G
G = [[1, 7, 2], [1, 6, -2], [1, 2, 1], [6, 5, 0], [2, 6, 2], [2, 5, -1], [2, 3, 4], [3, 4, 4], [4, 5, 1], [4, 2, 3]]
arbre_couvrant_minimal = pasKruskal(G)
print("Arbre couvrant minimal :", arbre_couvrant_minimal)

###-------------
### La complexité sera au plus quadratique.
###-------------