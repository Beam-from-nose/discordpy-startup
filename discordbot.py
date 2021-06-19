from discord.ext import commands
import os
import traceback
import random
import datetime
import time

import discord

from discord.ext import tasks

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix="/", intents=intents)
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_command_error(ctx, error):
	orig_error = getattr(error, "original", error)
	error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
	print(error_msg)

@bot.event
async def on_message(message):
	
	if message.channel.id == 801807475208224798:
			
		target = message.author
		join_date = datetime.datetime.now() - datetime.timedelta(days=28)
		
		if join_date <= target.joined_at:
			role = message.guild.get_role(844138721200439338)
			# 入ってきた Member に役職を付与
			await target.add_roles(role)

	await bot.process_commands(message)

@bot.command()
async def tes(ctx):
	
	guild = ctx.author.guild
	role = guild.get_role(844138721200439338)
	
	join_date = datetime.datetime.now() - datetime.timedelta(days=28)

	tdatetime = datetime.datetime.now()
	tstr = tdatetime.strftime('%Y/%m/%d')
	
	await ctx.send('処理を開始します(' + tstr + ')')
	
	for target in role.members:
		if target.joined_at <= join_date:
			await target.remove_roles(role)
			
			if target.nick == None:
				message = target.name + 'さんのロールを外しました 参加日：' + target.joined_at.strftime('%Y/%m/%d')
			else:
				message = target.nick + 'さんのロールを外しました 参加日：' + target.joined_at.strftime('%Y/%m/%d')
			await ctx.send(message)

	await ctx.send('処理を完了しました')

			
	await ctx.message.delete()

# 300秒に一回ループ
@tasks.loop(seconds=3600)
async def loop():	

	await bot.wait_until_ready()
	guild = bot.get_guild(799680125024337950)
	channel = guild.get_channel(844220827369209857)

	now = datetime.datetime.now().strftime('%H')
	if now == '01':
		role = guild.get_role(844138721200439338)

		join_date = datetime.datetime.now() - datetime.timedelta(days=28)

		tdatetime = datetime.datetime.now()
		tstr = tdatetime.strftime('%Y/%m/%d')

		await channel.send('処理を開始します(' + tstr + ')')

		for target in role.members:
			if target.joined_at <= join_date:
				await target.remove_roles(role)

				if target.nick == None:
					message = target.name + 'さんのロールを外しました 参加日：' + target.joined_at.strftime('%Y/%m/%d')
				else:
					message = target.nick + 'さんのロールを外しました 参加日：' + target.joined_at.strftime('%Y/%m/%d')
				await channel.send(message)

		await channel.send('処理を完了しました')

loop.start()


bot.run(token)
