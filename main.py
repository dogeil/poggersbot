import os, discord, traceback, asyncio, functools, itertools, math, youtube_dl
from keep_alive import keep_alive
from discord.ext import commands
from send import banlist, sendm

#banana
#apel

bot = commands.AutoShardedBot(command_prefix = '.', description = "it fights dummy",case_insensitive=True)
bot.remove_command('help')
IgnoreImport = []

for Extension in [f.replace('.py', '') for f in os.listdir("Cogs") if os.path.isfile(os.path.join("Cogs", f))]:
	if Extension in IgnoreImport:
		continue
	try:
		print(f"Loading extension {Extension}")
		bot.load_extension(f"Cogs.{Extension}")
		print(f"Extension {Extension} loaded.")
	except (discord.ClientException, ModuleNotFoundError, commands.errors.ExtensionFailed):
		print(f'Failed to load extension {Extension}.')
		traceback.print_exc()

@bot.event
async def on_ready():
	print('my body is ready')
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="your mom lmao"))

keep_alive()
token = os.environ.get("TOKEN")
bot.run(token)
# dumb bot made by @right hand man#0766 v1.2.3, to run it yourself, make a file named .env and paste TOKEN=token in there and replace the lowercase token with your bot token * GITHUB: https://github.com/Ya1Boi/poggersbot *
