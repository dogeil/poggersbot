from keep_alive import keep_alive
import discord, os, traceback, datetime
from discord.ext import commands

banlist=[]

fightlist=[]

async def log(ctx, extra="None"):
	cmdtime=str(datetime.datetime.today()).replace("-", "/").split(".")[0]+" (UTC)"

	cmduser=ctx.author.name+"#"+ctx.author.discriminator

	try:
		cmdname=ctx.command.name
	except:
		cmdname="(dad)"

	if(cmdname=="ball"):
		cmdname="8ball"
	
	cmdchannel=ctx.channel.name
	cmdserver=ctx.guild.name
	
	if(ctx.channel.id in banlist):
		return
	else:
		extra = extra.replace("`", "")
		logchannel=bot.get_channel(781124111216017458)
		otherlogchannel=bot.get_channel(763769618036031488)
		await logchannel.send(f"Command .{cmdname} used by `{cmduser}` at {cmdtime} in {cmdchannel} ({cmdserver}), Extra Information: `{extra}`\n")
		await otherlogchannel.send(f"Command .{cmdname} used by `{cmduser}` at {cmdtime} in {cmdchannel} ({cmdserver}), Extra Information: `{extra}`\n")

async def sendm(banlist, ctx, text=""):
	if(ctx.channel.id in banlist):
		return
	else:
		await ctx.send(text)

async def sendem(banlist, ctx, embed):
	if(ctx.channel.id in banlist):
		return
	else:
		await ctx.send(embed=embed)
		

#methe
#test banana

bot = commands.AutoShardedBot(command_prefix = ".", description = "it fights dummy",case_insensitive=True)
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
async def on_message(msg):
	await bot.process_commands(msg)

@bot.event
async def on_ready():
	print('my body is ready \n')
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you're mom"))
	
keep_alive()
token = os.environ.get("TOKEN")
bot.run(token)

"""
dumb bot made by @retard#9070, to run it yourself, check the README

GITHUB: https://github.com/Ya1Boi/poggersbot
"""

