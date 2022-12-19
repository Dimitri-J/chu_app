import sys
from modules.resident import Patient
from modules.resident import RH
from modules.administration import Archive
import streamlit as st
import pandas as pd

### Indique la configuration de connexion pour la BDD
connection_config = {
    "host" : "localhost",
    "user" :"py",
    "password":"python",
    "auth_plugin" : "mysql_native_password",
    "database" : "CHU_Caen",
    "port" : "3308"        
}

if __name__ == '__main__':

    st.title("CHU CAEN") ### Un titre
    genre = st.radio("Patient ou Résident", options=('Patient', 'Résident'),label_visibility="hidden",horizontal=True) ### Un sélecteur entre Patient et Résident
    out = st.checkbox("Présence de la personne à l'hospital", value=False) ### Une case pour dire si la personne est encore à l'hospital ou pas
    nom = st.text_input("Nom") ### Le champ nom
    prenom = st.text_input("Prénom") ### Le champ prénom
    age = st.number_input("Age", step=1) ### Le champ âge
    group_sang = st.selectbox("Groupe sanguain", options=('A+','A-','B+','B-','AB+','AB-','O+','O-')) ### Le champ groupe sanguain
    if genre=='Patient': ### Code à éxécuter si c'est un patient
        date_in = st.date_input("Date d'hospitalisation") ### Le champ date entrée du patient
    else: ### Si résident
        date_in = st.date_input("Date début contrat") ### Le champ date entrée du résident
        salaire = st.number_input("Salaire horaire", step=1) ### Le champ salaire du résident
    if genre=='Résident' and out==False: ### Code si résident plu présent à l'hospital
        date_out = st.date_input("Date sortie hospitalisation") ### Le champ de la date de fin de contrat
    col1, col2, col3 = st.columns(3) ### Streamlit sépare la page en 3 colonnes
    error = "" ### Erreur vide
    with col1: ### Colonne de gauche affiche le bouton Submit pour envoyer les infos à la BDD
        if st.button('Submit'):
            if genre=='Patient':
                
                personne = Patient(nom,prenom,age,group_sang,str(date_in))
                if  out==True:
                    try:
                        if Archive.enregister_archive_en_base("patients",personne.entree_hopital())==False:
                           error = ("Vérifier les informations") 
                        
                    except:
                            error = ("Vérifier les informations")
                            print("WTF1")
                else:
                    try:
                        Archive.update_patient_en_base(personne.sorti_hopital())
                    except:
                            error = ("Vérifier si le patient a bien été enregistré avant sa sortie")
                            print("WTF2")
            else:
                personne = RH(nom, prenom, age, group_sang, str(date_in), salaire)
                if  out==True:  
                    try:
                        if Archive.enregister_archive_en_base("rh",personne.debut_CDD_CDI()) == False:
                            error = ("Vérifier les informations")
                    except:                        
                            error = ("Vérifier les informations")
                            print("WTF3")
                else:
                    try:
                        if Archive.update_archive_en_base(personne.fin_CDD_CDI(date_out)) == False:
                            error = ("Vérifier les informations")
                    except:                          
                            error = ("Vérifier si le patient a bien été enregistré avant sa sortie")
                            print("WTF4")
    
    
    placeholder = st.empty() ### Prépare un espace qui peux afficher qu'un seul élément
    with placeholder.container(): 
        with col2: ### Affiche sur la colonne du milieu le bouton pour afficher la tâble archive
            if st.button('Show'):
                df = pd.DataFrame(Archive.afficher_les_archives_streamlit(),columns=('Identifiant Résident','Date entrée','Date Sortie'))
                df.fillna('', inplace=True)
                placeholder.dataframe(df,use_container_width=True)
    placeholder2 = st.empty()
    placeholder2.title(error) ### Affiche une erreur si il manque un champ ou si le patient ou résident existe déjà dans la BDD
