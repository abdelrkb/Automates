#####################################################
# Millieu
#####################################################

def prof(p):
    # Fonction pour calculer les profondeurs des nœuds dans l'arbre
    def racine(p):
        # Recherche des nœuds où le parent est le même que le nœud lui-même
        racines = [s for s, p in p.items() if s == p]
        # S'il y a une racine, la retourner, sinon None
        return racines[0] if racines else None
    
    s0 = racine(p) # Le sommet s0 est la racine de l'arbre
    profondeur = {}
    profondeur[s0] = 0  # La profondeur de la racine est 0
    pile = [s0]
    traite = set()  # Ensemble pour garder une trace des nœuds déjà traités
    while pile:
        s = pile.pop()
        traite.add(s)  # Marquer le nœud comme traité
        for fils, pere in p.items():
            # Vérifier si le nœud n'a pas été traité
            if pere == s and fils != s and fils not in traite:
                profondeur[fils] = profondeur[s] + 1
                pile.append(fils)
    return profondeur

def haut(p):
    # Fonction pour calculer les hauteurs des nœuds dans l'arbre
    profondeurs = prof(p) # Table des profondeurs
    hauteurs = {} # Table des hauteurs
    
    for s in p:
        hauteurs[s] = 0 # On initialise chaque hauteur à 0
    
    # Inversion des clés et des valeurs de la table des profondeurs
    inversion_profondeurs = {}
    for s, profondeur in profondeurs.items():
        if profondeur not in inversion_profondeurs:
            inversion_profondeurs[profondeur] = [s]
        else:
            inversion_profondeurs[profondeur].append(s)
    
    # Calcul des hauteurs à partir de l'inversion des profondeurs
    for profondeur in sorted(inversion_profondeurs.keys(), reverse=True):
        for s in inversion_profondeurs[profondeur]:
            pere = p[s]
            if s != pere:
                hauteurs[pere] = max(hauteurs[pere], hauteurs[s] + 1)
    
    return hauteurs

def millieu(p):
    # Fonction pour trouver les nœuds qui sont au milieu de l'arbre
    tableMillieu = {}
    profondeurs = prof(p)
    hauteurs = haut(p)
    print("Table des profondeurs:", profondeurs)
    print("Table des hauteurs:", hauteurs)
    for s in p:
        if profondeurs[s] == hauteurs[s]:
            tableMillieu[s] = True
        else:
            tableMillieu[s] = False
    return tableMillieu

# Exemple
p = {
    1: 1,
    2: 1,
    3: 2,
    4: 1,
    5: 4,
    6: 4,
    7: 5,
    8: 5,
    9: 8,
    10: 6,
    11: 10,
    12: 10
}

resultat = millieu(p)
millieu_graphe = [noeud for noeud, est_millieu in resultat.items() if est_millieu]
print(millieu_graphe)