# dossier de foction du TP1
# Nathan CHOPIN
# 17/09/24

def bissextile(annee):
    '''condition 1: multiple de 400 OU condition 2: multiple de 4 si ne termine pas par 00'''
    if annee % 400 or ( annee % 4 or not ( list(str(annee))[3] == '0' and list(str(annee))[2] == '0' ) ):
        return True
    else:
        return False

def nombre_jour(mois,annee):
    bool_bissextile = bissextile(annee)
    x = 0
    if bool_bissextile == True:
        x = 1      #valeur qui fera varier le nombre de jour de février
    if mois == 2:  #si mois de février
       return 28 + x
    elif mois % 2 == 0 : #selon mois pair ou impair sans le 2 (traité précédement)
        return 30
    else :
        return 31

def vérification_date(jour,mois,annee):
    if mois < 1 or mois > 12:
        return False
    elif jour > nombre_jour(mois,annee) or jour < 0:
        return False
    else :
        return True

def explane(bool_valide):
    '''transforme le bool issue de vérification_date(j,m,a) en les str suivant'''
    if bool_valide:
        return "date valide"
    else :
        return "date non valide"

