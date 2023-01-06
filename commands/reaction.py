import nextcord
from DiscordBot.logger import log
from DiscordBot.commands.reactions import emoji  # yuck

commands = {
    "emoji": emoji.emoji
}


async def reaction(message: nextcord.Message, client):
    log("command", f"(ur prefix) {message.guild.name}")
    reaction_type = message.content.split()[3]  # modify based on your prefix

    if reaction_type in commands:
        await commands[reaction_type](message, client)
    else:
        return
