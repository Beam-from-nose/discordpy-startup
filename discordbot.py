from discord.ext import commands
import os
import traceback
import random

import discord
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix="/", intents=intents)
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_command_error(ctx, error):
	orig_error = getattr(error, "original", error)
	error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
	await ctx.send(error_msg)

@bot.command()
async def act(ctx):

	act_list = [
		'緊急ボタン禁止', 
		'死体レポート禁止', 
		'位置情報と監視カメラ禁止',
		'停電とコミュサボの修理禁止',
		'緊急ボタン禁止',
		'緊急ボタン禁止', 
		'死体レポート禁止', 
		'位置情報と監視カメラ禁止',
		'停電とコミュサボの修理禁止',
		'死体レポート禁止'
	]

	random.shuffle(act_list)
	
	# メンバーリストを取得
	state = ctx.author.voice # コマンド実行者のVCステータスを取得
	if state is None: 
		return False
	
	i = 0

	members = state.channel.members
	for member in members:
		await member.send(act_list[i])
		i = i + 1
		
	message = ctx.message
	print(ctx)	
	await message.delete(delay=1.2)

	

@bot.command()
async def show(ctx):
	
	# メンバーリストを取得
	state = ctx.author.voice # コマンド実行者のVCステータスを取得
	if state is None: 
		return False
	
	members = state.channel.members
	members_count = len(members) # 人数取得

	i = 0
	messages = []
	for member in members:
		if member.voice.self_mute == True:
			continue
			
		if member.nick == None:
			messages.append(str(i) + '-' + member.name)
		else:
			messages.append(str(i) + '-' + member.nick)		 
		i = i + 1
		
	if len(messages) == 0:
		return False
	
	message = '\n'.join(messages)
	send_message = await ctx.send(message)
	list = [
		'\N{DIGIT ZERO}\N{COMBINING ENCLOSING KEYCAP}', 
		'\N{DIGIT ONE}\N{COMBINING ENCLOSING KEYCAP}', 
		'\N{DIGIT TWO}\N{COMBINING ENCLOSING KEYCAP}',
		'\N{DIGIT THREE}\N{COMBINING ENCLOSING KEYCAP}',
		'\N{DIGIT FOUR}\N{COMBINING ENCLOSING KEYCAP}',
		'\N{DIGIT FIVE}\N{COMBINING ENCLOSING KEYCAP}', 
		'\N{DIGIT SIX}\N{COMBINING ENCLOSING KEYCAP}', 
		'\N{DIGIT SEVEN}\N{COMBINING ENCLOSING KEYCAP}',
		'\N{DIGIT EIGHT}\N{COMBINING ENCLOSING KEYCAP}',
		'\N{DIGIT NINE}\N{COMBINING ENCLOSING KEYCAP}',
		'\N{BLACK RIGHT-POINTING TRIANGLE}',
		'\N{LEFTWARDS ARROW WITH HOOK}',
		'\N{NO ENTRY}'

	]
	for a in list:
		await send_message.add_reaction(a)
	

@bot.command()
async def smute(ctx):
	
	# メンバーリストを取得
	state = ctx.author.voice # コマンド実行者のVCステータスを取得
	if state is None: 
		return False
	
	message = "セミオートミュート"
	send_message = await ctx.send(message)
	list = [
		'\N{SPEAKER}', 
		'\N{SPEAKER WITH CANCELLATION STROKE}',
		'\N{END WITH LEFTWARDS ARROW ABOVE}',
		'\N{NO ENTRY}'
	]
	for a in list:
		await send_message.add_reaction(a)
	
@bot.event
async def on_reaction_add(reaction, user):

	#スタート以外はスルー
	if reaction.emoji == "▶":
		message = reaction.message
	elif reaction.emoji == "↩":
		message = reaction.message
	elif reaction.emoji == "⛔":
		message = reaction.message
	elif reaction.emoji == "🔈":
		message = reaction.message
	elif reaction.emoji == "🔇":
		message = reaction.message
	elif reaction.emoji == "🔚":
		message = reaction.message
	else:
		return False

	
	#押したのが人間かつ押されたのがながやbot
	if user.bot == False and message.author.id == 814061487647490118 :
		
		# ストップならメッセージ削除	
		if reaction.emoji == "⛔":
			await message.delete(delay=1.2)
			return False

		# 繰り返しならメンバーリロード
		if reaction.emoji == "↩":
			# メンバーリストを取得
			state = user.voice # コマンド実行者のVCステータスを取得
			if state is None: 
				return False

			members = state.channel.members
			members_count = len(members) # 人数取得

			i = 0
			messages = []
			for member in members:
				if member.voice.self_mute == True:
					continue

				if member.nick == None:
					messages.append(str(i) + '-' + member.name)
				else:
					messages.append(str(i) + '-' + member.nick)		 
				i = i + 1

			if len(messages) == 0:
				return False

			send_message = '\n'.join(messages)
			await message.edit(content=send_message)
			
			return False
		
		#参加者のミュート解除
		if reaction.emoji == "🔈":
			#リアクション初期化
			async for user in reaction.users():
				if user.bot == False:
					await reaction.remove(user)
			
			# メンバーリストを取得
			state = user.voice # コマンド実行者のVCステータスを取得
			if state is None: 
				return False

			members = state.channel.members
			for member in members:
				print(member)
				print(member.nick)
				print("()" in member.nick)
				if "()" in member.nick == True:
					continue
				if member.voice.self_mute == True:
					continue
				elif member.voice.mute == False:
					await member.edit(mute=True) # マイクミュート
				elif member.voice.mute == True and member.voice.deaf == True:				
					await member.edit(mute=False) # マイクミュート解除
					await member.edit(deafen=False) # スピーカーミュート解除


		#参加者のミュート
		if reaction.emoji == "🔇":
			#リアクション初期化
			async for user in reaction.users():
				if user.bot == False:
					await reaction.remove(user)

			# メンバーリストを取得
			state = user.voice # コマンド実行者のVCステータスを取得
			if state is None: 
				return False

			members = state.channel.members
			for member in members:
				if "()" in member.nick == True:
					continue
				if member.voice.self_mute == True:
					continue
				elif member.voice.mute == True and member.voice.deaf == False:
					await member.edit(mute=False) # マイクミュート解除
				else:
					await member.edit(mute=True) # マイクミュート
					await member.edit(deafen=True) # スピーカーミュート

		#参加者のミュート解除
		if reaction.emoji == "🔚":
			#リアクション初期化
			async for user in reaction.users():
				if user.bot == False:
					await reaction.remove(user)

			# メンバーリストを取得
			state = user.voice # コマンド実行者のVCステータスを取得
			if state is None: 
				return False
			members = state.channel.members

			for member in members:	
				await member.edit(mute=False) # チャンネルの参加者をミュート解除する
				await member.edit(deafen=False) # チャンネルの参加者をミュート解除する

		#投稿のリアクション状況を取得
		if reaction.emoji == "↩":
			i = 0;
			imno1 = None
			imno2 = None

			for r in message.reactions:

				if r.count > 1:
					if imno1 == None:
						imno1 = i
					else:
						imno2 = i
				i = i + 1
				if i == 10:
					break

			if imno1 == None:
				return False
			print(imno1)
			print(imno2)
			# メンバーリストを取得
			state = user.voice # コマンド実行者のVCステータスを取得
			if state is None: 
				return False

			members = state.channel.members
			members_count = 0
			for mem in members:
				if mem.voice.self_mute == True:
					continue

				members_count = members_count + 1

			#人数チェック
			if members_count < 3:
				#await ctx.send('ボイスチャンネルの人数が少なすぎます')
				return False

			#人数分の役職
			role_list = []
			for i in range(members_count):

				if i == 0:
					role_list.append(1)
				else:
					role_list.append(0)

			while True:
				random.shuffle(role_list)

				#インポスター1人
				if imno2 == None:
					if role_list[int(imno1)] == 0:
						two_mode = False
						break

				#インポスター2人
				else:
					if role_list[int(imno1)] == 0 and role_list[int(imno2)] == 0:
						two_mode = True
						if random.random() >= 0.5:
							kill_flag = True 
						else:
							kill_flag = False
						break

			m = 0
			for member in members:

				if member.voice.self_mute == True:
					continue	

				if role_list[m] == 1:
					await member.send('あなたは狂人')
					#await ctx.send('あなたは狂人')
				else:
					if two_mode == True:
						if m == int(imno1) or m == int(imno2):
							if kill_flag == True:
								await member.send('あなたはキルできるインポスター')
								#await ctx.send('あなたはキルできるインポスター')
								kill_flag = False 
							else:
								await member.send('あなたはキルできないインポスター')
								#await ctx.send('あなたはキルできないインポスター')
								kill_flag = True 
						else:
							await member.send('あなたはクルー')
							#await ctx.send('あなたはクルー')
					else:
						if m == int(imno1):
							await member.send('あなたはインポスター')
							#await ctx.send('あなたはキルできるインポスター')

						else:
							await member.send('あなたはクルー')
							#await ctx.send('あなたはクルー')

				m = m + 1

			#リアクション初期化
			await message.clear_reactions()
			list = [
				'\N{DIGIT ZERO}\N{COMBINING ENCLOSING KEYCAP}', 
				'\N{DIGIT ONE}\N{COMBINING ENCLOSING KEYCAP}', 
				'\N{DIGIT TWO}\N{COMBINING ENCLOSING KEYCAP}',
				'\N{DIGIT THREE}\N{COMBINING ENCLOSING KEYCAP}',
				'\N{DIGIT FOUR}\N{COMBINING ENCLOSING KEYCAP}',
				'\N{DIGIT FIVE}\N{COMBINING ENCLOSING KEYCAP}', 
				'\N{DIGIT SIX}\N{COMBINING ENCLOSING KEYCAP}', 
				'\N{DIGIT SEVEN}\N{COMBINING ENCLOSING KEYCAP}',
				'\N{DIGIT EIGHT}\N{COMBINING ENCLOSING KEYCAP}',
				'\N{DIGIT NINE}\N{COMBINING ENCLOSING KEYCAP}',
				'\N{BLACK RIGHT-POINTING TRIANGLE}',
				'\N{LEFTWARDS ARROW WITH HOOK}',
				'\N{NO ENTRY}'
			]
			for a in list:
				await message.add_reaction(a)

bot.run(token)
