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

filename=('ip_client.csv')

mydb = MySQLdb.connect(host='localhost',user='shodan',passwd='mysql')

cursor = mydb.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS shodan")

# Fermeture des requettes SQL
cursor.close()

# validation des changements
mydb.commit()

# Déconnexion de la bdd
mydb.close()

# Lecture du fichier CSV
column_names = ['client', 'ip1', 'ip2', 'ip3', 'ip4', 'ip5', 'ip6', 'ip7', 'ip8', 'ip9', 'ip10']
df = pd.read_csv(filename, header = None, names = column_names)
print(df)

# Copie du contenu du CSV dans la BDD
engine = create_engine('mysql://shodan:mysql@localhost/shodan')
connection=engine.connect()
with connection as conn, conn.begin():
    df.to_sql('csv', conn, if_exists='append', index=False)
    connection.execute("ALTER TABLE csv ADD Id INT AUTO_INCREMENT PRIMARY KEY")
