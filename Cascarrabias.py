import discord
import random


BOOMER_FILE = open("boomers.txt", "r")
BOOMER_IMGS = BOOMER_FILE.readlines()
BOOMER_FILE.close()

if len(BOOMER_IMGS) > 0:
    CHISTES_BOOMERS = True
else:
    CHISTES_BOOMERS = False


try:
    client = discord.Client()
    TOKEN = open("token.env", "r").readline()

    @client.event 
    async def on_ready():
        await client.get_channel(688816974947811406).send("Estúpidos críos, me han despertado de la siesta jugando al balón.")


    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        if message.content.startswith("Eh, viejo") or message.content.startswith("eh, viejo") or message.content.startswith("eh, Viejo") or message.content.startswith("Eh, Viejo"):
            await message.channel.send("¿Qué quieres ahora? {0}".format(str(message.author).split("#")[0]))
        if "cuentame chiste" in str(message.content) or "dime chiste" in str(message.content):
            if CHISTES_BOOMERS:
                await message.channel.send("Ja, ja... Mira que gracioso el chiste que me pasó mi cuñado el otro día por Whatsapp. {0}".format(random.choice(BOOMER_IMGS)))
            else:
                await message.channel.send("Ahora mismo no me acuerdo de ningún chiste...")
        if "otro chiste" in str(message.content):
            if CHISTES_BOOMERS:
                await message.channel.send("Vaya, parece que tenemos al graciosillo...")
            else:
                await message.channel.send("Ahora mismo no me acuerdo de ningún chiste...")
        
    client.run(TOKEN)

except KeyboardInterrupt:
    exit()



