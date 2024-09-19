# fonction de l'exercice 2 du Tp1
# Nathan Chopin
# 19/09/24


def mesImpots(revenu,x=4):
    '''ne fonctionne pas'''
    plafond = [10225,26070,74545,160336,160337]
    taux = [11,30,41,45,45]
    #print('                    ',revenu)
    if revenu <= plafond[0] or x < 0: 
        return 0
    elif revenu < plafond[x]:
        #print('passe ')
        return mesImpots(revenu,x-1)
    else :
        #print('calcul ',plafond[x],taux[x],revenu,'impots', int(float(mesImpots(revenu - plafond[x],x)) + (revenu - plafond[x]) * (taux[x] / 100)),'reste',(revenu - plafond[x]) )
        return int(float(mesImpots(revenu - plafond[x],x-1)) + (revenu - plafond[x]) * (taux[x] / 100))










def Impots(revenu):
    plafond = [10225,26071,74545,160336,160337]
    taux = [11,30,41,45,45]
    impots = 0
    for i in range(len(plafond)):
        i = (len(plafond)-1) - i
        if revenu >= plafond[i]:
            impots += (revenu - plafond[i]) * (taux[i] / 100)
            revenu = plafond[i] - 1
    return impots