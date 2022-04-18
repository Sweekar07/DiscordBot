import discord
from discord.ext import commands
from pymongo import MongoClient
import requests
import json
import random

mango_url = "mongodb+srv://Sweekar07:gO2KaO6QPMD7V1Em@discord-db.pid7h.mongodb.net/test"
cluster = MongoClient(mango_url)
#"mongodb+srv://TutorialBot:Mack68@$@tutorialcluster-yywug.mongodb.net/test"
db = cluster["UserData"]
collection = db["userdata"]
dblist = cluster.list_database_names()

#client = discord.Client()
client=commands.Bot(command_prefix='$')

f=open("E:\\DiscordBot\\DB\\token.txt","r")
lines=f.readlines()
key=lines[0]
f.close()



def get_quote():
    response=requests.get("https://zenquotes.io/api/random")
    json_data= json.loads(response.text)
    quote = json_data[0] ['q'] + " -" + json_data[0] ['a'] 
    return(quote)



@client.event
async def on_ready():
  print(f'{client.user} has connected to Discord!')


            
@client.event
async def on_message(ctx):
    if ctx.author==client.user:
        return 
    print(f"{ctx.channel}: {ctx.author}: {ctx.author.name}: {ctx.content}")
    myquery={"_id": ctx.author.id,}
    if (collection.count_documents(myquery) == 0):
        if "python" in str(ctx.content.lower()):
            post = {"_id": ctx.author.id, "name": ctx.author.name, "score": 1,}
            collection.insert_one(post)
            await ctx.channel.send('accepted!')
        elif "discord" in str(ctx.content.lower()):
            post = {"_id": ctx.author.id,"name": ctx.author.name ,"score": 1}
            collection.insert_one(post)
            await ctx.channel.send('accepted!')
        elif "lego" in str(ctx.content.lower()):
            post = {"_id": ctx.author.id, "name": ctx.author.name,"score": 1}
            collection.insert_one(post)
            await ctx.channel.send('accepted!')
        elif "code" in str(ctx.content.lower()):
            post = {"_id": ctx.author.id,"name": ctx.author.name ,"score": 1}
            collection.insert_one(post)
            await ctx.channel.send('accepted!')
    else:
        if "python" in str(ctx.content.lower()):
            query = {"_id": ctx.author.id,}
            user = collection.find(query)
            for result in user:
                score = result["score"]
            score = score + 1
            collection.update_one({"_id":ctx.author.id}, {"$set":{"score":score, "name": ctx.author.name}})
            await ctx.channel.send('accepted!')
        elif "discord" in str(ctx.content.lower()):
            query = {"_id": ctx.author.id}
            user = collection.find(query)
            for result in user:
                score = result["score"]
            score = score + 1
            collection.update_one({"_id":ctx.author.id}, {"$set":{"score":score}})
            await ctx.channel.send('accepted!')
        elif "lego" in str(ctx.content.lower()):
            query = {"_id": ctx.author.id}
            user = collection.find(query)
            for result in user:
                score = result["score"]
            score = score + 1
            collection.update_one({"_id":ctx.author.id}, {"$set":{"score":score}})
            await ctx.channel.send('accepted!')
        elif "code" in str(ctx.content.lower()):
            query = {"_id": ctx.author.id}
            user = collection.find(query)
            for result in user:
                score = result["score"]
            score = score + 1
            collection.update_one({"_id":ctx.author.id}, {"$set":{"score":score}})
            await ctx.channel.send('accepted!')
 
    if ctx.content.startswith('$toss'):
    #if "$toss" in str(ctx.content.lower()):
        x=["heads","tails"]
        y=random.choice(x)
        if y=="heads":
            print("It's a head")
            await ctx.channel.send("Its a heads congrats...///")
        elif y=="tails":
            print("It's a tail")
            await ctx.channel.send("Its a tail congrats...///")
    
    if ctx.content.startswith('$inspire'):
        quote=get_quote()
        await ctx.channel.send(quote)

    if ctx.content.startswith('$version'):
        Myembed=discord.Embed(title='Current Version', description="Version 1.0", colour=0x00ff00)
        Myembed.add_field(name="Version Code:", value='1.0.0', inline=False)
        Myembed.add_field(name='Date Released:', value='April 1st, 2022', inline=False)
        Myembed.set_footer(text='This is a sample footer')
        Myembed.set_author(name='Sweekar')
        await ctx.channel.send(embed=Myembed)
    

client.run(key)
