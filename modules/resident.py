
class Patient: ### Création class Patient

    def __init__(self, nom, prenom, age, groupe_sanguin, date_entree):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.sang = groupe_sanguin
        self.date_entree = date_entree
        self.identifiant_patient = nom + "_" + prenom + "_" + groupe_sanguin + "_" + date_entree

    def entree_hopital(self): ### Prépare la requête d'entré à l'hospital d'un patient
        variable_SQL = self.identifiant_patient,self.nom,self.prenom,self.sang,"1"
        print("Patient enregistré en base")
        return variable_SQL

    def sorti_hopital(self): ### Prépare la requête de sortie de l'hospital d'un patient
        variable_SQL = self.identifiant_patient
        print("Patient sortie en base")
        return variable_SQL


class RH:
   
    def __init__(self, nom, prenom, age, groupe_sanguin, date_recrutement, salaire):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.sang = groupe_sanguin
        self.date_recrutement = date_recrutement
        self.salaire = salaire
        self.identifiant_rh = nom + "_" + prenom + "_" + groupe_sanguin + "_" + date_recrutement

    def debut_CDD_CDI(self): ### Prépare la requête de début de contrat du RH
        sql_rh = self.identifiant_rh,self.nom,self.prenom,self.salaire,"1"
        sql_archive = self.identifiant_rh, self.date_recrutement
        print("RH enregistré en base")
        return sql_rh, sql_archive

    def fin_CDD_CDI(self, date_sortie): ### Prépare la requête de fin de contrat du RH
        sql_rh = self.identifiant_rh
        sql_archive = date_sortie
        print("RH sortie en base")
        return sql_rh, sql_archive