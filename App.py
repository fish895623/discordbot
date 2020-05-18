import discord

client = discord.Client()

token_credential = open("credential.txt", 'r').readline()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("집사")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("!안녕"):
        await message.channel.send("안녕하세요")


client.run(token_credential)
