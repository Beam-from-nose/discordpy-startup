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
        i = i + 1


@bot.command()
async def kj(ctx,imno1,imno2=None):
    
    # メンバーリストを取得
    state = ctx.author.voice # コマンド実行者のVCステータスを取得
    if state is None: 
        return False
    
    #members = state.channel.members  
    members = [
        '1', 
        '2', 
        '3',
        '4',
        '5',
        '6', 
        '7', 
        '8',
        '9',
        '10'
    ]
    members_count = len(members) # 人数取得
        
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
        if role_list[m] == 1:
            #await member.send('あなたは狂人です')
            await ctx.send('あなたは狂人です')
        else:
            if two_mode == True:
                if m == imno1 or m == imno2:
                    if kill_flag == True:
                        #await member.send('あなたはキルできるインポスター')
                        await ctx.send('あなたはキルできるインポスター')
                        kill_flag = False 
                    else:
                        #await member.send('あなたはキルできないインポスター')
                        await ctx.send('あなたはキルできないインポスター')
                        kill_flag = True 
                else:
                    #await member.send('あなたはクルー')
                    await ctx.send('あなたはクルー')
            else:
                #await member.send('あなたはクルー')
                await ctx.send('あなたはクルー')

        m = m + 1

bot.run(token)
