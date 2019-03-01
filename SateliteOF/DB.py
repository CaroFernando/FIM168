import mysql.connector

class con:

    def __init__(self, user="root", password="", database="", host="127.0.0.1"):
        self.acc = {'user': user, 'password': password,
                    'database': database, 'host': host}

    def est_con(self):
        try:
            self.cnx = mysql.connector.connect(** self.acc)
            self.cursor = self.cnx.cursor()
            print(self.acc)

            return True

        except:
            print("ERROR al conectar con " + str(self.acc["host"]))


    def des_con(self):
        self.cnx.close()


    def ex_ins(self, query):
        try:
            self.cursor.execute(query)
            self.cnx.commit()

            return "OK"

        except Exception as e:

            return ("ERROR: " + str(e))
