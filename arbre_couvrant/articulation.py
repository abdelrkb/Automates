# Fonction profondeur pour parcourir le graphe et identifier les points d'articulation
"""
La fonction profondeur est une implémentation de l'algorithme de parcours en profondeur qui parcourt le graphe et identifie 
les points d'articulation. Elle prend en paramètres le graphe, le noeud courant, un dictionnaire pour marquer les noeud atteints, 
des dictionnaires pour stocker les temps de découverte et les valeurs de min, le noeud parent, et un dictionnaire pour marquer les 
points d'articulation.
"""
def profondeur(graphe, u, atteint, parent, min, decouvert, articulation):
    # Variable pour compter le nombre d'enfants du noeud courant
    fils = 0
    # Marquer le noeud courant comme atteint
    atteint[u] = True
    # Assigner le temps de découverte et la valeur min du noeud courant
    decouvert[u] = profondeur.time
    """
    Lorsqu'on atteint un noeud pour la première fois, son temps de découverte est enregistré dans le dictionnaire.
    Ce temps de découverte est incrémenté progressivement à mesure que de nouveaux noeud sont découverts pendant le parcours en profondeur.
    """
    min[u] = profondeur.time
    # Incrémenter le temps de découverte global
    profondeur.time += 1
    """
    min est utilisé pour déterminer si un noeud est un point d'articulation un noeud u est un point d'articulation si un de ses voisins a
    une valeur supérieure ou égale à la valeur de découverte de u cela signifie que la suppression du noeud u diviserait le graphe en plusieurs 
    composantes connexes distinctes, ce qui en fait un point d'articulation.
    """
    # Parcours des voisins du noeud courant
    for v in graphe[u]:
        if not atteint[v]:
            # Si le voisin n'est pas atteint, lancer une profondeur récursive depuis ce voisin
            fils += 1
            parent[v] = u
            profondeur(graphe, v, atteint, parent, min, decouvert, articulation)
            # Mettre à jour la valeur min du noeud courant
            min[u] = min(min[u], min[v])
            
            # Vérifier si le noeud courant est un point d'articulation
            if parent[u] == -1 and fils > 1:
                articulation[u] = True
            elif parent[u] != -1 and min[v] >= decouvert[u]:
                articulation[u] = True
        elif v != parent[u]:
            # Mettre à jour la valeur min du noeud courant s'il y a un retour en arrière
            min[u] = min(min[u], decouvert[v])

# Fonction pour trouver tous les points d'articulation dans le graphe
def articulations(graphe):
    # Initialisation des structures de données nécessaires
    atteint = {}  # Dictionnaire pour suivre les noeud atteints
    decouvert = {}     # Dictionnaire pour stocker le temps de découverte de chaque noeud
    min = {}      # Dictionnaire pour stocker la valeur min de chaque noeud
    parent = {}   # Dictionnaire pour enregistrer le parent de chaque noeud
    articulation = {}       # Dictionnaire pour marquer les points d'articulation
    profondeur.time = 0  # Initialiser le temps global
    
    # Initialisation des dictionnaires avec les valeurs par défaut
    for node in graphe:
        atteint[node] = False
        decouvert[node] = 0
        min[node] = 0
        parent[node] = -1
        
    # Parcours de chaque noeud du graphe pour trouver les points d'articulation
    for node in graphe:
        if not atteint[node]:
            profondeur(graphe, node, atteint, parent, min, decouvert, articulation)
    
    # Filtrer les noeud marqués comme points d'articulation
    return articulation

# Exemple
#On representera sous forme de dictionnaire pour faciliter la compléxité
G = {1: [2, 3], 2: [1, 3], 3: [1, 2, 4, 5], 4: [3, 5, 6], 5: [3, 4], 6: [4, 7], 7: [6]}
artic = articulations(G)
GraphArticulations = [node for node in artic if artic[node]]
print("Articulations:", GraphArticulations)
