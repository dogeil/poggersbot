import datetime

banlist=[738052976723099751, 746241690028736582, 745686303479169105, 741919727110062198, 754459212658114698, 751614817412055081, 738064884159348848, 738064841658335283, 748977999285714996, 753064737721286836, 738064786218025111, 743875265532264479, 741303074857156658, 742386914383888456, 755854291063013539]
async def log(ctx, extra="None"):
	cmdtime=str(datetime.datetime.today()).replace("-", "/").split(".")[0]+" (UTC)"

	cmduser=ctx.author.name+"#"+ctx.author.discriminator

	cmdname=ctx.command.name

	if(cmdname=="ball"):
		cmdname="8ball"
	
	cmdchannel=ctx.channel.name
	
	if(ctx.channel.id in banlist):
		return
	else:
		with open("logs.txt","a") as file:
			file.write(f"Command .{cmdname} used by {cmduser} at {cmdtime} in {cmdchannel}, Extra Information: \"{extra}\"\n")

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
