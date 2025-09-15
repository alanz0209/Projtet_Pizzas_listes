from typing import Collection

#def tri_personnalise(e):
 #   return len(e)

def afficher_pizzas(collection, nb_premiers_elements=-1):
    c = collection
    if not nb_premiers_elements == -1:
        c =collection[:nb_premiers_elements]
    #collection.sort(reverse=True,key= tri_personnalise)
    nb_pizzas = len(c)
    if nb_pizzas == 0:
        print("AUCUNE PIZZA")
        return

    print(f"---- LISTE DES PIZZAS ({nb_pizzas}) ----")
    for i in c:
        print(i)
    print()

    print(f"Première pizza: {c[0]}")
    print(f"Dernière pizza: {c[-1]}")


def ajouter_pizza_utilisateur(c):
    p = input("Pizza à ajouter: ")
    if p.lower() in c:
        print("ERREUR!: La pizza existe déjà")
    else:
        c.append(p)

"""
def pizza_existe(e, collection):
    for i in collection:
        if e == i:
            return True
    return False
"""



pizzas = ["4 fromages", "végétarienne", "hawai", "calzonne"]


ajouter_pizza_utilisateur(pizzas)
afficher_pizzas(pizzas, 2)



















