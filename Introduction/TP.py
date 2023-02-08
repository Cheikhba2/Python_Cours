from random import randrange
# Premier TP: Annee Bisextile
# (Il suffit, en fait, de tester le reste de la division entière de b par a.
# Si ce reste est nul, alors a est un multiple de b.)

# Ma version
"""annee = int(input("saisir votre annee : "))
if annee % 4 and 400 : 
    print("l'annee est bisextile ")
else:
    print("l'annee n'est pas bisextile")"""


# version correction

"""annee = input("Saisissez une année : ") # On attend que l'utilisateur saisisse l'année qu'il désire tester
annee = int(annee)  # Risque d'erreur si l'utilisateur n'a pas saisi un nombre
bissextile = False  # On crée un booléen qui vaut vrai ou faux elle vaut par False
# selon que l'année est bissextile ou non
if annee % 400 == 0:
  bissextile = True
elif annee % 100 == 0:
  bissextile = False
elif annee % 4 == 0:
  bissextile = True
else:
  bissextile = False
if bissextile:  # Si l'année est bissextile
  print("L'année saisie est bissextile.")
else:
  print("L'année saisie n'est pas bissextile.")"""

# version optimisé

# On attend que l'utilisateur saisisse l'année qu'il désire tester

"""annee = int(input("Saisissez une année : "))

if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0) :
    print("L'année saisie est bissextile.")
else:
    print("L'année saisie n'est pas bissextile.")"""


