# main/script et test de l'exercice 1 du TP1
# Nathan CHOPIN
# 19/09/24

import tp1 as fn

print( '\n test de la fonction bissextil :')

print('L\'annee 2023 est t elle bissextil ? :',fn.bissextile(2023))
print('L\'annee 2000 est t elle bissextil ? :',fn.bissextile(2000))

print( '\n test de la fonction nombre de jour dans le mois:')

print('L\' pour l\'année 2023 le mois février avais :',fn.nombre_jour(2,2023) ,' jours')
print('L\' pour l\'année 2000 le mois février avais :',fn.nombre_jour(2,2000),' jours')

print( '\n test de la vérification de la date:')

print('La date du 36/02/549 est une' ,fn.explane(fn.vérification_date(36,2, 546)))
print('La date du 17/09/2024 est une',fn.explane(fn.vérification_date(17,9,2024)))




