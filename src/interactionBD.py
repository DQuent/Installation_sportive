#!/usr/bin/env python
#-*- coding: utf-8 -*-

import mysql.connector
import csv
from src.Util_String import *

def connexion():
	"""
	Méthode qui se connecte à la base de donnée E134935T 
	"""
	try :
		global cursor,db
		db = mysql.connector.connect(host="infoweb",user="E134935T",password="E134935T",database="E134935T")
		cursor = db.cursor()
	except ConnexionException as e:
		print("Connexion Exception : "+e)

def deconnexion():
	"""
	Méthode de déconnexion de la base
	"""
	try :
		db.close()
	except ConnexionException as e:
		print("Connexion Exception : "+e)

def affichageMessage(msg):
	print('-------------------------------------------------')
	print(msg)
	print('-------------------------------------------------')

def remplissageTableInstallation(nomFichier) :
	"""
	Méthode qui va parcourir le fichier Installations.csv et qui va remplir la table Installations avec ces données
	"""
	affichageMessage("remplissageTableInstallation start")

	connexion()

	try :
		fichier = open(nomFichier,'r')

		lecteurCsv = csv.reader(fichier, delimiter=',', quotechar='"')

		list_already_added = []

		for row in lecteurCsv:
			if(row[0]!="Nom usuel de l'installation" and row[1] not in list_already_added):
				if(row[1]!=""): 	numero						= row[1] #numero
				else: 				numero						= 'null'
				if(row[0]!=""):		nom 						= "'" + row[0].replace("'","") + "'" #nom
				else: 				nom							= 'null'
				if(row[2]!=""): 	ville						= "'" + row[2].replace("'","")+ "'"#ville
				else: 				ville						= 'null'
				if(row[6]!=""):		numVoie						= row[6].replace("'","")#numVoie pour adresse
				else:				numVoie						= 'null'
				if(row[7]!=""):		nomVoie						= row[7].replace("'","")#nomvoie pour adresse
				else:				nomVoie						= 'null'
				if(row[4]!=""):		codePostal					= "'" + row[4].replace("'"," ") + "'"
				else:				codePostal					= 'null'
				if(row[10]!=""):	latitude					= row[10] 
				else:				latitude 					= 'null'
				if(row[9]!=""):		longitude 					= row[9] 
				else:				longitude 					= 'null'
				if(row[12] !=""):	accesHandiSenso				= "'" + row[12].replace("'"," ") + "'"
				else:				accesHandiSenso				= 'null'
				if(row[11] !=""):	accesHandiMot				= "'" + row[11].replace("'"," ") + "'"
				else:				accesHandiMot				= 'null'

				if(numVoie!='null'): adresse = "'" + numVoie + " "
				else : adresse = "'"
				if(nomVoie!='null'):adresse = adresse + nomVoie + "'"
				else : adresse = 'null'
					
				list_already_added.append(row[1])
				requete="INSERT INTO `Installation`  VALUES (" + numero + "," + Util_String.convertString(nom) + "," + adresse + "," + codePostal + ", " + Util_String.convertString(ville) + ", " + latitude + ", " + longitude + "," + accesHandiSenso+ "," + accesHandiMot +")"
				cursor.execute(requete)

		db.commit()
		deconnexion()

	except ConnexionException as e:
		print("Connexion Exception : "+e)

	affichageMessage("remplissageTableInstallation fini")



def remplissageTableActivite(nomFichier) :
	"""
	Méthode qui va parcourir le fichier Activites.csv et qui va remplir la table Activites avec ces données
	"""
	affichageMessage("remplissageTableActivite start")

	connexion()

	try :
		liste = []

		fichier = open(nomFichier,'r')

		lecteurCsv = csv.reader(fichier, delimiter=',', quotechar='"')

		for row in lecteurCsv:
			if(row[0]!="Code INSEE"):
				if(row[4]!=""): 	numero						= row[4]
				else: 				numero						= 'null'
				if(row[5]!=""):		nom 						= "'" + row[5].replace("'"," ") + "'"
				else: 				nom							= 'null'
				
				if(numero not in liste and numero != 'null'):
					requete="INSERT INTO `Activite`  VALUES (" + numero + "," + Util_String.convertString(nom) +")"
					liste.append(numero)
					cursor.execute(requete)

		db.commit()
		deconnexion()
	except ConnexionException as e:
		print("Connexion Exception : "+e)

	affichageMessage("remplissageTableActivite fini")




def remplissageTableEquipementActivite(nomFichier) :
	"""
	Méthode qui va parcourir le fichier Equipement_Activite.csv et qui va remplir la table Equipement_Activite avec ces données
	"""
	affichageMessage("remplissageTableEquipementActivite start")

	connexion()

	try :
		liste = []

		fichier = open(nomFichier,'r')

		lecteurCsv = csv.reader(fichier, delimiter=',', quotechar='"')

		listeCodes = list()

		for row in lecteurCsv:
			if(row[0]!="Code INSEE"):
				if(row[2]!=""): 	numequip	 			= row[2]
				else: 				numequip	 			= 'null'
				if(row[4]!=""): 	numact	 				= row[4]
				else: 				numact					= 'null'

				if(numequip not in liste and numequip != 'null' and numact != 'null'):
					requete="INSERT INTO `Equipement_Activite`  VALUES (" + numequip + "," + numact + ")"
					liste.append(numequip)
					cursor.execute(requete)

		db.commit()
		deconnexion()
	except ConnexionException as e:
		print("Connexion Exception : "+e)
	affichageMessage("remplissageTableEquipementActivite fin")





def remplissageTableEquipement(nomFichier) :
	"""
	Méthode qui va parcourir le fichier Equipement.csv et qui va remplir la table Equipements avec ces données
	"""
	affichageMessage("remplissageTableEquipement start")
	
	connexion()

	try :
		fichier = open(nomFichier,'r')

		lecteurCsv = csv.reader(fichier, delimiter=',', quotechar='"')

		liste = []

		for row in lecteurCsv:
			if(row[0]!="ComInsee"):
				if(row[4]!=""): 	numero	 			= row[4]
				else: 				numero	 			= 'null'
				if(row[5]!=""): 	nom	 				= "'"+row[5].replace("'"," ")+"'"
				else: 				nom	 				= 'null'
				if(row[0]!=""): 	numinst	 			= row[2]
				else: 				numinst		 		= 'null'
				if(row[19]!=""): 	sallePoly	 	    = "'"+row[19].replace("'"," ")+"'"
				else: 				sallePoly	 		= 'null'
				if(row[16]!=""): 	eclairage	 	    = "'"+row[16].replace("'"," ")+"'"
				else: 				eclairage	 		= 'null'
				if(row[28]!=""): 	couverture	 	    = "'"+row[28].replace("'"," ")+"'"
				else: 				couverture	 		= 'null'

				if(numero not in liste and numero != 'null'):
					requete="INSERT INTO `Equipement`  VALUES (" + numero + "," + Util_String.convertString(nom) + "," + numinst + "," + sallePoly+ ","+ eclairage + "," + couverture + ")"
					liste.append(numero)
					cursor.execute(requete)

		db.commit()
		deconnexion()
	except ConnexionException as e:
		print("Connexion Exception : "+e)
	affichageMessage("remplissageTableEquipement fini")

def getRequete(requete):
	"""
	Méthode qui va exécuter la requête mise en paramètre
	"""
	try:
		connexion()
	except ConnexionException as e:
		print("Connexion Exception : "+e)
	try:
		cursor.execute(requete)

		data = cursor.fetchall()

		deconnexion()

		return data
	except SQLResquestFail as e:
		print("SQLResquestFail Exception : "+e)
	

