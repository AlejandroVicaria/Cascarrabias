import discord
import random


try:
    client = discord.Client()
    TOKEN = open("token.env", "r").readline()
    BOOMER_FILE = open("boomers.txt", "a+")
    BOOMER_IMGS = BOOMER_FILE.readlines()

    if len(BOOMER_IMGS) > 0:
        CHISTES_BOOMERS = True

    @client.event 
    async def on_ready():
        await client.get_channel(688816974947811406).send("A ver... Sonotone, Bastón, Mala ostia... Vale, lo tengo todo listo ya.")


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



