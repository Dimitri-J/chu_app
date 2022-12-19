import mysql.connector
from mysql.connector import Error

connection_config = {
    "host" : "localhost",
    "user" :"py",
    "password":"python",
    "auth_plugin" : "mysql_native_password",
    "database" : "CHU_Caen",
    "port" : "3308"        
}

class Archive:
    
    @staticmethod
    def enregister_archive_en_base(table, var): ### Enregistre un nouveau patient ou résident dans la BDD
        if table=='patients':  ### Enregistre un nouveau patient dans la BDD  
            try :
                mydb = mysql.connector.connect(**connection_config)
                mycursor = mydb.cursor()
                sql = f"""INSERT INTO {table} (`identifiant_patient`, `nom`, `prenom`, `groupe_sanguin`, `is_in_hospital`) VALUES {var};""" 
                # ON DUPLICATE KEY UPDATE {colonne_1_name}="{colonne_1_value}", {colonne_2_name}="{colonne_2_value}"  """
                
                print(sql)

                mycursor.execute(sql)

                mydb.commit()

                

                print(mycursor.rowcount, f"record inserted.")

                return True

            except Error as e:
                print(f"ça marche pas, parce que : {e}")
                return False

            
            finally:
                if mydb.is_connected():
                    mycursor.close()
                    mydb.close()
                    print("MySQL connection is closed")

        if table=='rh': ### Enregistre un nouveau résident dans la BDD  
            try :
                mydb = mysql.connector.connect(**connection_config)
                mycursor = mydb.cursor()
                sql_rh = f"""INSERT INTO {table} (`identifiant_rh`, `nom`, `prenom`, `salaire`, `working_at_hospital`) VALUES {var[0]};""" 
                sql_archive = f"""INSERT INTO archives (`identifiant_resident`, `date_entree`) VALUES {var[1]};""" 
                mycursor.execute(sql_rh)
                mycursor.execute(sql_archive)
                mydb.commit()

                print(mycursor.rowcount, f"record inserted.")

                return True

            except Error as e:
                print(f"ça marche pas, parce que : {e}")
                return False

            
            finally:
                if mydb.is_connected():
                    mycursor.close()
                    mydb.close()
                    print("MySQL connection is closed")           
    
    @staticmethod
    def update_archive_en_base(var): ### Met à jour la fin de contrat du résident pour la table RH et Archive
        try :
            mydb = mysql.connector.connect(**connection_config)
            mycursor = mydb.cursor() 
            sql_rh = f"""UPDATE `rh` SET `working_at_hospital`='0' WHERE `identifiant_rh`='{var[0]}';""" 
            sql_archive = f"""UPDATE `archives` SET `date_sortie`='{var[1]}' WHERE `identifiant_resident`='{var[0]}';""" 
            mycursor.execute(sql_rh)
            mycursor.execute(sql_archive)
            mydb.commit()
            print(mycursor.rowcount, f"record update.")
            if mycursor.rowcount == 0:
                return False

            return True

        except Error as e:
            print(f"ça marche pas, parce que : {e}")
            return False

        
        finally:
            if mydb.is_connected():
                mycursor.close()
                mydb.close()
                print("MySQL connection is closed")      

    @staticmethod
    def update_patient_en_base(var): ### Met à jour la sortie du patient
        try :
            mydb = mysql.connector.connect(**connection_config)
            mycursor = mydb.cursor() 
            sql_patient = f"""UPDATE `patients` SET `is_in_hospital`='0' WHERE `identifiant_patient`='{var}';""" 
            mycursor.execute(sql_patient)
            mydb.commit()
            print(mycursor.rowcount, f"record update.")

            return True

        except Error as e:
            print(f"ça marche pas, parce que : {e}")
            return False

        
        finally:
            if mydb.is_connected():
                mycursor.close()
                mydb.close()
                print("MySQL connection is closed")      


    @staticmethod
    def afficher_les_archives_console(): ### Affiche les infos de la tâble Archive dans la console
        try :
            mydb = mysql.connector.connect(**connection_config)
            mycursor = mydb.cursor() 
            sql_archive = f"""SELECT * FROM archives;""" 
            mycursor.execute(sql_archive)
            resultat = mycursor.fetchall()
            print(mycursor.rowcount, f"record show.")
            for line in resultat:
                print(line)

            return True

        except Error as e:
            print(f"ça marche pas, parce que : {e}")
            return False

        
        finally:
            if mydb.is_connected():
                mycursor.close()
                mydb.close()
                print("MySQL connection is closed")      


    @staticmethod
    def afficher_les_archives_streamlit(): ### Affiche les infos de la tâble Archive sur le site StreamLit
        try :
            mydb = mysql.connector.connect(**connection_config)
            mycursor = mydb.cursor() 
            sql_archive = f"""SELECT * FROM archives;""" 
            mycursor.execute(sql_archive)
            resultat = mycursor.fetchall()
            print(mycursor.rowcount, f"record show.")
            return resultat

            return True

        except Error as e:
            print(f"ça marche pas, parce que : {e}")
            return False

        
        finally:
            if mydb.is_connected():
                mycursor.close()
                mydb.close()
                print("MySQL connection is closed")          



