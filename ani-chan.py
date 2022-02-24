import discord
from discord.ext import commands
import keys

client = discord.Client()
client = commands.Bot(command_prefix="A!")
is_client_running = False

@client.event
async def on_ready():
    global is_client_running

    if not is_client_running:
        is_client_running = True
        print(f"Bot {client.user.name} initializing...")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("A!"):
        await message.channel.trigger_typing()

    await client.process_commands(message)

@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

@client.command(aliases = ['YouHaveBeenTerminated'])
async def terminate(ctx):
    await ctx.send("Terminating...")
    await client.close()

client.run(keys.TOKEN)