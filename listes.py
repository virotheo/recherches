

#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod: module
:author: FIL - FacultÃ© des Sciences et Technologies -  Univ. Lille <http://portail.fil.univ-lille1.fr>_
:date: avril 2019

Diverses fonctions de crÃ©ation de listes d'entiers

"""
import random

def cree_liste_croissante(n):
    '''
    :param n: (int) nombre d'entiers souhaitÃ©s
    :return: (list) liste des entiers de 0 Ã  n - 1
    :CU: aucune (si n <= 0, la liste obtenue est vide)
    :Exemples:

    >>> cree_liste_croissante(6)
    [0, 1, 2, 3, 4, 5]
    >>> cree_liste_croissante(0)
    []
    '''
    return [k for k in range(n)]


def cree_liste_decroissante(n):
    '''
    :param n: (int) nombre d'entiers souhaitÃ©s
    :return: (list) liste des entiers de n - 1 Ã  0
    :CU: aucune (si n <= 0, la liste obtenue est vide)
    :Exemples:

    >>> cree_liste_decroissante(6)
    [5, 4, 3, 2, 1, 0]
    >>> cree_liste_decroissante(0)
    []
    '''
    return [(n - 1 - k) for k in range(n)]

def cree_liste_melangee(n):
    '''
    :param n: (int) nombre d'entiers souhaitÃ©s
    :return: (list) liste des entiers de n - 1 Ã  0
    :CU: aucune (si n <= 0, la liste obtenue est vide)
    :Exemples:

    >>> n = 6
    >>> l = cree_liste_melangee(n)
    >>> len(l) == n
    True
    >>> all(k in l for k in range(n))
    True
    '''
    #l=[1,3,6,8]
    l = cree_liste_croissante(n)
    random.shuffle(l)
    return l

def cree_liste_melangee2(n, maxi):
    '''
    :param n: (int) nombre d'entiers souhaitÃ©s
    :param maxi: (int) valeur maximale des entiers souhaitÃ©s
    :return: (list) liste de n entiers choisis au hasard entre 0 et maxi (inclus)
    :CU:  maxi >= 0 (si n <= 0, la liste obtenue est vide)
    :Exemples:

    >>> n = 6
    >>> maxi = 10
    >>> l = cree_liste_melangee2(n, maxi)
    >>> len(l) == n
    True
    >>> all(0 <= k <= maxi for k in l)
    True
    '''
    return [random.randrange(maxi + 1) for _ in range(n)]

if __name__ == '__main__':
   import doctest
   doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)


