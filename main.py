from keep_alive import keep_alive
import discord, os, traceback, datetime
from discord.ext import commands

banlist=[778722406344556554]

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
	listofwords=["im", "Im", "iM", "IM", "i'm", "I'm", "I'M", "i'M"]
	for i in listofwords:
		if (msg.content.startswith(i+" ") and not msg.channel.id in banlist and not msg.author.id==741811813615927307):
			txt="Hi, "+msg.content.replace(i+" ","",1)+", I'm dad!"
			bruh=msg.guild.roles
			bruh2=[]
			bruh3=[]
			for i in bruh:
				a=i.name
				b=i.id
				bruh2.append(a)
				bruh3.append(b)
			for idx, i in enumerate(bruh3):
				txt=txt.replace(f"<@&{str(i)}>", bruh2[idx])
				txt=txt.replace("@everyone", "everyone")
				txt=txt.replace("@here", "here")
			if("gay" in txt.lower() or "homosexual" in txt.lower()):
				txt="I know"
			await msg.channel.send(txt)
			await log(await bot.get_context(msg), msg.content)
			
		
			
	await bot.process_commands(msg)

@bot.event
async def on_ready():
	print('my body is ready \n')
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you"))

@bot.command()
async def fight(ctx, player2 : discord.Member):
	
	await log(ctx)
	
	fightlist.append(f"{ctx.author.id}(100,{player2.id}(100-{ctx.channel.id}")
	
	await sendm(banlist, ctx, f"{ctx.author.mention} starts, the only thing working is punch for testing")
	
keep_alive()
token = os.environ.get("TOKEN")
bot.run(token)

"""
dumb bot made by @retard#9070, to run it yourself, check the README

GITHUB: https://github.com/Ya1Boi/poggersbot
"""

