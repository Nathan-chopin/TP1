# fonction de l'exercice 4  du tp1
# Nathan Chopin
# 19/09/24


tour_A = [1,2,3,4,5]
tour_B = [0,0,0,0,0]
tour_C = [0,0,0,0,0]

def Hanoi(départ,arrivée):
    plot = 0
    deplacement_possible = True
    if départ == arrivée:               #arrivée différente du départ
        print("ce mouvement est nul")
        return False
    
    for i in range(len(départ)):  #y a t-il un plot au départ
        if départ[i] != 0:
            x = départ[i]
        else :
            print("ERREUR : il n'y a pas de plot dans cette tour !")
            return False
    
    if 0 not in arrivée:   #y a-t-il de la place pôur le plot à l'arrivée
        print("il n'y a pas de place pour ce plot à l'arrivée")
        return False
    
    for i in range(len(arrivée)):
        if plot > arrivée[i] and arrivée[i] == 0:
            print('le plot sur la tour est plus petit que celui qui vous déplacez')
            return False
    
    
