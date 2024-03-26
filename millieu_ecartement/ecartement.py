#####################################################
# Ecartement
#####################################################
#La méthode pour calculer l'écartement d'un arbre consiste à trouver la racine de l'arbre, puis à parcourir chaque nœud de l'arbre en 
# profondeur. Lors de ce parcours, on exclut le nœud actuel et ses descendants pour éviter les boucles.
# On calcule la profondeur maximale à partir de chaque nœud enregistré, ce qui représente la distance maximale à la source. 
# Enfin, on prend le minimum de ces profondeurs maximales pour obtenir l'écartement de l'arbre. 
# Cette approche garantit un calcul efficace de l'écartement avec une complexité linéaire par rapport à la taille de l'arbre.


def profMaximal(p, exclude):
    def racine(p):
        # Recherche des nœuds où le parent est le même que le nœud lui-même
        racines = [s for s, p in p.items() if s == p]
        # S'il y a une racine, la retourner, sinon None
        return racines[0] if racines else None
    racine = racine(p)
    profondeur_maximale = 0
    pile = [(racine, 0)]  # On ajoute la racine avec une profondeur de 0 dans la pile
    while pile:
        s, profondeur = pile.pop()
        profondeur_maximale = max(profondeur_maximale, profondeur)
        for fils, pere in p.items():
            if pere == s and fils != s and fils not in exclude:  # Exclure le nœud actuel et ses enfants
                pile.append((fils, profondeur + 1))
    return profondeur_maximale


def ecartement(p):
    profondeurs_maximales = []
    for s in p:
        print(s)
        profondeurs_maximales.append(profMaximal(p, {s}))  # Exclure le nœud actuel et ses enfants 
        print(profondeurs_maximales) 
    return min(profondeurs_maximales)

# Exemple d'utilisation
p = {
    1: 1,
    2: 1,
    3: 2,
    4: 2,
    5: 2,
    6: 3,
    7: 5,
    8: 5
}

ecartement = ecartement(p)
print("L'écartement de l'arbre est de:", ecartement)
