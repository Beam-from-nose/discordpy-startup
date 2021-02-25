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
async def limit_act(ctx):

    act_list = [
        '緊急ボタン禁止', 
        '死体レポート禁止', 
        '位置情報と監視カメラ禁止',
        '停電とコミュサボの修理禁止',
        '緊急タスク時、アドミン側とリアクター上部の修理禁止',
        '緊急ボタン禁止', 
        '死体レポート禁止', 
        '位置情報と監視カメラ禁止',
        '停電とコミュサボの修理禁止',
        '緊急タスク時、アドミン側とリアクター上部の修理禁止'
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
        i = i+ 1

bot.run(token)

@bot.command()
async def kyojin(ctx,*imposter_no):
    
    # メンバーリストを取得
    state = ctx.author.voice # コマンド実行者のVCステータスを取得
    if state is None: 
        return False
    
    members = state.channel.members
    members_count = len(members) # 人数取得

    #人数分の役職
    role_list = []
    for i in range(members_count):
        
        if i == 0:
            role_list.append(1)
        else:
            role_list.append(0)
     
    
    for member in members:
        if role_list[m] == 1:
            await member.send('あなたは狂人です')

        m = m + 1

bot.run(token)
