import discord, datetime
from discord.ext import commands
from main import log

class Help(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.embed = discord.Embed(title="Engineer\'s Fighting Club", description="This is a Team Fortress 2 based fighting bot with some extra features too, but mainly is about player duels \n Important Commands:", timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
		self.embed.add_field(name=".fighthelp", value="Help about player duels")
		self.embed.add_field(name=".mischelp", value="Help about other commands")
		self.embed.add_field(name=".about", value="Stuff about the creator and the bot")
		self.embed.add_field(name=".invite", value="The bot\'s invite: https://tinyurl.com/poggers-bot")
		self.embed.set_thumbnail(url="https://media.discordapp.net/attachments/739303210204004383/745318242284863608/250px-Pugilists_Protector.png")

	@commands.command(help="Shows help menu")
	async def help(self, ctx):
		await log(ctx)
		await ctx.send(embed=self.embed)
	
	@commands.command(help="The invite")
	async def invite(self, ctx):
		await log(ctx)
		await ctx.send("https://tinyurl.com/poggers-bot")
	
	@commands.command(help="Shows about")
	async def about(self, ctx):
		await log(ctx)
		await ctx.send("This a player duel bot made by @retard#9070 using discord.py, you can download the source code here: https://github.com/Ya1Boi/poggersbot")

	@commands.command(help="misc help")
	async def mischelp(self, ctx):
		await log(ctx)
		embed = discord.Embed(title="Engineer\'s Shit Club", description="These are the misc commands not related to fighting", timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
		embed.add_field(name=".ping", value="Posts the bot\'s latency (ping)")
		embed.add_field(name=".pong", value="very funny")
		embed.add_field(name=".8ball (question)", value="8ball command that gives anwers to  your questions")
		embed.add_field(name=".pp", value="Randomly chooses your pp size, haha funny")
		embed.add_field(name=".peepee", value="poopoo (and vice versa)")
		embed.add_field(name=".help", value="Bot Help")
		embed.add_field(name=".roll (num)", value="Rolls a number between 1 and the given number")
		embed.add_field(name=".connectionterminated", value="Says the FNAF 6 ending copypasta, very funny")
		embed.add_field(name=".bonklang", value="The bonk cult's language of choice, bonk'läl'pøg")
		embed.add_field(name=".b", value=":b:")
		embed.add_field(name=".a", value=":a:")
		embed.add_field(name=".bakamitai", value="Sings baka mitai, duh")
		embed.add_field(name=".slaughter", value="the man behind the slaughter")
		embed.add_field(name=".monke", value="monke")
		embed.add_field(name=".arabfunny", value="very funny haha")
		embed.add_field(name=".randomshit", value="idk")
		embed.add_field(name=".cbt", value="cock and ball torture")
		embed.add_field(name=".say (text)", value="repeats the text you send")
		embed.add_field(name=".saydel (text)",value="repeats the text you send and deletes your message")
		embed.add_field(name=".sexuser (user)",value="gives a rate for the user of the command and the other person given")
		embed.add_field(name=".sex (text)",value="gives a rate for the user of the command and the text given")
		embed.add_field(name=".cock", value=":chicken:")
		embed.add_field(name=".calc", value="Calculates whatever you say after the command (only certain characters are allowed)")
		embed.add_field(name=".uwu", value="no lol")
		await ctx.send(embed=embed)

	@commands.command(help="the")
	async def fighthelp(self, ctx):
		await log(ctx)
		embed = discord.Embed(title="Engineer\'s Fighting Club", description="These are the basic fighting commands that can be used by every class", timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
		embed.add_field(name="attack", value="normal attack that has average damage and always hits")
		embed.add_field(name="secondary attack", value="slightly different attack that deals higher damage but only has a 50% chance to hit")
		embed.add_field(name="focus", value="makes the basic attack do 200% more damage and the secondary attack have a 25% higher chance to hit and deal 175% more damage and only lasts for the next turn")
		embed.add_field(name="end", value="ends the fight")
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Help(bot))
