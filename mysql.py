#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shodan
import time
import os
import subprocess
import shutil
import datetime
import sys
import csv
import commands
import re
import operator
import sqlite3
import MySQLdb
import pandas as pd
from sqlalchemy import create_engine

os.system("sudo service mysql start")
os.system("sudo service postgresql start")
os.system("sudo service apache2 start")

filename=('ip_client.csv')

# Lecture du fichier CSV
column_names = ['client', 'ip1', 'ip2', 'ip3', 'ip4', 'ip5', 'ip6', 'ip7', 'ip8', 'ip9', 'ip10']
df = pd.read_csv(filename, header = None, names = column_names)
print(df)


mydb = MySQLdb.connect(host='localhost',user='shodan',passwd='mysql')

cursor = mydb.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS shodan;")

# Fermeture des requettes SQL
cursor.close()

# validation des changements
mydb.commit()

# Déconnexion de la bdd
mydb.close()

# Copie du contenu du CSV dans la BDD
engine = create_engine('mysql://shodan:mysql@localhost/shodan') # Connexion dans la bdd shodan

engine.execute("DROP TABLE IF EXISTS csv;") # Supprimer la table csv si elle existe déjà
df.to_sql('csv', engine, if_exists='append', index=False) # CRéation de la nouvelle table
engine.execute("ALTER TABLE csv ADD id INT AUTO_INCREMENT PRIMARY KEY") # Incrémentation de la table csv
                                                                        # avec les données du fichier csv
engine.select([client]).where(csv.columns.id == '1')
#engine.execute("SELECT client FROM `csv` WHERE id=1")    # res=connection.fetchall()    # print res
# cursor1=mydb.cursor()
# cursor1.execute("SELECT id FROM `csv`")
# result=cursor1.fetchall()
# for row in result:
#     print row[0]
