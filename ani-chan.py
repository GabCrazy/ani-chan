#Imports basicos para o funcionamento do bot
import discord
from discord.ext import commands
import keys

#Método de geração de classe Client
client = discord.Client()
client = commands.Bot(command_prefix="A!")      #Prefixo dos comandos do bot
is_client_running = False                       #Bool de identificação de estado do bot

#Evento de ligar o bot
@client.event
async def on_ready():
    global is_client_running
    
    #Checagem do estado do bot
    if not is_client_running:                   
        is_client_running = True
        print(f"Agora a {client.user.name} tá acordando...")       #Mensagem de inicialização no terminal

#Evento de ler mensagens
@client.event
async def on_message(message):
    
    #Checagem para impedir o bot de responder a si mesmo
    if message.author == client.user:
        return
    
    #Checagem de prefixo de comando para demonstrar que está processando a mensagem
    if message.content.startswith("A!"):
        await message.channel.trigger_typing()
    
    #Processamento da mensagem
    await client.process_commands(message)

#Comando de ping
@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

#Comando de desligar o bot
@client.command(aliases = ['VocêFoiDeBase'])
async def mimir(ctx):
    await ctx.send("Vou amimir...")
    await client.close()

client.run(keys.TOKEN)