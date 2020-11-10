import discord, datetime
from discord.ext import commands
from main import banlist, sendm, sendem, log

class Help(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.embed = discord.Embed(title="Engineer\'s Fighting Club", description="This is a Team Fortress 2 based fighting bot with some extra features too, but mainly is about player duels \n Important Commands:", timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
		self.embed.add_field(name=".fighthelp", value="Help about player duels")
		self.embed.add_field(name=".mischelp", value="Help about other commands")
		self.embed.add_field(name=".about", value="Stuff about the creator and the bot")
		self.embed.add_field(name=".credits", value="Credits to all the people who helped me with this bot")
		self.embed.add_field(name=".invite", value="The bot\'s invite: https://tinyurl.com/poggers-bot")
		self.embed.add_field(name=".premium", value="Explains the premium features and how to get them")
		self.embed.set_thumbnail(url="https://media.discordapp.net/attachments/739303210204004383/745318242284863608/250px-Pugilists_Protector.png")

	@commands.command(help="Shows help menu")
	async def help(self, ctx):
		await log(ctx)
		await sendem(banlist, ctx, self.embed)
	
	@commands.command(help="The invite")
	async def invite(self, ctx):
		await log(ctx)
		await sendm(banlist, ctx, "https://tinyurl.com/poggers-bot")
		
	@commands.command()
	async def premium(self, ctx):
		await log(ctx)
		await sendm(banlist, ctx, "**The premium for this bot doesn't give you anything in return yet**, you can still achieve premium if you want to support me, there are three premium levels \n \n Level 1: the least additions, you can get it by sending me any steam item worth at least 20 cents/5 refined metal \n \n Level 2: All the extra additions (I'm still working on those), level 2 costs any steam item worth more than 80 cents/20 refined metal \n \n Level 3: All the extra additions, you can also ask for anything for me to add to this bot, as long as it's not too complex, that I'll add it, level 3 costs any steam item worth more than one Team Fortress 2 Mann Co. Crate Key (I can't give an exact price for the level 3 since the price of the Key varies a lot, you can check the price on the Steam community market)\n \n The steam trade link you are supposed to send the items: https://steamcommunity.com/tradeoffer/new/?partner=1101449828&token=BjWbFQjZ \n \n **I'm still working on adding premium additions, if you have an idea, feel free to share it** \n \n **Premium stays with you forever, you can also buy one premium level and then upgrade to another one later** \n \n Level 4: i just give you the token of this bot (full control of the bot), costs one Team Fortress 2 Unusual hat worth more than 30 keys \n **I made level 4 as a joke but if you actually do it, I'll gladly accept it**")
		
	@commands.command(help="Shows about")
	async def about(self, ctx):
		await log(ctx)
		await sendm(banlist, ctx, "This a player duel bot made by @retard#9070 in discord.py, you can download the source code here: https://github.com/Ya1Boi/poggersbot v1.3.0")

	@commands.command(help="Shows credits")
	async def credits(self, ctx):
		await log(ctx)
		await sendm(banlist, ctx, "I would like to thank all the people that helped me: @JezzaProto#6483 for organizing my bad code, @weakpc#0568 ~~for being a pain in the ass~~ for motivating me to code, I also think that I haven\'t emphasized enough how @bonke#8942 helped by making a whole language for her, so @bonke#8942 for ~~giving me free money~~ helping me through my tough times and all the people on my server that helped me")

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
		embed.add_field(name=".sex (user mention/text)",value="gives a rate for the user of the command and the user/text given (runs on the same command as the other version of .sex)")
		embed.add_field(name=".cock", value=":chicken:")
		await sendem(banlist, ctx, embed)

def setup(bot):
	bot.add_cog(Help(bot))
