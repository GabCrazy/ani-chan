#Imports basicos para o funcionamento do bot
from ast import Await, alias
from random import randrange, random
import discord
from discord.ext import commands
import keys
from datetime import datetime 

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

#Checagem de erro de comando
@client.event
async def on_command_error(ctx, error):
    
    #Checa a existencia do comando
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Não sei fazer isso :(")
    
    #Descrição genérica do erro
    else:
        await ctx.send(error)
        return
    print(datetime.now(), "command exception", type(error), error)  #Envia o erro para o terminal

#####################################################
##################Comandos gerais####################
#####################################################


#####################################################
###############Comandos de servidor##################
#####################################################

#Comando de ping-pong
@client.command()
@commands.guild_only()                              #Restrição para utilizar o comando somente no servidor
async def ping(ctx):
    await ctx.send("Pong!")
    
#####################################################
###############Comandos de privado###################
#####################################################

#Comando de ding-dong
@client.command()
@commands.dm_only()                                 #Restrição para utilizar o comando somente no privado
async def ding(ctx):
    await ctx.send("Dong!")

#####################################################
##############Comandos de permissão##################
#####################################################

#Comando de marco-polo
@client.command()
@commands.has_permissions(manage_guild=True)        #Restrição de permissão, só pode utilizar se puder gerenciar o servidor
async def marco(ctx):
    await ctx.send("Polo!")

#####################################################
################Comandos de cargo####################
#####################################################

#Comando de gerar numero aleatório
@client.command(aliases=["numero_entre"])                                   
@commands.has_role("adm")                           #Restrição de cargo, só pode utilizar se possuir esse cargo
async def randNum(ctx,a,b):
    result = randrange(int(a),int(b))               #Função de aleatoriedade do Python3
    await ctx.send(f"Que tal... **{result}**? Ele está entre {a} e {b} ^^")     #Retornar uma mensagem pro chat utilizando variaveis e modificadores de texto

#####################################################
#############Comandos do dono do bot#################
#####################################################

#Comando de desligar o bot
@client.command(aliases = ['VocêFoiDeBase'])        #Outros meios de chamar o comando
@commands.is_owner()                                #Restrição de ser dono do bot
async def mimir(ctx):
    await ctx.send("Vou amimir...")
    await client.close()

@mimir.error                                        #Manejador de erro do comando
async def mimir_erro(ctx, error):
    if isinstance(error, commands.NotOwner):
        await ctx.send("Você não pode me fazer mimir!!! UwU")
    else:
        await ctx.send(error)

#####################################################
#################Fim dos comandos####################
#####################################################

client.run(keys.TOKEN)                              #Identificador do bot