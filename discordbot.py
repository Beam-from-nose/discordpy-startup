from discord.ext import commands
import os
import traceback

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
   
    users = [member.display_name for member in state.channel.members]
    
    for user in users:
            m =  user
            await client.send_message(message.channel, m)

bot.run(token)

