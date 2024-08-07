import discord
import random
import os

my_secret = os.environ['katcordtoken']

rpsrock = [
    "Bots choice: Rock **Tie**", "Bots choice: Paper **You lose**",
    "Bots choice: Scissors **You win**"
]
rpspaper = [
    "Bots choice: Rock **You win**", "Bots choice: Paper **Tie**",
    "Bots choice: Scissors **You lose**"
]
rpsscissors = [
    "Bots choice: Rock **You lose**", "Bots choice: Paper **You win**",
    "Bots choice: Scissors **Tie**"
]
greeting_list = [
    "hello", "hi", "good morning", "good afternoon", "good evening"
]
jokes = [
    "What do you call a rich elf? Welfy.",
    "When does it rain money? When there is 'change' in the weather.",
    "Did you hear about the restaurant on the moon? The food is good, but there's no atmosphere.",
    "How does the man in the moon cut his hair? Eclipse it.",
    "What’s faster, cold or hot? Hot, because you can catch a cold.",
    "Who is the world's greatest underwater secret agent? James Pond.",
    "Why wouldn't the crab share his sweets? Because he was a little shellfish!",
    "Why did the toilet paper roll down the hill? To get to the bottom.",
    "Why did the scientist wear denim? Because he was a jean-ius.",
    "What happens when cows refuse to be milked? Udder chaos.",
    "When is it bad luck to meet a black cat? When you’re a mouse."
]
coin = ["Heads", "Tails"]


def get_response(message: str) -> str:
    person_message = message.lower()


    if "!kat" == person_message:
        return "https://tenor.com/view/yippee-happy-yippee-creature-yippee-meme-yippee-gif-gif-1489386840712152603"

    if "!rickroll" == person_message:
        return "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

    if "!pedro" == person_message:
        return "[Pedro](https://www.youtube.com/watch?v=Pb-HDNUSqrE)"
        
    if "!whopper" == person_message:
        return "<:Whopper:1264047545156501587>"

    if "!moyai" == person_message:
        return "<:Moyai:1264931828742230036>"

    if "!server" == person_message:
        return "https://discord.gg/2FdrFw6XKU"

    if "!meow" == person_message:
        return "Meow!"

    if "!rps rock" == person_message:
        return random.choice(rpsrock)

    if "!rps paper" == person_message:
        return random.choice(rpspaper)

    if "!rps scissors" == person_message:
        return random.choice(rpsscissors)

    if "!add" == person_message:
        return "[Add the bot to a server](https://discord.com/oauth2/authorize?client_id=1258066583717286010&permissions=274877971520&integration_type=0&scope=bot)"

    if "!fact" == person_message:
        return "Cats have 9 lives."

    if "!coin" == person_message:
        return str(random.choice(coin))

    if "!joke" == person_message:
        return str(random.choice(jokes))

    if "!dice" == person_message:
        return str(random.randint(1, 6))

    if "!github" == person_message:
        return "[Github](https://github.com/BenjaminKat1234/Katcord) <:Github:1264228835449241621>"

    if "!nerd" == person_message:
        return "<:Nerd:1264681608330612766>"

    if "<@1258066583717286010>" == person_message:
        return "<:KatCord:1264055154139729960>"

    if "!commands" == person_message:
        return "```Commands:\n!add - Adds the bot to a server\n!dice - Rolls a dice\n!rps (Choice) - Play rock paper scissors\n!github - Sends a link to the katcord github\n!kat- Yippe\n!pedro - Pedro Pedro Pedro\n!moyai - moyai\n!meow - Meow\n!nerd - Erm.. actually\n!fact - Cats have 9 lives\n!whopper - Whopper Whopper\n!joke - Tells a joke\n!coin - Flips a coin\n!server - Sends a server invite link\n!commands - Shows a list of commands```"


async def send_message(message, user_message, is_private):
    try:
        response = get_response(user_message)
        await message.author.send(
            response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


TOKEN = my_secret
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)



@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    await client.change_presence(activity=discord.Game(name="!commands"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    if user_message[0] == '?':
        user_message = user_message[1:]
        await send_message(message, user_message, is_private=True)
    else:
        await send_message(message, user_message, is_private=False)


client.run(TOKEN)
