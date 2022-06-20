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
  await client.change_presence(status = discord.Status.idle, activity = discord.Game('!meaning'))
  print("I'm alive.")  #will print "bot online" in the console when the bot is online


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
      
      Example_set = ''
      for ex in range(1, 17):
        try:
          i = '> ' + str(ex)
          Example_set = Example_set + i + '. *' + Examples[ex].text+ '*\n'
        except IndexError: 
          break
      try:
        await message.channel.send('-\n***__{}__***\n\n{}\n\nExamples:-\n{}'.format(phrase, Meaning.text, Example_set)) 
      except Exception as x: 
        await message.channel.send(x)
      # for i in range(1,len(Examples)): # No_1_catalog_content
      #   try:
      #     await message.channel.send('> {}. *{}*'.format(i, Examples[i].text))
      #   except IndexError:
      #     break
    else:
      await message.channel.send(no_result_message)



try:
  client.run(os.getenv('TOKEN'))
except:
  os.system("kill 1")


  
