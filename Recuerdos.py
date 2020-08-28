import sqlite3
import threading


class Memoria():
    """
    Inicia la memoria de Cascarrabias, para ello habrá que tener una base de datos creada previamente con las tablas definidas en el Readme, si no, no funcionará correctamente
    """
    def __init__(self, archivo):
        try:
            self.conn = sqlite3.connect(archivo)
            self.cursor = self.conn.cursor()
            self.ready = True if self.cursor != None else False
            print("[*] Iniciada la memoria de Cascarrabias.")

        except Exception as e:
            print("[*] No se ha podido iniciar la memoria de Cascarrabias")
        

    def obtener_intereses_usuario(self, id_usuario):
        """
        Obtiene los intereses que ha definido el usuario hablando con Cascarrabias y han sido guardados en la base de datos.
        """
        intereses = self.cursor.execute("SELECT intereses FROM discord_users WHERE id_usuario = ?", (str(id_usuario),))

        intereses = self.cursor.fetchone()

        if intereses:
            # Obtenemos los intereses si hay alguno y los devolvemos
            return intereses[0].split(",")
        else:
            # No devolvemos ningún interés
            return None
        

    def guardar_interes_usuario(self, id_usuario, interes):
        """
        Guarda un nuevo interés para el usuario especificado en la base de datos.
        """
        try:
            intereses = self.cursor.execute("SELECT intereses FROM discord_users WHERE id_usuario = ?", (str(id_usuario),))

            intereses = self.cursor.fetchone()
        
            if intereses[0] == None:
                # Si no hay ningún interés lo guardamos simplemente.
                self.cursor.execute("UPDATE discord_users SET intereses = ? WHERE id_usuario = ?", ("{0}".format(interes), str(id_usuario)))
                self.conn.commit()
                return True

            else:
                # Separamos los intereses que estarán formateados con una coma si los hubiese y los guardamos en un array.
                array_intereses = intereses[0].split(",")
                # Guardamos el nuevo interés en el array.
                array_intereses.append(interes)

                # Actualizamos la base de datos con el nuevo interés para el usuario.
                self.cursor.execute("UPDATE discord_users SET intereses = ? WHERE id_usuario = ?", (",".join(array_intereses), str(id_usuario)))
                self.conn.commit()
                return True

        except Exception as e:
            print("[*] Error guardando interés: {0}".format(e))
            return e



    def obtener_saludo_usuario(self, id_usuario):
        """
        Obtiene el saludo personal para el usuario.
        """
        return True


    def limpiar_datos_usuario(self, id_usuario):
        """
        Limpia todos los datos asociados al usuario especificado de la base de datos.
        """
        self.cursor.execute("UPDATE discord_users SET intereses = NULL, gustos = NULL, saludo_personalizado = NULL, cumpleaños = NULL, provincia = NULL WHERE id_usuario = ?", (str(id_usuario),))
        self.conn.commit()


    def add_miembros(self, usuarios):
        """
        Guarda todos los ids de los usuarios en la base de datos.
        """
        for usuario in usuarios:
            try:
                self.cursor.execute("INSERT INTO discord_users (id_usuario) VALUES (?);", (str(usuario), ))
                self.conn.commit()
            except sqlite3.IntegrityError:
                print("[*] Ya existe el usuario en la base de datos.")





if __name__ == "__main__":
    Memo = Memoria("memoria.db")
    guardado = Memo.guardar_interes_usuario("xRayO#8858", "la pizza con piña")