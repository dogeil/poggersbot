import discord, datetime
from discord.ext import commands
from main import banlist, sendm, sendem, log

class Fight(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		
		
def setup(bot):
	bot.add_cog(Fight(bot))