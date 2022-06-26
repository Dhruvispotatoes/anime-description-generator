from aitextgen import aitextgen
from discord.ext import commands

bot = commands.Bot(command_prefix='~')
token = ''

ai = aitextgen(model_folder="model1/")


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
