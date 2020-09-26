import discord, datetime
from discord.ext import commands
from send import banlist, sendm

class Bonklang(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.embed = discord.Embed(title="Engineer\'s Bonk Cult", description="These are the bonk cult commands", timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
		self.embed.add_field(name=".bonklang", value="Says command you are currently seeing")
		self.embed.add_field(name=".translateto (text)", value="Translates what you sent to bonk'läl'pøg")
		self.embed.add_field(name=".translatefrom (text)", value="Translates what you sent from bonk'läl'pøg to english")
		self.embed.add_field(name=".bonklang about", value="Stuff about bonk language")
		self.embed.add_field(name=".bonklang help", value="Explains the bonk language")

	@commands.command(help="Base command for all bonklang commands.")
	async def bonklang(self, ctx, *, Type = None):
		if Type == None:
			if(ctx.channel.id not in banlist):
				await ctx.send(embed=self.embed)
		elif Type.upper() == "HELP":
			await sendm(banlist, ctx, "a=ł\nb=ľ\nc=ļ\nd=ĺ\ne=æ\nf=å\ng=ā\nh=ă\ni=ą\nj=à\nk=á\nl=l (duh)\nm=â\nn=ã\no=ä\np=p (duh)\nq=ø\nr=ž\ns=s (duh)\nt=ő\nu=u\nv=č\nw=w (duh)\nx=ķ\ny=y (duh)\nz=ň\nspace=\' \n ***The (duh) letters are known as equality letters and they are the same as in english***")
		elif Type.upper() == "ABOUT":
			await sendm(banlist, ctx, "bonk'läl'pøg is a language made for @arii#0471, it's context is in english, so it's more like encryption and not a language")

	@commands.command(help="Translating out of bonklang.")
	async def translatefrom(self, ctx, *, Text = None):
		if Text == None:
			await sendm(banlist, ctx, "You need to give me some text.")
		else:
			Text = Text.replace("ł","a")
			Text = Text.replace("ľ","b")
			Text = Text.replace("ļ","c")
			Text = Text.replace("ĺ","d")
			Text = Text.replace("æ","e")
			Text = Text.replace("å","f")
			Text = Text.replace("ā","g")
			Text = Text.replace("ă","h")
			Text = Text.replace("ą","i")
			Text = Text.replace("à","j")
			Text = Text.replace("á","k")
			Text = Text.replace("l","l")
			Text = Text.replace("â","m")
			Text = Text.replace("ã","n")
			Text = Text.replace("ä","o")
			Text = Text.replace("p","p")
			Text = Text.replace("ø","q")
			Text = Text.replace("ž","r")
			Text = Text.replace("s","s")
			Text = Text.replace("ő","t")
			Text = Text.replace("u","u")
			Text = Text.replace("č","v")
			Text = Text.replace("w","w")
			Text = Text.replace("ķ","x")
			Text = Text.replace("y","y")
			Text = Text.replace("ň","z")
			Text = Text.replace("'"," ")
			Text = Text.replace("ł".upper(),"a".upper())
			Text = Text.replace("ľ".upper(),"b".upper())
			Text = Text.replace("ļ".upper(),"c".upper())
			Text = Text.replace("ĺ".upper(),"d".upper())
			Text = Text.replace("æ".upper(),"e".upper())
			Text = Text.replace("å".upper(),"f".upper())
			Text = Text.replace("ā".upper(),"g".upper())
			Text = Text.replace("ă".upper(),"h".upper())
			Text = Text.replace("ą".upper(),"i".upper())
			Text = Text.replace("à".upper(),"j".upper())
			Text = Text.replace("á".upper(),"k".upper())
			Text = Text.replace("l".upper(),"l".upper())
			Text = Text.replace("â".upper(),"m".upper())
			Text = Text.replace("ã".upper(),"n".upper())
			Text = Text.replace("ä".upper(),"o".upper())
			Text = Text.replace("p".upper(),"p".upper())
			Text = Text.replace("ø".upper(),"q".upper())
			Text = Text.replace("ž".upper(),"r".upper())
			Text = Text.replace("s".upper(),"s".upper())
			Text = Text.replace("ő".upper(),"t".upper())
			Text = Text.replace("u".upper(),"u".upper())
			Text = Text.replace("č".upper(),"v".upper())
			Text = Text.replace("w".upper(),"w".upper())
			Text = Text.replace("ķ".upper(),"x".upper())
			Text = Text.replace("y".upper(),"y".upper())
			Text = Text.replace("ň".upper(),"z".upper())
			bruh=ctx.guild.roles
			bruh2=[]
			bruh3=[]
			for i in bruh:
				a=i.name
				b=i.id
				bruh2.append(a)
				bruh3.append(b)
			for idx, i in enumerate(bruh3):
				txt=Text.replace(f"<@&{str(i)}>", bruh2[idx])
				txt=txt.replace("@everyone", "everyone")
				txt=txt.replace("@here", "here")
			await sendm(banlist, ctx, txt)

	@commands.command(help="Translates into bonklang.")
	async def translateto(self, ctx, *, Text = None):
		if Text == None:
			await sendm(banlist, ctx, "You need to give me some text")
		else:
			Text = Text.replace("a","ł")
			Text = Text.replace("b","ľ")
			Text = Text.replace("c","ļ")
			Text = Text.replace("d","ĺ")
			Text = Text.replace("e","æ")
			Text = Text.replace("f","å")
			Text = Text.replace("g","ā")
			Text = Text.replace("h","ă")
			Text = Text.replace("i","ą")
			Text = Text.replace("j","à")
			Text = Text.replace("k","á")
			Text = Text.replace("l","l")
			Text = Text.replace("m","â")
			Text = Text.replace("n","ã")
			Text = Text.replace("o","ä")
			Text = Text.replace("p","p")
			Text = Text.replace("q","ø")
			Text = Text.replace("r","ž")
			Text = Text.replace("s","s")
			Text = Text.replace("t","ő")
			Text = Text.replace("u","u")
			Text = Text.replace("v","č")
			Text = Text.replace("w","w")
			Text = Text.replace("x","ķ")
			Text = Text.replace("y","y")
			Text = Text.replace("z","ň")
			Text = Text.replace(" ","'")
			Text = Text.replace("a".upper(),"ł".upper())
			Text = Text.replace("b".upper(),"ľ".upper())
			Text = Text.replace("c".upper(),"ļ".upper())
			Text = Text.replace("d".upper(),"ĺ".upper())
			Text = Text.replace("e".upper(),"æ".upper())
			Text = Text.replace("f".upper(),"å".upper())
			Text = Text.replace("g".upper(),"ā".upper())
			Text = Text.replace("h".upper(),"ă".upper())
			Text = Text.replace("i".upper(),"ą".upper())
			Text = Text.replace("j".upper(),"à".upper())
			Text = Text.replace("k".upper(),"á".upper())
			Text = Text.replace("l".upper(),"l".upper())
			Text = Text.replace("m".upper(),"â".upper())
			Text = Text.replace("n".upper(),"ã".upper())
			Text = Text.replace("o".upper(),"ä".upper())
			Text = Text.replace("p".upper(),"p".upper())
			Text = Text.replace("q".upper(),"ø".upper())
			Text = Text.replace("r".upper(),"ž".upper())
			Text = Text.replace("s".upper(),"s".upper())
			Text = Text.replace("t".upper(),"ő".upper())
			Text = Text.replace("u".upper(),"u".upper())
			Text = Text.replace("v".upper(),"č".upper())
			Text = Text.replace("w".upper(),"w".upper())
			Text = Text.replace("x".upper(),"ķ".upper())
			Text = Text.replace("y".upper(),"y".upper())
			Text = Text.replace("z".upper(),"ň".upper())
			bruh=ctx.guild.roles
			bruh2=[]
			bruh3=[]
			for i in bruh:
				a=i.name
				b=i.id
				bruh2.append(a)
				bruh3.append(b)
			for idx, i in enumerate(bruh3):
				txt=Text.replace(f"<@&{str(i)}>", bruh2[idx])
				txt=txt.replace("@everyone", "everyone")
				txt=txt.replace("@here", "here")
			await sendm(banlist, ctx, txt)

def setup(bot):
	bot.add_cog(Bonklang(bot))
