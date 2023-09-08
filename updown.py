import random

# test command 2

path_tries = '.nbt'
path_games = '.nbp'

nbt = 0
nbp = 0
nmin = 1
nmax = 99
play_again = True

print("Plus petit ou plus grand")

while play_again:
    # create save files, or read those if they exist
    with open(path_tries, 'a+', encoding="utf-8") as f:
        rr = f.read()
        if len(rr.strip()) > 0: # something is stored
            nbt = int(rr.strip())
        else: # store the initial (0)
            f.write(str(nbt))
        f.close()
    with open(path_games, 'a+', encoding="utf-8") as f:
        rr = f.read()
        if len(rr.strip()) > 0: # something is stored
            nbp = int(rr.strip())
        else: # store the initial (0)
            f.write(str(nbp))
        f.close()
    if nbp > 0:
        print("Nombre de parties : " + str(nbp) + " | Ratio : " + str(nbt / nbp))
    nkey = random.randint(nmin, nmax)
    going_on = True
    t = 0
    while(going_on):
        t += 1
        q = input("Entrez un nombre entre " + str(nmin) + " et " + str(nmax) + "\n")
        q = int(q)
        if q == nkey:
            print("C'est gagné !")
            going_on = False
        elif q > nkey:
            print("Trop haut ! Visez plus bas.")
        else:
            print("Trop bas ! Visez plus haut, genre la lune.")
    nbt += t
    nbp += 1
    # save scores
    with open(path_tries, 'w', encoding="utf-8") as f: # empty file
        f.write(str(nbt))
        f.close()
    with open(path_games, 'w', encoding="utf-8") as f:
        f.write(str(nbp))
        f.close()
    print("Nombre de parties : " + str(nbp) + " | Ratio : " + str(nbt / nbp))
    doitagain = ''
    while doitagain != 'Q' and doitagain != 'R':
        doitagain = input("Voulez-vous [R]ejouer ou [Q]uitter ?").upper()
    if doitagain == 'Q':
        play_again = False
print("Allez, bisoux, hein !")
