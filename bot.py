from discord.ext import commands
import random
import math
import asyncio
import onetimepad
import string

command_prefix="-"
bot = commands.Bot(command_prefix="-")
bot.remove_command("help")

#COMMANDS
cmddict={
    #-command [argument]: ["What command does.","arguments","usage example 1","usage example 2"]
    "help": ["Lists all commands and what they do.","command name (optional)","-help","-help quote"],
    "say": ["Repeats message content.","text to repeat","-say PoryBot","-say :pensive:"],
    "starbucks":["Randomly generates a Starbucks order.","Takes no arguments.","-starbucks"," "],
    "rps":["Plays rock paper scissors with PoryBot.","rock/paper/scissors","-rps rock","-rps scissors"],
    "death":["Gives you a Minecraft death.","Takes no arguments","-death",""],
    "encrypt":["Encrypts a message using uncrackable one time pad encryption.","message","-encrypt \"porybot rules\"","-encrypt hungry"],
    "decrypt":["Decrypts a one time pad cipher.","cipher, key","-decrypt 0b1d0704191c chickens","-decrypt 415d414d575943184b445c5442 1234567891011"],
    "sans":["You're Gonna Have A Bad Time..................","Takes no arguments","-sans"," "],
    "nothing":["It just doesn't do anything lol","Why would this have arguments","-nothing"," "],
    "darkstarbucks":["A random Starbucks order, but dark.","Takes no arguments","-darkstarbucks"," "],
    "number":["Generates a random number.","Takes no arguments","-number"," "],
    "ship":["Ships you/specified person with someone.","person to ship","-ship","-ship PoryBot"],
    "tiktok":["Posts a random TikTok video.","Takes no arguments","-tiktok"," "],
}


'''TO-DO LIST:
add more minecraft deaths

'''
#GENERAL FUNCTIONS#########################################################################

def rstring(len):
    printable=string.punctuation+string.ascii_letters+string.digits
    key=""
    for x in range(0,int(len)+1):
        key=key+random.choice(printable)
    return key

#ASYNC FUNCTIONS###########################################################################

@bot.command()
async def tiktok(ctx):
    tiktoks=["https://www.youtube.com/watch?v=49zOqNy3zFI","https://www.youtube.com/watch?v=cRWtUBlfEJE",""]

@bot.command()
async def say(ctx,*,content:str):
    await ctx.send(content)

@bot.command()
async def help(ctx,*,command=""):
    toprint=""
    if command=="":
        for cmd in cmddict:
            toprint=toprint+"`"+cmd+"`"+" --------------- "+cmddict[cmd][0]+"\n"
    elif command not in cmddict:
        toprint="Not a valid command. Be sure to omit the prefix of the command you need help with!"
    else:
        toprint="**"+command.upper()+" usage:** \n"+cmddict[command][0]+"\n \n"+"**Arguments:** \n"+cmddict[command][1]+" \n \n**Examples:**\n`"+cmddict[command][2]+"`\n`"+cmddict[command][3]+"`"
    await ctx.send(toprint)

@bot.command()
async def starbucks(ctx):
    drinks=["latte","cappuccino","coffee","frappuccino"]
    sizes=["Tall","Grande","Venti"]
    flavors=["caramel","peppermint","pumpkin spice","vanilla","vanilla bean","salted caramel","chai","mocha"]
    xtra=["extra whipped cream","extra froth","extra ice"]
    milks=["coconut milk","almond milk","whole milk","soy milk","organic milk","skim milk"]
    frapflavors=["strawberry","caramel","mocha","pumpkin spice","vanilla","salted caramel","cupcake","maple pecan","white chocolate"]
    iced=random.randint(1,5)#1/4 chance its iced
    extras=random.randint(1,5)#1-5 no extras, 6-9 each different extra
    size=random.choice(sizes)#size
    decaf=random.randint(1,5)#1/4 chance its decaf
    milk=random.randint(1,5)#1/4 chance choose from milks
    espresso=random.randint(1,16)#1-5 shots espresso, 2/3 no extra
    drink=random.choice(drinks)
    flavor=random.choice(flavors)
    pumps=random.randint(1,21)#1-5 pumps of flavor, 3/4 chance no
    size=size+" "
    if iced==4:
        iced="iced "
    else:
        iced=""
    if decaf==1:
        decaf="decaf "
    else:
        decaf=""
    if pumps>=6:
        flavor=flavor+" "
    drink=drink+" "
    if pumps<6:
        pumps="with "+str(pumps)+" pumps of "+flavor+" "
    else:
        pumps=""
    if milk==4:
        milk="with "+random.choice(milks)+" "
    else:
        milk=""
    if espresso<6 and drink is not "coffee":
        espresso="with "+str(espresso)+" shots of espresso "
    else:
        espresso=""
    if extras==4:
        extras="with "+random.choice(xtra)
    else:
        extras=""
    if drink=="coffee ":
        espresso=""
    if drink=="frappuccino ":
        flavor=random.choice(frapflavors)+" "
        iced=""
    if " " not in flavor:
        flavor=""

    order=size+iced+decaf+flavor+drink+pumps+milk+espresso+extras
    await ctx.send(order)

@bot.command()
async def death(ctx):
    killer=["a creeper","a skeleton",random.choice(ctx.guild.members).mention,"an enderman","a zombie","a spider",random.choice(ctx.guild.members).mention,"Drowned","husk","polar bear","wolf",random.choice(ctx.guild.members).mention,random.choice(ctx.guild.members).mention]
    messages=[" was shot by an arrow"," was shot by "+random.choice(killer)," was pricked to death"," walked into a cactus whilst trying to escape "+random.choice(killer)," drowned"," drowned whilst trying to escape "+random.choice(killer)," suffocated in a wall"," was blown up by a creeper"," hit the ground too hard"," fell from a high place"," fell off a ladder"," fell into a patch of fire"," fell into a patch of cacti"," went up in flames"," burned to death"," tried to swim in lava"," was slain by "+random.choice(killer)," was killed by magic"," starved to death"," fell out of the world"," died"," fell out of the world"," was pummeled by "+random.choice(ctx.guild.members).mention," withered away"," experienced kinetic energy"," removed an elytra while flying"," was killed by [Intentional Game Design]"," was squashed by a falling anvil"," was struck by lightning"," discovered the floor was lava"," was impaled by"+random.choice(killer)]
    await ctx.send(ctx.author.mention+random.choice(messages))

@bot.command()
async def encrypt(ctx,input):
    key=rstring(len(input)+1)
    try:
        cipher=onetimepad.encrypt(input,key)
        await ctx.send("```ENCRYPTED MESSAGE: \n"+cipher+"\nKEY:\n"+key+"```\nDon't lose your key, or you won't be able to decrypt it!")
    except:
        await ctx.send("Usage: -encrypt [message]")

@bot.command()
async def decrypt(ctx,cipher,key):
        try:
            cipher=onetimepad.decrypt(cipher,key)
            await ctx.send("```DECRYPTED MESSAGE: \n"+cipher+"```")
        except:
            await ctx.send("izzy fix ur code it ran an error")



#GAMES ETC####################################################

@bot.command()
async def rps(ctx,*,choice="0"):
    possible=["rock","paper","scissors"]
    if choice not in possible:
        await ctx.send("Please type 'rock', 'paper', or 'scissors' after the command!")
        return
    comp=random.choice(possible)
    win=True
    await ctx.send("PoryBot has chosen "+comp+".")
    if comp==choice:
        await ctx.send("Aaaah! It's a tie!")
        return
    elif choice=="rock":
        if comp=="paper":
            win=False
    elif choice=="paper":
        if comp=="scissors":
            win=False
    elif choice=="scissors":
        if comp=="rock":
            win=False
    if win==True:
        prizes=["liver.","gentrified popsicles.","soy sauce.","GoGurt:tm:.","ashes.","Minecraft dirt.","lozenges.","vintage beanie babies.","Soundcloud fame.","clown shoes.","sarcophagus juice.","soup.","Fiji:tm: water.","Vine followers.","Reddit Gold.","apple juice.","Discord Nitro.","free real estate.","The Elder Scrolls V: Skyrim"]
        await ctx.send(ctx.author.mention+" has beaten PoryBot! Here, have some "+random.choice(prizes))
    elif win==False:
        await ctx.send("Sorry! PoryBot wins. Better luck next time! :P")

@bot.command()
async def ship(ctx,*,user="00"):
    ships=["Shrek","Sans Undertale","Darkiplier","Mr. Krabs","Bill Cipher","MatPat","Venom","Matsuno Karamatsu","The Onceler","Tord Eddsworld","Junkrat","Sandy Cheeks","Bowsette","BBC's Sherlock","Ross from Friends","Michael Scott","Leslie Knope","Bayonetta","Murdoc Gorillaz","Hades as portrayed in the Disney feature-length animated film 'Hercules'","Fortnite","Dirt","Jimmy John himself","Marge Simpson"]
    if user=="00":
        await ctx.send("PoryBot ships "+ctx.author.mention+" with "+random.choice(ships)+".")
    else:
        await ctx.send("PoryBot ships "+user+" with "+random.choice(ships)+".")



#DARK COMMANDS#########################################################

@bot.command()
async def number(ctx):
    numbers=["69","420"]
    await ctx.send(random.choice(numbers))

@bot.command()
async def darkstarbucks(ctx):
    drinks=["latte","cappuccino","coffee","frappuccino"]
    sizes=["Tall","Grande","Venti","Trenta","A gallon of"]
    flavors=["blood","meat","skin","kale","sand","7up","[REDACTED]","tubby custard","bouillon","gasoline","dirt","bone meal","mystery flavor","DayQuil","salted-caramel-but-instead-of-salt-it's-cigarette-ashes"]
    xtra=["[REDACTED]","the blood of a virgin","Pepsi:tm:","extra pulp","holy water","soy sauce","activated coal"]
    milks=["breastmilk","ambrosia","tomato paste","chicken broth","clown juice","old greek yogurt","Pure Ass:tm:"]
    pumpflavors=["guilt","horny goat weed","[REDACTED]","void","[REDACTED]","bone-hurting juice","arm juice","sarcophagus juice","tomato sauce","vodka","love potion no. 9","NyQuil","toilet water","bong water","gentrification",":thinking:"]
    iced=random.randint(1,5)#1/4 chance its iced
    extras=random.randint(1,5)#1-5 no extras, 6-9 each different extra
    size=random.choice(sizes)#size
    decaf=random.randint(1,5)#1/4 chance its decaf
    milk=random.randint(1,5)#1/4 chance choose from milks
    espresso=random.randint(1,50)#1-5 shots espresso, 2/3 no extra
    drink=random.choice(drinks)
    flavor=random.choice(flavors)
    pumps=random.randint(1,500)#1-5 pumps of flavor, 3/4 chance no
    pumps2=random.randint(1,25)
    size=size+" "
    if iced==4:
        iced="iced "
    else:
        iced=""
    if decaf==1:
        decaf="decaf "
    else:
        decaf=""
    if pumps>=10:
        flavor=flavor+" "
    drink=drink+" "
    if pumps<150:
        pumps="with "+str(pumps)+" pumps of "+random.choice(pumpflavors)+" "
        if pumps2>=10:
            pumps2=""
        else:
            pumps2="and "+str(pumps2)+" pumps of "+random.choice(pumpflavors)+" "
    else:
        pumps=""
        pumps2=""
    if milk==4:
        milk="with "+random.choice(milks)+" "
    else:
        milk=""
    if espresso<25 and drink is not "coffee":
        espresso="with "+str(espresso)+" shots of espresso "
    else:
        espresso=""
    if extras==4:
        extras="with "+random.choice(xtra)
    else:
        extras=""
    if drink=="coffee ":
        espresso=""
    if drink=="frappuccino ":
        iced=""

    order=size+iced+decaf+flavor+drink+pumps+pumps2+milk+espresso+extras
    await ctx.send(order)


@bot.command()
async def sans(ctx):
    await ctx.send('''█████████████▀▀▀▀▀▀▀▀▀▀▀▀▀███████████
████████▀▀░░░░░░░░░░░░░░░░░░░▀▀██████
██████▀░░░░░░░░░░░░░░░░░░░░░░░░░▀████
█████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░███
████░░░░░▄▄▄▄▄▄▄░░░░░░░░▄▄▄▄▄▄░░░░░██
████░░▄██████████░░░░░░██▀░░░▀██▄░░██
████░░███████████░░░░░░█▄░░▀░░▄██░░██
█████░░▀▀███████░░░██░░░██▄▄▄█▀▀░░███
██████░░░░░░▄▄▀░░░████░░░▀▄▄░░░░░████
█████░░░░░█▄░░░░░░▀▀▀▀░░░░░░░█▄░░░███
█████░░░▀▀█░█▀▄▄▄▄▄▄▄▄▄▄▄▄▄▀██▀▀░░███
██████░░░░░▀█▄░░█░░█░░░█░░█▄▀░░░░██▀▀
▀░░░▀██▄░░░░░░▀▀█▄▄█▄▄▄█▄▀▀░░░░▄█▀░░░
▄▄▄░░░▀▀██▄▄▄▄░░░░░░░░░░░░▄▄▄███░░░▄█
██████▄▄░░▀█████▀█████▀██████▀▀░░▄███
██████████▄░░▀▀█▄░░░░░▄██▀▀▀░▄▄▄███▀▄
███████████░██░▄██▄▄▄▄█▄░▄░████████░█''')

bot.run("bot token here")
