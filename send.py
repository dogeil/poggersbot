import os
from keep_alive import keep_alive
import discord, random, datetime, os, traceback
import asyncio
import functools
import itertools
import math
import youtube_dl
from async_timeout import timeout
from discord.ext import commands

banlist=[738052976723099751, 746241690028736582, 745686303479169105, 741919727110062198, 754459212658114698, 751614817412055081, 738064884159348848, 738064841658335283, 748977999285714996, 753064737721286836, 738064786218025111, 743875265532264479, 741303074857156658, 742386914383888456, 755854291063013539]
async def log(ctx, extra=None, cmdnameoverwrite=None):
	day=str(datetime.datetime.today().day)
	if(day.__len__()==1):
		day="0"+day
	month=str(datetime.datetime.today().month)
	if(month.__len__()==1):
		month="0"+month
	year=str(datetime.datetime.today().year)
	if(year.__len__()==1):
		year="0"+year
	hour=str(datetime.datetime.today().hour)
	if(hour.__len__()==1):
		hour="0"+hour
	minute=str(datetime.datetime.today().minute)
	if(minute.__len__()==1):
		minute="0"+minute
	second=str(datetime.datetime.today().second)
	if(second.__len__()==1):
		second="0"+second
	
	cmdtime=day+"/"+month+"/"+year+", "+hour+":"+minute+":"+second+" (UTC)"

	cmduser=ctx.author.name+"#"+ctx.author.discriminator

	cmdname=ctx.command.name

	if(cmdnameoverwrite==None):
		return
	else:
		cmdname=cmdnameoverwrite

	cmdchannel=ctx.channel.name
	
	if(ctx.channel.id in banlist):
		return
	else:
		print(f"Command .{cmdname} used by {cmduser} at {cmdtime} in {cmdchannel}, Extra Information: \"{extra}\"")

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