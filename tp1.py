# Nathan CHOPIN
# dossier fonction du TP1
# 17/09/24

def bissextile(annee):
    if annee % 4 or annee % 400 or ( list(str(annee))[0] == '0' and list(str(annee))[1] == '0' ):
        return True
    else:
        return False

