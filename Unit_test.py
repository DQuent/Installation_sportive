####################################################################
#Ce fichier permet d'effectuer les tests Unitaires de l'application#
####################################################################


from src.interactionBD import *
 
#TEST DE L IMPORTATION DU FICHIER INSTALLATIONS.CSV
assert getRequete("SELECT COUNT(*) FROM Installation") == 2  # test de l'addition