#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

#Importation des bibliothèques nécessaires
import shodan
import time
import os
import subprocess
import shutil
import commands
import commands
import datetime
import sys
import re
import operator
import sqlite3

global adresse_ip
def clear():
    print "\n" * 80
def option1():
	print("Option 1 sélectionné\n")
	#File_IP=input("veuillez entrer le nom de votre csv contenant le nom des clients et leurs adresses ip publiques:\n") pour permettre la lecture du fichier, on rentre son nom
	#scan( --fields ip_str,port,org --separator , 'File_IP'
	#Alerte_csv(File_IP)#le nom du fichier est passe en parametre de la fonction, besoin d'un compte premium
def option2():
    def compare():
        alerte= ("Alerte::%s.txt" %Current_Date) # Variable qui contient le format de nom pour le fichier d'alerte
        File1 = ('%s.log' %Previous_Date) # Fichier de le veille
        commands.getoutput('find / -name %s >findme.txt' %File1) # cherche si le fichier de la veille existe
        if os.path.getsize('findme.txt') == 0: # Si le find n'a rien trouvé
            os.remove('findme.txt') # on supprime le fichier temporaire
            print("Il n'y a pas de fichier de scan de la veille.")
        else:
            File2 = ('%s.log' %Current_Date) # Fichier d'aujourd'hui

            old_lines = file(File1).read().split(' ')
            new_lines = file(File2).read().split(' ')

            # Tout le contenu devient une string
            old_lines_set = set(old_lines)
            new_lines_set = set(new_lines)
            # Comparaison
            old_added = old_lines_set - new_lines_set
            old_removed = new_lines_set - old_lines_set

            if old_lines_set == new_lines_set: # S'il n'y a pas de changement entre les deux scans
                print ("")
                print ("le fichier de la veille être supprimé")
                commands.getoutput('rm %s' %File1) # Suppression du fichier de la veille

            # boucle for pour seulement garder les éléments qui ont changé
            sys.stdout=open(alerte,"w") # Toute les sorties qui seront entre cette ligne et sys.stdout.close() seront écrites dans le fichier de la variable alerte
            for line in old_lines:
                if line in old_added:
                    print '-', line.strip()
                elif line in old_removed:
                    print '+', line.strip()
            for line in new_lines:
                if line in old_added:
                    print '-', line.strip()
                elif line in old_removed:
                    print '+', line.strip()
            sys.stdout.close()

    adresse_ip=raw_input("Veuillez enrter une adresse IP cible: ")
    loop=True
    while loop:
    	print ("\n")
        Current_Date = datetime.datetime.today().strftime ('%d-%m-%Y::%H:%M') # Récupératino de la date du jour sour le format entre ""
        yesterday = datetime.datetime.today() - datetime.timedelta(days=1) # La veille = jour - 1
        Previous_Date = yesterday.strftime ('%d-%m-%Y::%H:%M')
        commands.getoutput('shodan host %s >%s.log' %(adresse_ip, Current_Date)) # Excécution de la commande de scan shodan
        content=commands.getoutput('cat %s.log' %Current_Date)
        print content
        compare()
        time.sleep(86400) # temps d'attente en seconde, 86400s pour 24h
def option3():
	#Mettre tout le code de l'option 3
	print("Option 3 sélectionné\n")
def option4():
	#Mettre tout le code de l'option 4
	print("Option 4 sélectionné\n")
def changer_api():
	print "Précision: le fichier qui contient la clef est enregistré par défaut dans le même répertoire que le script."
	print ("\n")
	SHODAN_API_KEY=raw_input("Veuillez indiquer une nouvelle clef API: ")
	while SHODAN_API_KEY=="":
		SHODAN_API_KEY=raw_input('\nVeuillez entrer une clef valide: ') # Tant qu'on n'a pas entré de clef
		print ("\n")
	f=open('api_key.txt','w') # Ouverture ou création du fichier api_key.txt en mode écriture ("w")
	f.write(SHODAN_API_KEY) # On écrit dans le fichier la clef API
	f.close() # Puis on ferme le fichier
	print ("La clé API a bien été remplacée!")
	print ("\n")
	api = shodan.Shodan(SHODAN_API_KEY) # Et on implémante la clef API avec la commande Shodan
def sortie():
	print("A bientôt!!\n")
def changer_repertoire_api():
	loop=True
	print("\n")
	while loop:
	    rinit=raw_input("Veuillez indiquer le chemin du fichier api_key.txt: ")
	    print("\n")
	    isExist = os.path.exists(rinit)
	    if isExist==True: # Si le chemin du fichier api existe
	        print("Chemin trouvé!")
	        print("\n")
	        rdest=raw_input("Ou voulez-vous déplacer le fichier (indiquer le répertoire sans le nom du fichier AVEC le / à la fin): ")
	        print("\n")
	        isExiste = os.path.exists(rdest) # Si le chemin de destination existe
	        if isExiste==True:
	            print("Répertoire ou chemin trouvé!")
	            print("\n")
	            shutil.move(rinit, rdest+'api_key.txt') # On déplace le fichier de la clef
	            if os.path.exists(rdest+'api_key.txt')==True: # Si le fichier a bien été déplacé
	                print("Le fichier a été déplacé avec succès!")
	                loop=False # On arrete la boucle
	        else:
	            print("Répertoire inconnu... Attention aux / et aux accents s'il y en a") # Affichage d'un message d'erreur
	            print("\n")
	            loop=False # on arrete la boucle
	    else:
	        print("Répertoire inconnu... Attention aux / et aux accents s'il y en a") # Affichage d'un message d'erreur
	        print("\n")
	        loop=False # on arrete la boucle

clear()
print 30 * "-" , "SHODAN AUTOMATIC SCRIPT" , 30 * "-"
if os.stat("api_key.txt").st_size == 0:
	print "Attention: aucune clef API est enregistrée dans api_key.txt, veuillez d'abbord en ajouter une."
	print ("\n")
	changer_api()

def main_menu():
	print 83 * "-"
	print " Que voulez vous faire:"
	print "1. Ajouter une alerte en fonction d\'une liste"
	print "2. Ajouter une alerte en fonction d\'une adresse ip"
	print "3. Faire un scan sur les bases de donnees shodan (rapport xlsx)"
	print "4. Obtenir des informations sur une adresse ip ayant ete repertorie par shodan (rapport xlsx)"
	print "5. Changer/ajouter la clé API (api_key.txt)"
	print "6. Déplacer le fichier de sauvegarde de la clef API"
	print "99. Sortir"
	print 83 * "-"

loop=True

while loop:
	f=open('api_key.txt','r')
	str=f.read()
	f.close()
	SHODAN_API_KEY=str
	api = shodan.Shodan(SHODAN_API_KEY)
	main_menu()    ## afficher le menu
	choice=int(input("Entrer la valeur correspondant à votre choix [1-6/99]: "))
	if choice==1:
		option1() # Appel de la fonction "option1"
	elif choice==2:
		option2()
	elif choice==3:
		option3()
	elif choice==4:
		option4()
	elif choice==5:
		changer_api()
	elif choice==6:
		changer_repertoire_api()
	elif choice==99:
		sortie()
		loop=False
	else:
		raw_input("La saisie est incorrecte, veuillez choisir un numéro entre 1 et 5, ou bien 99 pour sortir.")
