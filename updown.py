import random

nmin = 1
nmax = 99
nkey = random.randint(nmin, nmax)
going_on = True
while(going_on):
    q = input("Entrez un nombre entre " + str(nmin) + " et " + str(nmax) + "\n")
    q = int(q)
    if q == nkey:
        print("C'est gagné !")
        going_on = False
    elif q > nkey:
        print("Trop haut ! Visez plus bas.")
    else:
        print("Trop bas ! Visez plus haut.")
