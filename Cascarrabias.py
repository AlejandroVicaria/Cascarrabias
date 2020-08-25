import discord
import random
import asyncio
import sys
import Recuerdos


BOOMER_FILE = open("boomers.txt", "r")
BOOMER_IMGS = BOOMER_FILE.readlines()
BOOMER_FILE.close()

# Añadimos DEBUG para tracing en los errores
DEBUG = True if sys.argv[2] == "True" else False

if DEBUG == True:
    print("[*] Iniciando Cascarrabias en modo DEBUG.")

# Cargamos la memoria
memoria = Recuerdos.Memoria("memoria.db")


# Marcamos si el archivo de imágenes boomers se puede usar
if len(BOOMER_IMGS) > 0:
    CHISTES_BOOMERS = True
else:
    CHISTES_BOOMERS = False


try:
    client = discord.Client()
    TOKEN = sys.argv[1]

    @client.event 
    async def on_ready():
        await client.get_channel(688816974947811406).send("Estúpidos críos, me han despertado de la siesta jugando al balón.")

        # Intentamos cargar la memoria del bot
        try:
            if memoria.ready:
                # No hacemos nada para no floodear
                pass
            else:
                # Si no creamos una excepción y desactivamos la memoria
                raise "Error cargando la memoria"
            if DEBUG == True:
                await client.get_channel(688816974947811406).send("Estoy en modo debug, así que puede que diga cosas raras.")
        except Exception:
            await client.get_channel(688816974947811406).send("Hoy no me acuerdo de nada, es como si me hubiesen formateado el disco duro....")
            



    @client.event
    async def on_message(message):

        def check(m):
            # Función que comprueba los mensajes del mismo usuario.
             return m.author == message.author


        channel = message.channel

        if message.author == client.user:
            # Desactivamos que el BOT se pueda auto-contestar para no spamear.
            return

        else:
            # Procedemos con el funcionamiento normal del BOT
            if "eh, viejo" in message.content.lower():
                await channel.send("¿Qué quieres ahora? {0}".format(str(message.author).split("#")[0]))

                # Esperamos la respuesta del usuario que ha llamado al bot.
                try:

                    message = await client.wait_for("message", timeout=30.0, check=check)

                    # Hook de contar chistes
                    if "cuentame un chiste" in message.content.lower() or "dime un chiste" in message.content.lower() or "dime otro chiste" in message.content.lower():
                        if CHISTES_BOOMERS:
                            await channel.send("Ja, ja... Mira que gracioso el chiste que me pasó mi cuñado el otro día por Whatsapp. {0}".format(random.choice(BOOMER_IMGS)))
                        else:
                            await channel.send("Ahora mismo no me acuerdo de ningún chiste...")

                    # Hook de guardar gustos
                    elif "me gusta" in message.content.lower():
                        if memoria.ready:
                            interes = message.content.replace("me gusta", "")
                            guardado = memoria.guardar_interes_usuario(message.author, interes)
                            if guardado == True:
                                await channel.send("Vale, me acordaré de que te gusta {0}".format(interes.strip()))
                            else:
                                if DEBUG == True:
                                    await channel.send("Se me ha frito el cerebro, no me voy a acordar de eso, dile a los que me crearon esto: {0}".format(guardado))
                                else:
                                    await channel.send("Se me ha frito el cerebro, no me voy a acordar de eso.")

                        else:
                            await channel.send("Ya te voy avisando de que no me voy a acordar de la chorrada esa que me has dicho...")


                    # Hook de juegos (muy a la larga, quiero hacer juegos interesantes)
                    elif "jugar" in message.content.lower() or "jugamos a algo" in message.content.lower():
                        await channel.send("Todavía estoy aprendiendo juegos, ya jugaremos a algo otro día.")


                    # Hook de gustos
                    elif "estoy triste" in message.content.lower():
                        if memoria.ready:
                            intereses = memoria.obtener_intereses_usuario(message.author)
                            await channel.send("Bueno, siempre puedes ir a {0}, me acuerdo que te gusta mucho".format(random.choice(intereses)))
                        else:
                            await channel.send("Pues ala, una palmadita en la espalda y a seguir.")

                    elif "olvida mi nombre, mi cara, mi casa, y pega la vuelta" in message.content.lower():
                        if memoria.ready:
                            memoria.limpiar_datos_usuario(message.author)
                            await channel.send("¡Jamás te pude comprender! A partir de ahora ya no me acordaré de nada de lo que me dijiste.")
                        else:
                            await channel.send("Vaya, si parece que sabe la canción de Pimpinela y todo...")

                except asyncio.TimeoutError:

                    # Si no ha contestado en 30 segundos lo mandamos a la mierda suavemente.
                    await channel.send("¿Qué divertido no? Primero me hablas y después me haces el mismo vacío que te hacen a ti por whatsapp.")


        
    client.run(TOKEN)

except KeyboardInterrupt:
    exit()



