#!/usr/bin/env python
#-*- coding: utf-8 -*-

from libs.bottle import *
import mysql.connector
from src.interactionBD import *
from src.Exceptions.ConnexionException import *
from src.Exceptions.SQLResquestFail import *
from src.Util_String import *

##################
#    ROUTING     #
##################

@route('/static/<filepath:path>')
def file_stac(filepath):
  	return static_file(filepath,root="./static")

@route('/')
@view('template/index.tpl')
def index():
	"""
	Méthode qui va charger la page d'acceuil de l'application
	"""
	context = template('template/index')
	return (context)

@route('/search',method='POST')
@view('template/result.tpl')
def search():
	"""
	Méthode qui va exécuter une requête SQL et redirigé l'utilisateur en fonction du remplissage du formulaire de la page d'acceuil
	"""
	#On recupere le champ ville
	ville = Util_String.convertString(request.forms.get('ville'))

  	#On recupere le champ sport
	sport = Util_String.convertString(request.forms.get('sport'))

	#Si les deux champs sont renseignes
	if sport != '' and ville != '':
		print('2 champs renseignes')
		requeteFinale = ''.join(["select DISTINCT i.numero, i.nom, e.numero, e.nom, a.numero, a.nom FROM Installation i JOIN Equipement e ON i.numero = e.numinst JOIN Equipement_Activite ea ON e.numero = ea.numequip JOIN Activite a ON ea.numact = a.numero WHERE i.ville = '",str(ville),"' AND a.nom LIKE '%",str(sport),"%' "]) 
		print(requeteFinale)
		result = getRequete(requeteFinale)
		print(result)
		# Valeur de view si SPORT ET VILLE
		view=1

	#Sinon si ville renseigne	
	elif ville != '':
		print('ville renseignes')
		requeteFinale = ''.join(["select DISTINCT a.nom FROM Installation i JOIN Equipement e ON i.numero = e.numinst JOIN Equipement_Activite ea ON e.numero = ea.numequip JOIN Activite a ON ea.numact = a.numero WHERE i.ville = '",str(ville),"'"])
		print(requeteFinale)
		result = getRequete(requeteFinale)
		# Valeur de view si QUE VILLE
		view=2

	#Sinon si sport renseigne	
	elif sport != '':
		print('sport renseignes')
		requeteFinale = ''.join(["select DISTINCT i.ville from Installation i, Equipement e, Equipement_Activite ea, Activite a WHERE i.numero=e.numinst and e.numero=ea.numequip and ea.numact=a.numero and a.nom LIKE '%",str(sport),"%'"])
		print(requeteFinale)
		result = getRequete(requeteFinale)
		# Valeur de view si QUE SPORT
		view=3 

	context = template('template/result',rows=result,ville=ville,sport=sport,view=view)
	return (context)


@route('/map')
@view('template/map.tpl')
def map():
	"""
	Méthode qui va charger la page qui contient la google map
	"""
	context = template('template/map')
	return (context)

@route('/map2',method='POST')
@view('template/map2.tpl')
def map():
	"""
	Méthode qui va récupéré les coordonnées de la ville mise dans le formulaire, et l'afficher avec la map
	"""
	ville = Util_String.convertString(request.forms.get('ville'))
	loc = []
	if ville !='':
		requeteFinale = ''.join(["select distinct i.latitude, i.longitude FROM Installation i, Activite a, Equipement e, Equipement_Activite ea WHERE a.numero=ea.numact And ea.numequip=e.numero And e.numinst=i.numero And i.ville ='",str(ville),"'"]) 
		result = getRequete(requeteFinale);
		for row in result:
			loc.append(row)


	context = template('template/map2',locs=loc)
	return (context)


run(host='localhost', port=8080, reloader=True)