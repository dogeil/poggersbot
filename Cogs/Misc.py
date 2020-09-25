import discord, random, datetime
import asyncio
import functools
import itertools
import math
import youtube_dl
from async_timeout import timeout
from discord.ext import commands
from send import banlist, sendm
from discord.utils import get

class Misc(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(help="Ask the 8ball a question", aliases=["8ball"])
	async def ball(self, ctx, *, question=None):
		if(question!=None):
			responses = ["It is certain.","It is decidedly so.","Without a doubt.","Yes – definitely.","You may rely on it.","As I see it, yes.","Most likely.","Outlook good.","Yes.","Signs point to yes.","Reply hazy, try again.","Ask again later.","Better not tell you now.","Cannot predict now.","Concentrate and ask again.","Don't count on it.","My reply is no.","My sources say no.","Outlook not so good.","Very doubtful."]
			bruh=ctx.guild.roles
			bruh2=[]
			bruh3=[]
			for i in bruh:
				a=i.name
				b=i.id
				bruh2.append(a)
				bruh3.append(b)
			for idx, i in enumerate(bruh3):
				txt=question.replace(f"<@&{str(i)}>", bruh2[idx])
				txt=txt.replace("@everyone", "everyone")
				txt=txt.replace("@here", "here")
				
			await sendm(banlist, ctx, f"Question: {txt}\n{random.choice(responses)}")
		else:
			await sendm(banlist, ctx, "give me a question, get an answer")

	@commands.command()
	async def sex(self, ctx, *, sexpeople = None):
		if("!and" in sexpeople):
			sexpeoplelist=sexpeople.replace(" ", "").split("!and")
			sexperson1=sexpeoplelist[0]
			sexperson2=sexpeoplelist[1]
			if(sexperson1.startswith("<@")):
				sexperson1=sexperson1.replace("<@","")
				sexperson1=sexperson1.replace("!","")
				sexperson1=sexperson1.replace(">","")
				sexid=int(sexperson1[0:19])
				sexperson11 = self.bot.get_user(sexid).name
			else:
				sexperson11=sexpeoplelist[0]
			if(sexperson2.startswith("<@")):
				sexperson2=sexperson2.replace("<@","")
				sexperson2=sexperson2.replace("!","")
				sexperson2=sexperson2.replace(">","")
				sexid=int(sexperson2[0:19])
				sexperson22 = self.bot.get_user(sexid).name
			else:
				return
			sexperson22=sexpeoplelist[1]
			RATE=random.randint(1,100)
			sexembed=discord.Embed(title=f"sex rate of {sexperson11} and {sexperson22}", description=f"***{RATE}%***", timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
			if(ctx.channel.id not in banlist):
				await ctx.send(embed=sexembed)
		else: 
			if(sexpeople==None):
				await sendm(banlist, ctx, "give me someone to sex")
			else:
				if(sexpeople.startswith("<@")):
					sexpeople=sexpeople.replace("<@","")
					sexpeople=sexpeople.replace("!","")
					sexpeople=sexpeople.replace(">","")
					sexid=int(sexpeople[0:19])
					sexuser = self.bot.get_user(sexid)
					RATE=random.randint(1,100)
					sexembed=discord.Embed(title=f"sex rate of {ctx.author.name} and {sexuser.name}", description=f"***{RATE}%***", timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
					if(ctx.channel.id not in banlist):
						await ctx.send(embed=sexembed)
				else:
					RATE=random.randint(1,100)
					sexembed=discord.Embed(title=f"sex rate of {ctx.author.name} and {sexpeople}", description=f"***{RATE}%***", timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
					if(ctx.channel.id not in banlist):
						await ctx.send(embed=sexembed)

	@commands.command(help="pp size epik")
	async def pp(self, ctx):
		await sendm(banlist, ctx, f"8{'='*random.randint(1,10)}D")

	@commands.command(help="pong")
	async def ping(self, ctx):
		await sendm(banlist, ctx, f"pong gaming \n" + "{:.1f}".format(self.bot.latency * 1000) +" ms")

	@commands.command(help="roll dice")
	async def roll(self, ctx, num = None):
		if num == None:
			await sendm(banlist, ctx, "You need to give me a number")
		elif int(num) < 1:
			await sendm(banlist, ctx, "Number must be bigger than 1")
		else:
			roll = random.randint(1, int(num))
			await sendm(banlist, ctx, f"Roll: {str(roll)}")
	
	@commands.command(help="repeats the text you sent")
	async def say(self, ctx, *, txt = None):
		if(txt==None):
			await sendm(banlist, ctx, "give me some text")
		else:
			bruh=ctx.guild.roles
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
				
			await sendm(banlist, ctx, txt)
	
	@commands.command(help="repeats the text you sent and deletes your message")
	async def saydel(self, ctx, *, txt = None):
		if(txt==None):
			await sendm(banlist, ctx, "give me some text")
		else:
			bruh=ctx.guild.roles
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
				
			await sendm(banlist, ctx, txt)
		await ctx.message.delete()

	@commands.command(help="baka mitai")
	async def bakamitai(self, ctx):
		await sendm(banlist, ctx, "baka mitai kodomo na no ne yume wo otte kizu tsuite uso ga heta na kuse ni waraenai egao miseta I LOVE YOU mo roku ni iwanai kuchibeta de honma ni bukiyou na no ni na no ni doushite sayonara wa ieta no dame da ne dame yo dame na no yo anta ga suki de suki sugite dore dake tsuyoi osake de mo yugamanai omoide ga baka mitai baka mitai hontou baka ne anta shinjiru bakari de tsuyoi onna no furi setsunasa no yokaze abiru hitori ni natte san-nen ga sugi machinami sae mo kawarimashita na no ni na no ni doushite miren dake okizari honma ni roku na otoko ya nai soroi no yubiwa hazushimasu zamaa miro seisei suru wa ii kagen mattete mo baka mitai dame da ne dame yo dame na no yo anta ga suki de suki sugite dore dake tsuyoi osake de mo yugamanai omoide ga baka mitai honma ni roku na otoko ya nai soroi no yubiwa hazushimasu zamaa miro seisei suru wa nan na no yo kono namida baka mitai")

	@commands.command()
	async def monke(self, ctx):
		await sendm(banlist, ctx, ":orangutan:")

	@commands.command()
	async def arabfunny(self, ctx):
		await sendm(banlist, ctx, "https://media.discordapp.net/attachments/742075556648058900/754209706024763392/repost_this_image_to_instantly_die.png?width=388&height=300")

	@commands.command()
	async def randomshit(self, ctx):
		await sendm(banlist, ctx, "https://cdn.discordapp.com/attachments/742075556648058900/754210572488278127/The_engineer.txt")

	@commands.command()
	async def cbt(self, ctx):
		await sendm(banlist, ctx, "Cock and ball torture (CBT) is a sexual activity involving application of pain or constriction to the male genitals. This may involve directly painful activities, such as wax play, genital spanking, squeezing, ball-busting, genital flogging, urethral play, tickle torture, erotic electrostimulation or even kicking.[1] The recipient of such activities may receive direct physical pleasure via masochism, or emotional pleasure through erotic humiliation, or knowledge that the play is pleasing to a sadistic dominant. Many of these practices carry significant health risks.")

	@commands.command()
	async def peepee(self, ctx):
		await sendm(banlist, ctx, "poopoo")

	@commands.command()
	async def poopoo(self, ctx):
		await sendm(banlist, ctx, "peepee")

	@commands.command()
	async def slaughter(self, ctx):
		await sendm(banlist, ctx, "I don't know what I was thinking\n Leaving my child behind\n Now I suffer the curse\n Knowing now I am blind\n \n With all this anger, guilt and sadness\n Coming to haunt me forever\n I can't wait for the cliff at the end of the river\n \n Is this revenge I am seeking\n Or seeking someone to avenge me\n Stuck in my own paradox\n I wanna set myself free\n \n Maybe I should chase and find\n Before they'll try to stop it\n It won't be long before I'll become a puppet\n \n It's been so long\n Since I last have seen my son\n Lost to this monster\n To the man behind the slaughter\n \n Since you've been gone\n I've been singing this stupid song\n So I could ponder\n The sanity of your mother\n \n I wish I lived in the present\n With the gift of my past mistakes\n But the future keeps luring in like a pack of snakes\n \n Your sweet little eyes\n Your little smile, is all I remember\n Those fuzzy memories mess with my temper\n \n Justification is killing me\n But killing isn't justified\n What happened to my son, I'm terrified\n \n It lingers in my mind\n And the thought keeps on getting bigger\n I'm sorry my sweet baby\n I wish I've been there\n \n It's been so long\n Since I last have seen my son\n Lost to this monster\n To the man behind the slaughter\n \n Since you've been gone\n I've been singing this stupid song\n So I could ponder\n The sanity of your mother\n")

	@commands.command()
	async def b(self, ctx):
		await sendm(banlist, ctx, ":b:")

	@commands.command()
	async def a(self, ctx):
		await sendm(banlist, ctx, ":a:")

	@commands.command()
	async def connectionterminated(self, ctx):
		await sendm(banlist, ctx, "Connection terminated.")
		await sendm(banlist, ctx, "I'm sorry to interrupt you Elizabeth, if you still even remember that name. But I'm afraid you've been misinformed. You are not here to receive a gift, nor have you been called here by the individual you assume. Although you have indeed been called.\n \nYou have all been called here. Into a labyrinth of sounds and smells, misdirection and misfortune. A labyrinth with no exit, a maze with no prize. You don't even realize that you are trapped. Your lust for blood has driven you in endless circles, chasing the cries of children in some unseen chamber, always seeming so near, yet somehow out of reach.\n \nBut you will never find them, none of you will. This is where your story ends.\n \nAnd to you, my brave volunteer, who somehow found this job listing not intended for you. Although there was a way out planned for you, I have a feeling that's not what you want. I have a feeling that you are right where you want to be. I am remaining as well, I am nearby.\n \nThis place will not be remembered, and the memory of everything that started this can finally begin to fade away. As the agony of every tragedy should. And to you monsters trapped in the corridors: Be still and give up your spirits, they don't belong to you.\n \nFor most of you, I believe there is peace and perhaps more waiting for you after the smoke clears. Although, for one of you, the darkest pit of Hell has opened to swallow you whole, so don't keep the devil waiting, old friend.\n \nMy daughter, if you can hear me, I knew you would return as well. It's in your nature to protect the innocent. I'm sorry that on that day, the day you were shut out and left to die, no one was there to lift you up into their arms the way you lifted others into yours. And then, what became of you.\n \nI should have known you wouldn't be content to disappear, not my daughter. I couldn't save you then, so let me save you now.\n \nIt's time to rest. For you, and for those you have carried in your arms.\n \nThis ends for all of us.")
		await sendm(banlist, ctx, "End communication.")

def setup(bot):
	bot.add_cog(Misc(bot))
