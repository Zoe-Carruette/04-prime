""" Main --> Calcul d'un nombre premier"""
from math import sqrt

#### Fonction secondaire


def isprime(p):
    """
    Vérifie si un nombre est premier.
    
    Paramètre:
    p (int): Le nombre à vérifier.

    Returns:
    bool: True si p est premier, False sinon.
    """
    # votre code ici
    premier=True
    if p==1:
        premier = False
    for i in range (2,int(sqrt(p))+1):
        if p%i == 0:
            premier=False
            break
    return premier

#### Fonction principale


def main():
    """
    La fonction principale qui teste des nombres premier de 1 à 100 et les affiches.
    """
    # vos appels à la fonction secondaire ici
    isprime(3)
    isprime(22)
    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
