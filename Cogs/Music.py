import discord, datetime
import youtube_dl
from discord.ext import commands
from main import banlist, sendm, sendem, log

class Music(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(help="test")
	async def test(self, ctx):
		await log(ctx)
		await sendm(banlist, ctx, "yes")

def setup(bot):
	bot.add_cog(Music(bot))