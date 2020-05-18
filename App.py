import discord

client = discord.Client()

# NOTE Credential
credential_token = open("credential.txt", 'r').readline()
credential_riot = open('credential_riot.txt', 'r').readline()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("집사 일")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("!참가"):
        await message.channel.send("안녕하세요")


client.run(credential_token)
