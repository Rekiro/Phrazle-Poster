import discord
import os
import lexico
import phrazle 
import datetime
import asyncio
# import time
import discord.ext
#from discord.utils import get
from discord.ext import commands#, tasks
#from discord.ext.commands import has_permissions, CheckFailure, check
#^ basic imports for other features of discord.py and python ^

#client = discord.Client()

bot = commands.Bot(command_prefix='!', help_command = help())  #put your own prefix here


@bot.event
async def on_ready():
  await bot.change_presence(status = discord.Status.idle, activity = discord.Game('!meaning'))
  print("I'm alive.")  #will print "bot online" in the console when the bot is online

@bot.command(aliases = ['p'])
async def ping(ctx):
  '''Pings the bot and checks for latency'''
  await ctx.send(f'Pong! \n Latency: {round(bot.latency*1000)} milliseconds')

@bot.command()
async def hi(ctx):
  '''Bot greets back the user.'''
  await ctx.reply("Hello " +ctx.author.mention)  #simple command so that when you type "!ping" the bot will respond with "pong!"


# instantiate Lexico class from search_lexico.py
dictionary = lexico.Dictionary()

# no result message
no_result_message = '''Sorry, we can\'t find what you are searching for. But you can search on web here:\n--> https://www.oxfordlearnersdictionaries.com/definition/english/dictionary'''

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
    
  message_content = message.content.lower()  # lower case message

  if f'!define' in message_content:
    '''!define [word] defines the word from a dictionary.'''

    definition, url = dictionary.define(message_content)

    if definition != None:
      
      try:
        await message.channel.send(definition) 
      except Exception as x: 
        await message.channel.send(x)
      
    else:
      await message.channel.send(no_result_message)
      
  await bot.process_commands(message) #makes the bot run other commands as well



@bot.command(aliases = ['a','today', 'today\'s answer'])
async def answer(ctx):
  '''Posts the answer for today\'s Phrazle'''
  answer = phrazle.Phrazle_Answer()
  await ctx.send(answer.one_time())

@bot.command(aliases = ['post answers daily','daily', 'post', 'daily answers'])
async def post_answers_daily(ctx):
  '''Posts the answer for Phrazle on a daily basis'''
  while True: 
    now = datetime.datetime.now()
    then = now + datetime.timedelta(days =1)
    #then = now.replace(hour = 11, minute =46)
    wait_time = (then-now).total_seconds()
    answer = phrazle.Phrazle_Answer()
    await asyncio.sleep(wait_time)

    await ctx.send(answer.daily_answers())
    
#     @bot.command(aliases = ['stop'])
#     def stop_daily_posting(ctx): 
#       break

@bot.command(aliases = ['h'])
async def help(ctx):
  await ctx.send('''```Available Commands
  
answer             :  Posts the answer for today's Phrazle

define <word>      :  Shows the meaning of the <word> with usage examples.

help               :  Shows this message

hi                 :  Bot greets back the user

ping               :  Pings the bot and checks for latency

post answers daily :  Posts the answer for Phrazle on a daily basis```''')

try:
  bot.run(os.getenv('TOKEN'))
except:
  os.system("kill 1")


  
