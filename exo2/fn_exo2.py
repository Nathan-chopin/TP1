# fonction de l'exercice 2 du Tp1
# Nathan Chopin
# 19/09/24


def mesImpots(revenu,x=4):
    print(x)
    plafond = [10225,26070,74545,160336,160337]
    taux = [11,30,41,45,45]
    if revenu <= plafond[0] or x < 0:
        return 0
    elif revenu < plafond[x]:
        print('passe ',plafond[x],taux[x],revenu)
        return mesImpots(revenu,x-1)
    else :
        print('calcul ',plafond[x],taux[x],(revenu - plafond[x]),x)
        return float(mesImpots(revenu - plafond[x],x)) + (revenu - plafond[x]) * (taux[x] / 100)

        