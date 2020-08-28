import random





class Bingo():
    def __init__(self, tiempo, cartones):
        self.num_cartones = cartones
        self.tiempo = tiempo
        self.cartones = []


    def generar_carton(self):
        numeros_creados = []
        numeros_carton = []

        for carton in self.cartones:
            for numero in carton["Numeros"]:
                numeros_creados.append(numero)

        # Creamos los números para el cartón siempre y cuando no se repitan entre ellos.
        for y in range(0, 15):
            numero_creado = random.randint(0, 90)

            # Mientras el número no se repita lo metemos en el cartón.
            if y < 15:
                numeros_carton.append(numero_creado)
                numeros_creados.append(numero_creado)

        self.cartones.append({
            "Numeros": numeros_carton,
            "Asignado": "NO"
        })


    def generar_cartones(self):
        numeros_creados = []

        numeros_carton = []

        # Creamos cada cartón tomando el número de cartones como referencia.
        for x in range(0, self.num_cartones):
            self.generar_carton()



    def vender_carton(self, usuario):
        for carton in self.cartones:
            if carton["Asignado"] == "NO":
                carton["Asignado"] = usuario
                return usuario

        return "NADIE"

        



if __name__ == "__main__":
    Bing = Bingo(20, 10)
    Bing.generar_cartones()
    resultado = Bing.vender_carton("xRayO#8858")
    print("El cartón se ha vendido a {0}".format(resultado))
