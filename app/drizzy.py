from pathlib import Path
import discord
from aitextgen import aitextgen
from discord.ext import commands
import os
from datetime import datetime


bot = commands.Bot(command_prefix='~')
token = 'OTg4OTYzNjU1NzQ1OTU3ODg4.GerOP4.5fB9YjERszqrEyDWUzXIu41isAMx6bBgs5A_Tw'

ai = aitextgen(model_folder="model1/")
dirpath = os.getcwd()
now = datetime.now().hour + 1  # this represents EST.


@bot.command()
async def generate(ctx, *, prompt):
    '''
    Function: generates text randomly or based on a prompt. 
    '''

    message = await ctx.send('Thinking...')
    output = ai.generate(n=2,
                         max_length=120,
                         prompt=prompt,
                         temperature=0.8,
                         return_as_list=True)
    await message.edit(content='\n\n'.join(output))


bot.run(token)
