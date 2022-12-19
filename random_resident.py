import random
from modules.resident import Patient
from modules.resident import RH
from modules.administration import Archive

f_p = open("prenom.txt", "r") ### Ouvre le fichier prénom
# print(f_p.read()) 

f_n = open("nom.txt", "r") ### Ouvre le fichier nom

l_f_p = f_p.readlines() ### Lit les lignes du fichier prénom

l_f_n = f_n.readlines() ### Lit les lignes du fichier nom

i_f_p = len(l_f_p) ### Indique le nombre de prénom

i_f_n = len(l_f_n) ### Indique le nombre de nom

rand_prenom = random.randint(0,i_f_p) ### Choisit un prénom au hasard

rand_nom = random.randint(0,i_f_n) ### Choisit un nom au hasard

def date_rnd(): ### Fonction pour choisir une date au harsard dans l'année 2022
    year = 2022
    month = random.randint(1,12)
    if month == (1,3,5,7,8,10,12):
        day = random.randint(1,31)
    elif month == 2:
        day = random.randint(1,28)
    else:
        day = random.randint(1,30)
    return f"{year}-{month}-{day}"

def sang(): ### Fonction pour choisir le groupe sangain au hasard
    Group = ["O", "A", "B", "AB"]
    Signe = ["+","-"]
    return (Group[random.randint(0,3)]+Signe[random.randint(0,1)])
    
### Info de connexion pour la BDD

connection_config = {
    "host" : "localhost",
    "user" :"py",
    "password":"python",
    "auth_plugin" : "mysql_native_password",
    "database" : "CHU_Caen",
    "port" : "3308"        
}


for i in range(1,50):
    rand_prenom = random.randint(0,i_f_p-1)
    rand_nom = random.randint(0,i_f_n-1)
    personne = l_f_n[rand_nom].replace("\n", ""), l_f_p[rand_prenom].replace("\n", "")
    date_rnd()
    globals()['rh%s' % i] = RH(personne[0],personne[1],random.randint(18,70),sang(),date_rnd(),random.randint(1,999)) ### Chose à éviter mais créé une variable selon la boucle i (rh1, rh2, rh3, ...) pour regrouper toutes les infos pour créer l'objet i de la class RH
    Archive.enregister_archive_en_base("rh",(globals()['rh%s' % i]).debut_CDD_CDI()) ### Enregistre tous les faux RH dans la BDD