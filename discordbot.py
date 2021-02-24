from discord.ext import commands
import os
import traceback

import discord
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def nagayan(ctx):

    msg = 'test message'

    # メンバーリストを取得
    state = ctx.author.voice # コマンド実行者のVCステータスを取得
    if state is None: 
        return False
    
    channel_id = state.channel.id
    channel_info = client.get_channel(channel_id) 
    
    members = channel_info.members #finds members connected to the channel
    for member in members:
        await member.send('aa')
  
    await ctx.send(members)

bot.run(token)

