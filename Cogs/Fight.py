import discord, random, datetime
from discord.ext import commands
from send import banlist, sendm

starter, notstarter, srtmh, notsrtmh, starterhp, notstarterhp, notsrtatk, srtatk, notsrtdef, srtdef, notsrtacc, srtacc, notsrtatkmode, srtatkmode, notsrtdefmode, srtdefmode, notsrtaccmode, srtaccmode, srtdodgemode, notsrtdodgemode, srtscoutacc, notsrtscoutacc, srtheavydmg, notsrtheavydmg, srtheavydodge, notsrtheavydodge = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

class Fight(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.embed = discord.Embed(title="Engineer\'s Fighting Help", description="The fights here are really simple \n Fighting Commands:", timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
		self.embed.add_field(name=".fight @examplename", value="Starts a fight with the person given (Rewrite WIP)")
		self.embed.add_field(name=".class", value="This shows the available classes to use in a fight and their explanation")
		self.embed.add_field(name="Fights options", value="All the current acceptable things you can do in a fight:")
		self.embed.add_field(name="jab", value="A simple punch, damage varies from 7-15")
		self.embed.add_field(name="quick one-two", value="Quick two punches, second punch has 50% chance to miss, each punch\'s damage varies from 5-13")
		self.embed.add_field(name="hook", value="A simple punch that does a consisntent 25 damage, but has only a 65% chance to hit")
		self.embed.add_field(name="uppercut", value="A good punch that does from 25-35 damage, but has only a 40% chance to hit")
		self.embed.add_field(name="massive haymaker", value="A strong punch that takes one turn to charge, does 55 damage, but has only a 50% chance to hit (you take 200% damage while charging), and also cancels any other charging massive haymaker when hit")
		self.embed.add_field(name="taunt kill", value="A attack that insta-kills but has only 0.5% chance to hit")
		self.embed.add_field(name="Spy Moves", value="To see the special moves only available to spy, check the spy section in the .class command")
		self.embed.add_field(name="defend", value="This increases your defense to 160%, but decreases your accuracy and attack to 70%")
		self.embed.add_field(name="attack", value="This increases your attack to 160%, but decreases your accuracy and defense to 70%")
		self.embed.add_field(name="focus", value="This increases your accuracy to 160%, but decreases your attack and defense to 70%")
		self.embed.add_field(name="dodge", value="This decreases your opponent\'s accuracy to 60%, but increases their accuracy and attack to 120%")
		self.embed.add_field(name="balance", value="Balances your stats back to 100% (attack, accuracy and defense)")
		self.embed.add_field(name="stats", value="This shows the current battle\'s statistics")
		self.embed.add_field(name="end/die", value="Ends the fight you are currently on")

	@commands.command(help="Shows help menu")
	async def fighthelp(self, ctx):
		if(ctx.channel.id not in banlist):
			await ctx.send(embed=self.embed)

	def switchstr(self):
		global starter, notstarter, srtmh, notsrtmh, starterhp, notstarterhp, notsrtatk, srtatk, notsrtdef, srtdef, notsrtacc, srtacc, notsrtatkmode, srtatkmode, notsrtdefmode, srtdefmode, notsrtaccmode, srtaccmode, srtdodgemode, notsrtdodgemode, srtscoutacc, notsrtscoutacc, srtheavydmg, notsrtheavydmg, srtheavydodge, notsrtheavydodge
		starter, notstarter = notstarter, starter
		srtmh, notsrtmh = notsrtmh, srtmh
		starterhp, notstarterhp = notstarterhp, starterhp
		notsrtatk, srtatk = srtatk, notsrtatk
		notsrtdef, srtdef = srtdef, notsrtdef
		notsrtacc, srtacc = srtacc, notsrtacc
		notsrtatkmode, srtatkmode = srtatkmode, notsrtatkmode
		notsrtdefmode, srtdefmode = srtdefmode, notsrtdefmode
		notsrtaccmode, srtaccmode = srtaccmode, notsrtaccmode
		srtdodgemode, notsrtdodgemode = notsrtdodgemode, srtdodgemode
		srtscoutacc, notsrtscoutacc = notsrtscoutacc, srtscoutacc
		srtheavydmg, notsrtheavydmg = notsrtheavydmg, srtheavydmg
		srtheavydodge, notsrtheavydodge = notsrtheavydodge, srtheavydodge

	@commands.command()
	async def fight(self, ctx, pl2 : discord.Member):
		if(ctx.author == pl2):
			await sendm(banlist, ctx, "You can't fight yourself, dummy")
			return
		if(ctx.author.bot or pl2.bot):
			await sendm(banlist, ctx, "You can't fight bots, dummy")
			return

		global p1
		global p2
		global p1hp
		global p2hp
		global starter
		global notstarter
		global starterhp
		global notstarterhp
		global endfight
		global srtmh
		global notsrtmh
		global srtatk
		global srtdef
		global srtacc
		global notsrtatk
		global notsrtdef
		global notsrtacc
		global srtatkmode
		global srtdefmode
		global srtaccmode
		global srtdodgemode
		global notsrtatkmode
		global notsrtdefmode
		global notsrtaccmode
		global notsrtdodgemode

		p1 = ctx.author
		p1hp = 150
		p2 = pl2
		p2hp = 150
		starter = random.choice([p1,p2])
		srtmh=False
		notsrtmh=False
		srtatk=100
		srtdef=100
		srtacc=100
		notsrtatk=100
		notsrtdef=100
		notsrtacc=100
		srtatkmode=None
		srtdefmode=None
		srtaccmode=None
		srtdodgemode=None
		notsrtatkmode=None
		notsrtdefmode=None
		notsrtaccmode=None
		notsrtdodgemode=None
		endfight=None

		if starter == p1:
			starterhp = p1hp
			notstarterhp = p2hp
			notstarter = p2
		elif starter == p2:
			starterhp = p2hp
			notstarterhp = p1hp
			notstarter = p1
		await sendm(banlist, ctx, f"{starter.mention} Starts off! What would you like to do? (if you need help, use .fighthelp command)")

		@self.bot.listen()
		async def on_message(msg):
			global p1
			global p2
			global p1hp
			global p2hp
			global starter
			global notstarter
			global starterhp
			global notstarterhp
			global endfight
			global srtmh
			global notsrtmh
			global srtatk
			global srtdef
			global srtacc
			global notsrtatk
			global notsrtdef
			global notsrtacc
			global srtatkmode
			global srtdefmode
			global srtaccmode
			global srtdodgemode
			global notsrtatkmode
			global notsrtdefmode
			global notsrtaccmode
			global notsrtdodgemode
			global p2pick
			global p1pick
			global srtscoutacc
			global notsrtscoutacc
			global srtheavydmg
			global notsrtheavydmg
			global srtheavydodge
			global notsrtheavydodge

			if msg.content.lower() == "quick one-two" and msg.author.id == starter.id:
				attacks = random.randint(1,100)
				if attacks >= 50:
					dmg=random.randint(5,13)
					notstarterhp-=dmg
					if notstarterhp < 0:
						notstarterhp=0
					if starterhp < 0:
						starterhp=0
					await sendm(banlist, ctx, f"{starter.mention}'s first attack did {dmg} to {notstarter.mention} and now he/she is left with {notstarterhp}!")
					await sendm(banlist, ctx, "Second attack missed!")
					self.switchstr()
					if notstarterhp <= 0:
						await sendm(banlist, ctx, f"{notstarter.mention} is dead! {starter.mention} just won with {starterhp}hp left!")
						return
					elif starterhp <= 0:
						await sendm(banlist, ctx, f"{starter.mention} is dead! {notstarter.mention} just won with {notstarterhp}hp left!")
						return
					else:
						await sendm(banlist, ctx, f"{starter.mention} is next! What would you like to do? Type your choice out in chat")
				else:
					attack1dmg=(5,13)
					attack2dmg=(5,13)
					dmg=attack1dmg+attack2dmg
					sample1damaged=notstarterhp-attack1dmg
					notstarterhp-=dmg
					if sample1damaged < 0:
						sample1damaged=0
					if notstarterhp < 0:
						notstarterhp=0
					if starterhp < 0:
						starterhp=0
					await sendm(banlist, ctx, f"{starter.mention}'s first attack did {attack1dmg} to {notstarter.mention} and now is left with {sample1damaged}!")
					await sendm(banlist, ctx, f"{starter.mention}'s second attack did {attack2dmg} to {notstarter.mention} and now is left with {notstarterhp}!")
					self.switchstr()
					if notstarterhp <= 0:
						await sendm(banlist, ctx, f"{notstarter.mention} is dead! {starter.mention} just won with {starterhp}hp left!")
						return
					elif starterhp <= 0:
						await sendm(banlist, ctx, f"{starter.mention} is dead! {notstarter.mention} just won with {notstarterhp}hp left!")
						return
					else:
						await sendm(banlist, ctx, f"{starter.mention} is next! What would you like to do? Type your choice out in chat")
			elif msg.content.lower() == "jab" and msg.author.id == starter.id:
				dmg=random.randint(7,15)
				notstarterhp-=dmg
				if notstarterhp < 0:
					notstarterhp=0
				if starterhp < 0:
					starterhp=0
				await sendm(banlist, ctx, f"{starter.mention}'s attack did {dmg} to {notstarter.mention} and now is left with {notstarterhp}!")
				self.switchstr()
				if notstarterhp <= 0:
					await sendm(banlist, ctx, f"{notstarter.mention} is dead! {starter.mention} just won with {starterhp}hp left!")
					return
				elif starterhp <= 0:
					await sendm(banlist, ctx, f"{starter.mention} is dead! {notstarter.mention} just won with {notstarterhp}hp left!")
					return
				else:
					await sendm(banlist, ctx, f"{starter.mention} is next! What would you like to do? Type your choice out in chat")
			elif msg.content.lower()=="taunt kill" and msg.author.id==starter.id:
				chance=random.randint(1,100)
				if chance == 69:
					await sendm(banlist, ctx, f"{starter.mention}'s attack did 42069 (haha) to {notstarter.mention} and now is left with 0hp!")
					await sendm(banlist, ctx, f"{notstarter.mention} is dead! {starter.mention} just won with {starterhp}hp left!")
					return
				else:
					await sendm(banlist, ctx, "Taunt attack missed!")
					self.switchstr()
					await sendm(banlist, ctx, f"{starter.mention} is next! What would you like to do? Type your choice out in chat")

			elif msg.content.lower()=="hook" and msg.author.id==starter.id:
				chance=random.randint(1,100)
				if chance >= 35:
					dmg=25
					notstarterhp-=dmg
					if(notstarterhp<0):
						notstarterhp=0
					if(starterhp<0):
						starterhp=0
					await sendm(banlist, ctx, f"{starter.mention}\'s attack did {dmg} to {notstarter.mention} and he/she is now left with {notstarterhp}!")
					self.switchstr()
					if notstarterhp <= 0:
						await sendm(banlist, ctx, f"{notstarter.mention} is dead! {starter.mention} just won with {starterhp}hp left!")
						return
					elif starterhp <= 0:
						await sendm(banlist, ctx, f"{starter.mention} is dead! {notstarter.mention} just won with {notstarterhp}hp left!")
						return
					else:
						await sendm(banlist, ctx, f"{starter.mention} is next! What would you like to do? Type your choice out in chat")
				else:
					await sendm(banlist, ctx, "Hook attack missed!")
					self.switchstr()
					await sendm(banlist, ctx, f"{starter.mention} is next! What would you like to do? Type your choice out in chat")

			elif msg.content.lower()=="uppercut" and msg.author.id==starter.id:
				chance=random.randint(1,100)
				if chance >= 60:
					dmg=(25,35)
					notstarterhp-=dmg
					if notstarterhp < 0:
						notstarterhp=0
					if starterhp < 0:
						starterhp=0

					await sendm(banlist, ctx, f"{starter.mention}\'s attack did {dmg} to {notstarter.mention} and he/she is now left with {notstarterhp}!")
					self.switchstr()
					if notstarterhp <= 0:
						await sendm(banlist, ctx, f"{notstarter.mention} is dead! {starter.mention} just won with {starterhp}hp left!")
						return
					elif starterhp <= 0:
						await sendm(banlist, ctx, f"{starter.mention} is dead! {notstarter.mention} just won with {notstarterhp}hp left!")
						return
					else:
						await sendm(banlist, ctx, f"{starter.mention} is next! What would you like to do? Type your choice out in chat")
				else:
					await sendm(banlist, ctx, "Uppercut attack missed!")
					self.switchstr()
					await sendm(banlist, ctx, f"{starter.mention} is next! What would you like to do? Type your choice out in chat")

			elif(msg.content.lower()=="massive haymaker" and msg.author.id==starter.id and not srtmh):
				await sendm(banlist, ctx, "Massive Haymaker Charging up!")
				srtdef=50
				srtmh=True
				if notstarterhp < 0:
					notstarterhp=0
				if starterhp < 0:
					starterhp=0
				self.switchstr()
				await sendm(banlist, ctx, f"{starter.mention} is next! What would you like to do? Type your choice out in chat")

			elif srtmh and not starterhp < 1 and not notstarterhp < 1:
				srtdef=100
				srtmh=False
				notsrtmh=False
				chance=random.randint(1,100)
				if chance >= 50:
					dmg=55
					notstarterhp-=dmg
					if notstarterhp < 0:
						notstarterhp=0
					if starterhp < 0:
						starterhp=0
					await sendm(banlist, ctx, f"{starter.mention}\'s attack did {dmg} to {notstarter.mention} and he/she is now left with {notstarterhp}!")
					self.switchstr()
					if notstarterhp <= 0:
						await sendm(banlist, ctx, f"{notstarter.mention} is dead! {starter.mention} just won with {starterhp}hp left!")
						return
					elif starterhp <= 0:
						await sendm(banlist, ctx, f"{starter.mention} is dead! {notstarter.mention} just won with {notstarterhp}hp left!")
						return
					else:
						await sendm(banlist, ctx, f"{starter.mention} is next! What would you like to do? Type your choice out in chat")
				else:
					await sendm(banlist, ctx, "Massive Haymaker attack missed!")
					self.switchstr()
					await sendm(banlist, ctx, f"{starter.mention} is next! What would you like to do? Type your choice out in chat")

			elif(msg.content.lower()=="defend" and msg.author.id==starter.id ):
				if not srtdefmode:
					srtdefmode=True
					srtatkmode=False
					srtaccmode=False
					srtdodgemode=False
					srtdef=160
					srtatk=70
					srtacc=70
					await sendm(banlist, ctx, "You are now defending!")
					self.switchstr()
					await sendm(banlist, ctx, f"{starter.mention} is next! What would you like to do? Type your choice out in chat")

				else:
					await sendm(banlist, ctx, "You are already defending")
					self.switchstr()
					await sendm(banlist, ctx, f"{starter.mention} is next! What would you like to do? Type your choice out in chat")

			elif(msg.content.lower()=="balance" and msg.author.id==starter.id and not p1pick==None and not p2pick==None):
				srtdefmode=False
				srtatkmode=False
				srtaccmode=False
				srtdodgemode=False
				srtdef=100
				srtatk=100
				srtacc=100
				await sendm(banlist, ctx, "You are now balanced!")
				self.switchstr()
				await sendm(banlist, ctx, f"{starter.mention} is next! What would you like to do? Type your choice out in chat")

			elif(msg.content.lower()=="attack" and msg.author.id==starter.id ):
				if not srtatkmode:
					srtdefmode=False
					srtatkmode=True
					srtaccmode=False
					srtdodgemode=False
					srtdef=70
					srtatk=160
					srtacc=70
					await sendm(banlist, ctx, "You are now attacking!")
					self.switchstr()
					await sendm(banlist, ctx, f"{starter.mention} is next! What would you like to do? Type your choice out in chat")

				else:
					await sendm(banlist, ctx, "You are already attacking")
					self.switchstr()
					await sendm(banlist, ctx, f"{starter.mention} is next! What would you like to do? Type your choice out in chat")

			elif(msg.content.lower()=="focus" and msg.author.id==starter.id):
				if not srtaccmode:
					srtdefmode=False
					srtatkmode=False
					srtaccmode=True
					srtdodgemode=False
					srtdef=70
					srtatk=70
					srtacc=160
					await sendm(banlist, ctx, "You are now focusing!")
					self.switchstr()
					await sendm(banlist, ctx, f"{starter.mention} is next! What would you like to do? Type your choice out in chat")

				else:
					await sendm(banlist, ctx, "You are already focusing")
					self.switchstr()
					await sendm(banlist, ctx, f"{starter.mention} is next! What would you like to do? Type your choice out in chat")

			elif((msg.content.lower() == "dodge" and msg.author.id == starter.id)):
					if(not srtdodgemode):
						srtdefmode=False
						srtatkmode=False
						srtaccmode=False
						srtdodgemode=True
						notsrtdef=120
						notsrtatk=120
						notsrtacc=60
						await sendm(banlist, ctx, "You are now dodging!")
						self.switchstr()
						await sendm(banlist, ctx, f"{starter.mention} is next! What would you like to do? Type your choice out in chat")
					else:
						await sendm(banlist, ctx, "You are already dodging")
						self.switchstr()
						await sendm(banlist, ctx, f"{starter.mention} is next! What would you like to do? Type your choice out in chat")
			elif msg.content.lower() == "hwiwhwiwbwiwbwtbwiba8jw8hw8wbywbqosbivw7wb" or msg.content.lower() == "end":
				print("a2")
				if msg.author.id == starter.id or msg.author.id == notstarter.id:
					await sendm(banlist, ctx, "You are ded, not big surprise")
					self.bot.remove_listener(on_message)
					return
				else:
					print("a1")
			elif(msg.content.lower()=="stats" and (msg.author.id==starter.id or msg.author.id==notstarter.id)):
				if(starter.id==p1.id):
					await sendm(banlist, ctx, f"Player 1: {p1.mention} \n Player 2: {p2.mention} \n Player 1 HP: {starterhp} \n Player 2 HP: {notstarterhp} \n Player 1 charging massive haymaker: {srtmh} \n Player 2 charging massive haymaker: {notsrtmh} \n Player 1 Attack: {srtatk}% \n Player 1 Defend: {srtdef}% \n Player 1 Accuracy: {srtacc}% \n Player 2 Attack: {notsrtatk}% \n Player 2 Defend: {notsrtdef}% \n Player 2 Accuracy: {notsrtacc}%")
				elif(notstarter.id==p1.id):
					await sendm(banlist, ctx, f"Player 1: {p2.mention} \n Player 2: {p1.mention} \n Player 1 HP: {notstarterhp} \n Player 2 HP: {starterhp} \n Player 1 charging massive haymaker: {notsrtmh} \n Player 2 charging massive haymaker: {srtmh} \n Player 1 Attack: {notsrtatk}% \n Player 1 Defend: {notsrtdef}% \n Player 1 Accuracy: {notsrtacc}% \n Player 2 Attack: {srtatk}% \n Player 2 Defend: {srtdef}% \n Player 2 Accuracy: {srtacc}%")

def setup(bot):
	bot.add_cog(Fight(bot))
