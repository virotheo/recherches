from listes import *
from timeit import timeit

def verification_liste(tab):
    for i in range(len(tab) - 1):
        if tab[i] > tab[i + 1]:
            return False
    return True

def recherches(val,tab):
    if verification_liste(tab) == False:
        return "Cette liste n'est pas bien triée"
    n = len(tab)
    for i in range (0,n):
        if tab [i] == val:
            return True
    return False

def recherche_dichotomique(tab, val):
    if not verification_liste(tab):
        return "Cette liste n'est pas bien triée"
    i = 0
    j = len(tab) - 1

    while i <= j:
        m = (i + j) // 2

        if tab[m] == val:
            return True
        elif tab[m] > val:
            j = m - 1
        else:
            i = m + 1

    return False

print(recherches(2,cree_liste_melangee(10)))
print(recherches(50,cree_liste_croissante(1)))
print(recherches(101,cree_liste_croissante(1)))
print("-----------------")
print(recherche_dichotomique(cree_liste_decroissante(10),5))
print(recherche_dichotomique(cree_liste_croissante(10),5))
print("-----------------")

from timeit import timeit

setup = """
from listes import cree_liste_croissante
from __main__ import recherches, recherche_dichotomique

tab = cree_liste_croissante(1000)
val = 500
"""

t_recherche = timeit(
    stmt="recherches(val, tab)",
    setup=setup,
    number=1000
)

t_dicho = timeit(
    stmt="recherche_dichotomique(tab, val)",
    setup=setup,
    number=1000
)

print("Recherche linéaire :", t_recherche)
print("Recherche dichotomique :", t_dicho)
