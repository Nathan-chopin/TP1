# Nathan CHOPIN
# dossier fonction du TP1
# 17/09/24

def bissextile(annee):
    if annee % 400 or ( annee % 4 or not ( list(str(annee))[3] == '0' and list(str(annee))[2] == '0' ) ):
        return True
    else:
        return False

def nombre_jour(mois,annee):
    bool_bissextile = bissextile(annee)
    x = 0
    if bool_bissextile == True:
        x = 1      #valeur qui fera varier le nombre de jour de février
    if mois == 2:
       return 28 + x
    elif mois % 2 == 0 :
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
    