import discord
import os
import search_lexico
# import time
import discord.ext
#from discord.utils import get
from discord.ext import commands#, tasks
#from discord.ext.commands import has_permissions, CheckFailure, check
#^ basic imports for other features of discord.py and python ^

client = discord.Client()

client = commands.Bot(command_prefix='!')  #put your own prefix here


@client.event
async def on_ready():
  print("bot online")  #will print "bot online" in the console when the bot is online


@client.command()
async def hi(ctx):
  await ctx.send("Hello " +ctx.author.mention)  #simple command so that when you type "!ping" the bot will respond with "pong!"


# instantiate Lexico class from search_lexico.py
dictionary = search_lexico.Lexico()

# no result message
no_result_message = '''Sorry, we can\'t find what you are searching for. But you can search on web here:\n--> https://www.oxfordlearnersdictionaries.com/definition/english/dictionary'''


@client.event
async def on_message(message):
  if message.author == client.user:
    return
    
  message_content = message.content.lower()  # lower case message

  if f'!meaning' in message_content:

    key_words, phrase = dictionary.key_words_search_words(message_content)
    Meaning, Examples = dictionary.search(key_words)


    if Meaning != None:
      await message.channel.send('-\n***__{}__***\n\n{}\n\nExamples:-'.format(phrase, Meaning.text)) 
      for i in range(1,len(Examples)): # No_1_catalog_content
        try:
          await message.channel.send('> {}. *{}*'.format(i, Examples[i].text))
        except IndexError:
          break
    else:
      await message.channel.send(no_result_message)


try:
  client.run(os.getenv('TOKEN'))
except:
  os.system("kill 1")
#get your bot token and create a key named `TOKEN` to the secrets panel then paste your bot token as the value.
#to keep your bot from shutting down use https://uptimerobot.com then create a https:// monitor and put the link to the website that appewars when you run this repl in the monitor and it will keep your bot alive by pinging the flask server
#enjoy!

  
#async def kick(ctx, member : discord.Member):
#    try:
#        await member.kick(reason=None)
#        await ctx.send("kicked "+member.mention) #simple kick command to demonstrate how to get and use member mentions
#    except:
#        await ctx.send("bot does not have the kick members permission!")

 # anything
