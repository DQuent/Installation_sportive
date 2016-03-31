#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.interactionBD import *
from src.Exceptions.ConnexionException import *
from src.Exceptions.SQLResquestFail import *
import mysql.connector
import csv


#-----------------------------#
#		MAIN Remplissage      #
#-----------------------------#

db = mysql.connector.connect(host="infoweb",user="E134935T",password="E134935T",database="E134935T")
cursor = db.cursor()

cursor.execute("DELETE FROM `Installation` WHERE 1")
cursor.execute("DELETE FROM `Activite` WHERE 1")
cursor.execute("DELETE FROM `Equipement_Activite` WHERE 1")
cursor.execute("DELETE FROM `Equipement` WHERE 1")
db.commit()
db.close()

print('-------------------------------------------------')
print("|                  drop fini                    |")
print('-------------------------------------------------')

remplissageTableInstallation('csv/Installations.csv')
print('-------------------------------------------------')
print("|      TableInstallation                        |")
print('-------------------------------------------------')
remplissageTableActivite('csv/Activites.csv')
print('-------------------------------------------------')
print("|       TableActivite                           |")
print('-------------------------------------------------')
remplissageTableEquipementActivite('csv/Activites.csv')
print('-------------------------------------------------')
print("|        EquipementActivite                      |")
print('-------------------------------------------------')
remplissageTableEquipement('csv/Equipements.csv')
print('-------------------------------------------------')
print("|        TableEquipement                        |")
print('-------------------------------------------------')