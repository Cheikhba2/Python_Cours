import turtle
from email.message import EmailMessage
# Varibales comprehension
"""mon_age = 21
mon_age = mon_age + 5
print(mon_age)


# Premier exemple de condition
a = 5
if a > 0:  # Si a est supérieur à 0
    print("a est supérieur à 0.")


a = 5
b = 8
if a > 0:
    b += 1  # On incrémente la valeur de b c'est à dire qu'on rajoute 1
    print("a =", a, "et b =", b)  # On affiche les valeurs des variables


age = 21
if age >= 18:  # Si age est supérieur ou égal à 18
    print("Vous êtes majeur.")
else:  # Sinon (age inférieur à 18)
    print("Vous êtes mineur.")


a == 0  # ca donne True ou Flase
if a > 0:
    print("a est superieur à 0")
elif a < 0:
    print("a est inferieur à 0")
elif a == 0:
    print("a est égale à 0")
else:
    print("a est nul")


print(4 == 4)  # True


a = 5  # c'est valide mais trés lourd en ligne de code
if a >= 2:
    if a <= 8:
        print("a est dans l'intervalle.")
    else:
        print("a n'est pas dans l'intervalle.")
else:
    print("a n'est pas dans l'intervalle.")

a = 5
if a < 2 or a > 8:  # utilisation de l'opérateur and qui reduit les lignes de code
    print("a est dans l'intervalle.")
else:
    print("a n'est pas dans l'intervalle.")"""

# Exmeple d'utilisation des boucles

"""print("1 * 7 =", 1 * 7)
print(" 2 * 7 =", 2 * 7)
print(" 3 * 7 =", 3 * 7)
print(" 4 * 7 =", 4 * 7)
# cette exemple peut etre optomisé par l'utilisation des boucles
print(" 5 * 7 =", 5 * 7)
print(" 6 * 7 =", 6 * 7)
print(" 7 * 7 =", 7 * 7)
print(" 8 * 7 =", 8 * 7)
print(" 9 * 7 =", 9 * 7)
print("10 * 7 =", 10 * 7)"""


"""nb = int(input("saisissez un nombre : "))
i = 0  # C'est notre variable compteur que nous allons incrémenter dans la boucle

while i < 10:  # Tant que i est strictement inférieure à 10
    print(i + 1, "*", nb, "=", (i + 1) * nb)
    i += 1  # On incrémente i de 1 à chaque tour de boucle"""

# exemple d'utilisation de l'instruction for
"""chaine = "Bonjour les ZER0S"
for lettre in chaine:
    print(lettre)"""

"""chaine = "Bonjour les ZER0S"
for lettre in chaine:
    if lettre in "AEIOUYaeiouy":  # lettre est une voyelle
        print(lettre)
else:  # lettre est une consonne... ou plus exactement, lettre n'est pas une voyelle
    print("*")"""

# utilisation de break

"""while 1:  # 1 est toujours vrai -> boucle infinie
    lettre = input("Tapez A pour quitter : ")
    if lettre == 'A':
        print("Fin de la boucle")
        break"""

# Utilisation du mot clef continue

"""i = 1
while i < 20:  # Tant que i est inférieure à 20
    if i % 3 == 0:
        i += 4  # On ajoute 4 à i
        print("On incrémente i de 4. i est maintenant égale à", i)
        continue  # On retourne au while sans exécuter les autres lignes
    print("La variable i =", i)
    i += 1  # Dans le cas classique on ajoute juste 1 à i"""


# Création de fonction

"""def table_de_7():
    nb = 7
    i = 0  # Notre compteur ! L'auriez-vous oublié ?
    while i < 10:  # Tant que i est strictement inférieure à 10,
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1  # On incrémente i de 1 à chaque tour de boucle
table_de_7()"""


"""def table(nb): # (def table(nb, max):) plusieurs parametres autre possibilité
    i = 0
    # Tant que i est strictement inférieure à 10, (while i < max)
    while i < 10:
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1  # On incrémente i de 1 à chaque tour de boucle.

table(11) # pour appeler la fonction """


# def table(nb, max=10):  # valeur par defaut de max
#   """Fonction affichant la table de multiplication
# par nb de 1*nb à max*nb
# (max >= 0) """  # ceci est un docstring
# i = 0
# while i < max:
# print(i + 1, "*", nb, "=", (i + 1) * nb)
# i += 1


# table(5)

# table(10)

# appel de la fonction suivant les valeurs qu'on veeut en parametre
# def fonc(a=1, b=2, c=3, d=4, e=5):

#  print("a =", a, "b =", b, "c =", c, "d =", d, "e =", e)


# fonc(a=9, b=78)

# utilisation de try et except (forme imple)
"""annee = input("saisir une annee  ")
try:  # On essaye de convertir l'année en entier
    annee = int(annee)
except:
    print("Erreur lors de la conversion de l'année.")"""


# forme complete de try et except
"""try:
    resultat = numerateur / denominateur
except NameError:
    print("La variable numerateur ou denominateur n'a pas été définie.")
except TypeError:
    print("La variable numerateur ou denominateur possède un type incompatible avecla division.")
except ZeroDivisionError:
    print("La variable denominateur est égale à 0.")"""

# les mots clefs else et finnaly dans le bloc try except (exemple d'utilisation)
"""try:
    resultat = numerateur / denominateur
except NameError:
    print("La variable numerateur ou denominateur n'a pas été définie.")
except TypeError:
    print("La variable numerateur ou denominateur possède un type incompatible avecla division.")
except ZeroDivisionError:
    print("La variable denominateur est égale à 0.")
else:
    print("Le résultat obtenu est", resultat)"""


# Assertion
"""annee = input("Saisissez une année supérieure à 0 :")
try:
    annee = int(annee)  # Conversion de l'année
    assert annee > 0
except ValueError:
    print("Vous n'avez pas saisi un nombre.")
except AssertionError:
    print("L'année saisie est inférieure ou égale à 0.")"""

# lever une exception
"""annee = input()  # L'utilisateur saisit l'année
try:
    annee = int(annee)  # On tente de convertir l'année
    if annee <= 0:

        # lever une exception grâce au mot-clé raise
        raise ValueError("l'année saisie est négative ou nulle")

except ValueError:
    print("La valeur saisie est invalide (l'année est peut-être négative).")"""


"""Parité."""

# Programme principal =========================================================
"""n = int(input("Entrez un entier strictement positif :"))
while n < 1:
    n = int(input("Entrez un entier STRICTEMENT POSITIF, s.v.p. :"))

if n % 2 == 0:
    print(n, "est pair.")
else:
    print(n, "est impair.")"""

import pandas 