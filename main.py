from keep_alive import keep_alive
import discord, os, traceback, datetime, random
from discord.ext import commands

fightdict={}

def getfight(id, dicte):
	variables=None
	ids=None
	for a, b in dicte.items():
		if str(id) in a:
			ids=a
			variables=b
	stuff=[ids, variables]
	return stuff

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
	
	extra = extra.replace("`", "")
	logchannel=bot.get_channel(781124111216017458)
	otherlogchannel=bot.get_channel(763769618036031488)
	await logchannel.send(f"Command .{cmdname} used by `{cmduser}` at {cmdtime} in {cmdchannel} ({cmdserver}), Extra Information: `{extra}`\n")
	await otherlogchannel.send(f"Command .{cmdname} used by `{cmduser}` at {cmdtime} in {cmdchannel} ({cmdserver}), Extra Information: `{extra}`\n")

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
	if str(msg.author.id) in str(fightdict):
		fight=getfight(msg.author.id, fightdict)
		p1id=int(fight[0].split("/")[1])
		p2id=int(fight[0].split("/")[2])
		p1=None
		if str(msg.author.id) == fight[0].split("/")[1]:
			p1=True
		else:
			p1=False
		if(msg.content.lower()=="punch"):
			if(p1==True and fight[1]["turn"]==True):
				randomdmg=random.randint(0, 100)
				new = {
					"p1hp" : fight[1]["p1hp"],
					"p2hp" : fight[1]["p2hp"]-randomdmg,
					"turn" : False
				}
				fightdict[fight[0]]=new
				newhp=str(new["p2hp"])
				await msg.channel.send(f"you dealt {randomdmg} damage")	
				if 0>=new["p2hp"]:
					await msg.channel.send(f"{msg.author.mention} you win!!! \ncongratulations you get nothing")
					del fightdict[fight[0]]
				else:
					await msg.channel.send(f"theyre now at {newhp} hp")
					await msg.channel.send(f"<@{str(p2id)}> youre next")
			elif(p1==False and fight[1]["turn"]==False):
				randomdmg=random.randint(0, 100)
				new = {
					"p1hp" : fight[1]["p1hp"]-randomdmg,
					"p2hp" : fight[1]["p2hp"],
					"turn" : True
				}
				fightdict[fight[0]]=new
				newhp=str(new["p1hp"])
				await msg.channel.send(f"you dealt {randomdmg} damage")	
				if 0>=new["p1hp"]:
					await msg.channel.send(f"{msg.author.mention} you win!!! \ncongratulations you get nothing")
					del fightdict[fight[0]]
				else:
					await msg.channel.send(f"theyre now at {newhp} hp")
					await msg.channel.send(f"<@{str(p1id)}> youre next")
	await bot.process_commands(msg)

@bot.command()
async def fight(ctx, obama : discord.Member):
	a1=0
	a2=0
	for fn in fightdict:
		if(str(ctx.author.id) in fn and str(obama.id) in fn):
			a1+=1
			a2+=1
		if(str(ctx.author.id) in fn):
			a1+=1
		if(str(obama.id) in fn):
			a2+=1
	if(obama.id==741811813615927307):
		#funny scenario trying to fight the bot
		await ctx.send("ok i win you lose")
	elif(obama.bot):
		#trying to fight a bot
		await ctx.send(f"{obama.mention} is a bot and im pretty sure you cant fight robots they would instantly win")
	elif(obama.id==ctx.author.id):
		#trying to fight self
		await ctx.send(f"{obama.mention} what you cant fight yourself dumb")
	elif(a1>=1 and a2>=1):
		#the command user and the other person are already fighting
		await ctx.send(f"{ctx.author.mention} youre already fighting that person")
	elif(a1>=1):
		#the command user is already fighting
		await ctx.send(f"{ctx.author.mention} stop thinking youre so good you cant fight two people at once")
	elif(a2>=1):
		#the other person is already fighting
		await ctx.send(f"{ctx.author.mention} why are you trying to fight {obama.mention} theyre already doing it with someone else")
	else:
		#actual fight
		turn=None

		a=random.randint(0, 100)
		if(a>=50):
			turn=True
		else:
			turn=False
		
		add = {
		"p1hp": 100,
		"p2hp": 100,
		"turn": turn
		}
		fightdict[f"/{str(ctx.author.id)}/{str(obama.id)}/"]=add
		if turn==True:
			await ctx.send(f"welcome to fight command scuffed edition!!!\n{ctx.author.mention} you start\n type \"punch\" because thats the only option")
		else:
			await ctx.send(f"welcome to fight command scuffed edition!!!\n{obama.mention} you start\n type \"punch\" because thats the only option")

@bot.command()
async def printfd(ctx):
	await ctx.send(str(fightdict))
@bot.command()
async def clearfd(ctx):
	for key in fightdict.keys():
  	  del fightdict[key]
	await ctx.send("ok")

@bot.event
async def on_ready():
	print('my body is ready \n')
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you're mom"))
	
keep_alive()
token = os.environ.get("TOKEN")
bot.run(token)

"""
dumb bot made by @retard#9070, to run it yourself, check the README

GITHUB: https://github.com/Ya1Boi/poggersbot (i just realized this is kind of useless because if youre seeing this youre probably already on the github)
"""

