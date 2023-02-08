def table(nb, max=10):  # valeur par defaut de max
    """Fonction affichant la table de multiplication
par nb de 1*nb à max*nb
(max >= 0) """  # ceci est un docstring
    i = 0
    while i < max:
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1


if __name__ == "__main__":
    table(4)
