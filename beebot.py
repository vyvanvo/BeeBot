import discord
from discord.ext import commands
import random
from datetime import date
import threading

client = commands.Bot(command_prefix = 'buzz ')
client.remove_command('help')
token = 'ODAwMTAwMzE1MTg5MzQ2MzE2.YANNfA.A3ThDWdomTzPlWMg_WEGhWnGHDw'


#negative words
negative_words = ['bad', 'suck', 'loser']

#qotd
quotes = []

#positive quotes
positive_quotes = []

with open('positive_quotes.txt', encoding='utf8') as f:
    for line in f:
        line = line.strip()
        positive_quotes.append(line)
        quotes.append(line)

#iroh quotes
iroh_quotes = []

with open('uncleiroh_quotes.txt', encoding='utf8') as f:
    for line in f:
        line = line.strip()
        iroh_quotes.append(line)
        quotes.append(line)

#motivational quotes
motivational_quotes = []

with open('motivational_quotes.txt', encoding='utf8') as f:
    for line in f:
        line = line.strip()
        motivational_quotes.append(line)
        quotes.append(line)

#cat url
cat_urls = []

with open('cat_urls.txt', encoding='utf8') as f:
    for line in f:
        line = line.strip()
        cat_urls.append(line)

#dog url
dog_urls = []

with open('dog_urls.txt', encoding='utf8') as f:
    for line in f:
        line = line.strip()
        dog_urls.append(line)


@client.event
#when the bot is ready
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'hello beebot' in message.content.lower() or 'hi beebot' in message.content.lower():
        await message.channel.send(f'hello {message.author.name}!')
    elif 'bye beebot' in message.content.lower():
        await message.channel.send('bye bye!')
    elif 'happy birthday' in message.content.lower():
        await message.channel.send('happy birthday!! :partying_face: :birthday:')
    elif 'sad' in message.content.lower() or 'cry' in message.content.lower():
         await message.channel.send('turn that frown upside down! C:')
    elif 'jazz' in message.content.lower():
        await message.channel.send(':saxophone:  you like jazz?  :saxophone:')
        await message.channel.send('https://tenor.com/view/you-like-jazz-bee-movie-meme-cartoons-pick-up-lines-gif-10421511')
    elif 'i' in message.content.lower() and 'bad' in message.content.lower() and not('not') in message.content.lower():
        await message.channel.send('you are not bad! C:')
    elif 'i' in message.content.lower() and 'suck' in message.content.lower() and not('don\'t') in message.content.lower():
        await message.channel.send('you don\'t suck! C:')
    elif 'i\'m' in message.content.lower() and 'loser' in message.content.lower() and not('not') in message.content.lower():
        await message.channel.send('you\'re a champion!  :triumph: :trophy:')
    else:    
        for word in negative_words:
            if 'you' in message.content.lower() and word in message.content.lower():
                await message.channel.send('that\'s not very nice. :C')
            
    await client.process_commands(message)

    
internal_day = date.today()
internal_quote = random.choice(quotes)

@client.command()
async def qotd(ctx):
    today = date.today()

    global internal_day
    global internal_quote

    print(internal_day)
    
    if today != internal_day :
        internal_quote = random.choice(quotes)
        internal_day = today
    if internal_quote == '' :
        internal_quote = random.choice(quotes)
    await ctx.send(internal_quote)

@client.command()
async def motivation(ctx):
    m_quote = random.choice(motivational_quotes)
    await ctx.send(f'{m_quote}  :triumph:')

@client.command()
async def positive(ctx):
    p_quote = random.choice(positive_quotes)
    await ctx.send(f'{p_quote}  :blush:')

@client.command()
async def iroh(ctx):
    i_quote = random.choice(iroh_quotes)
    await ctx.send(f'{i_quote}  :tea:')    
    
cats_say = ['meoww ~', 'purr ~', 'nyaa ~']

@client.command(aliases=['kitty', 'cat', 'catto'])
async def neko(ctx):
    cat = random.choice(cat_urls)
    cat_list = cat.split()

    embed = discord.Embed(
        title = random.choice(cats_say),
        description = f'[source]({cat_list[0]})',
        colour = discord.Colour.purple()
    )
    embed.set_image(url=cat_list[1])
    await ctx.send(embed=embed)

dogs_say = ['bork!', 'woof!', 'arf!', 'bowow']

@client.command(aliases=['dog', 'doge', 'doggy', 'pup', 'pupper'])
async def doggo(ctx):
    dog = random.choice(dog_urls)
    dog_list = dog.split()
    
    embed = discord.Embed(
        title = random.choice(dogs_say),
        description = f'[source]({dog_list[0]})',
        colour = discord.Colour.teal()
    )
    embed.set_image(url=dog_list[1])
    await ctx.send(embed=embed)    

@client.command()
async def help(ctx):

    helptext = 'to communicate with beebot, please use the \"buzz\" prefix to translate your message into the language of bees!\nthese are the commands that you can use with beebot:\n'
    qotd = '**qotd**: quote of the day!'
    motivation = '**motivation**: motivational quotes!'
    positive = '**positive**: positive, uplifting quotes!'
    iroh = '**iroh**: wise words from the :dragon: dragon of the west :dragon:'
    cat = '**cat/catto/kitty/neko**: cute cat photos!'
    dog = '**dog/doge/doggo/doggy/pup/pupper**: cute doggo pics!'

    description = helptext + '\n' + qotd + '\n' + motivation + '\n' + positive + '\n' + iroh + '\n' + cat + '\n' + dog

    embed = discord.Embed(
        title = 'beebot says hello!',
        #description = 'to communicate with beebot, please use the \"buzz\" prefix to translate your message into the language of bees!\nthese are the commands that you can use with beebot:\n',
        description = description,
        colour = discord.Colour.gold()
    )

    embed.set_footer(text='have a nice day~')
    embed.set_author(name='beebot', icon_url='https://cdn.discordapp.com/attachments/800120744066678826/800162515547324435/bee.jpg')
    #embed.add_field(value='**qotd**: quote of the day!')
    #embed.add_field(name='motivation', value='motivational quotes!')
    #embed.add_field(name='positive', value='positive, uplifting quotes!')
    #embed.add_field(name='iroh', value='wise words from the :dragon: dragon of the west :dragon:')

    await ctx.send(embed=embed)

client.run(token)

