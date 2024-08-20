import time
import requests
import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def mem(ctx):
    with open('IMAGES/meme.jpg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def bimbomeme(ctx):
    with open('IMAGES/bimbomeme.jpg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)


@bot.command()
async def memeperro(ctx):
    with open('IMAGES/memeperro.jpg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def memegato(ctx):
    with open('IMAGES/memegato.jpg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def mememessi(ctx):
    with open('IMAGES/mememessi.jpg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def memealbert(ctx):
    with open('IMAGES/memealbert.jpg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def mememessi2(ctx):
    with open('IMAGES/mememessi2.jpg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
@bot.command()
async def memes(ctx):
    x = os.listdir('IMAGES')

    with open(f'IMAGES/{random.choice(x)}', 'rb') as f:
            picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def profedeingles(ctx):
    time.sleep(2)
    await ctx.send(f"""Hello, I am {bot.user}!""")# esta linea saluda
    time.sleep(2)
    await ctx.send(f'Te voy hablar un poco sobre el INGLES')
    time.sleep(2)
    await ctx.send(f'El inglés se encuentra ubicado como uno de los primeros idiomas que permite a personas de los cinco continentes entenderse entre sí, además de ser necesitando para la educación, la vida laboral, para viajar, para utilizar el internet, y así mismo si quieres estar a la vanguardia de tu profesión')
    # Enviar una pregunta al usuario
    time.sleep(2)
    await ctx.send("Quieres consejos sobre cómo saber INGLES super facil? Responde con 'sí' o 'no'.")
# Esperar la respuesta del usuario
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ['sí', 'si', 'no']
    response = await bot.wait_for('message', check=check)
    if response:
        if response.content in ['sí', 'si']:
            time.sleep(2)
            await ctx.send("1. Si te gusta jugar, juega tu juego favorito con personas que hablen otros idiomas(como el INGLES)")
            time.sleep(2)
            await ctx.send("2. Rebasa tus conocimientos poniendote retos mentales")   
        else:
            await ctx.send("Está bien, si alguna vez necesitas consejos, no dudes en preguntar.")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")
    await ctx.send("Quieres saber la definicion del INGLES?, responde si o no")
    response1 = await bot.wait_for('message', check=check)
    if response1:
        if response1.content in ['sí', 'si']:
            time.sleep(2)
            await ctx.send("El idioma inglés (English) es una lengua germánica occidental perteneciente a la familia de lenguas indoeuropeas, que surgió en los reinos anglosajones de Inglaterra. Hoy en día el inglés es tanto el idioma más hablado en el mundo, así como el tercer idioma nativo más hablado, después del chino mandarín y el español.") 
        else:
            await ctx.send("Está bien, si alguna vez necesitas consejos, no dudes en preguntar.")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")


bot.run("¡¡TU TOKEN SECRETO VA AQUI!!")