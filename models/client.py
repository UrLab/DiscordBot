import logging

import discord
from discord.ext import commands
from discord_slash import SlashCommand


class BachelorOverTelecom(commands.Bot):
    """BachelorOverTelecom's client"""

    instance = None

    @staticmethod
    def get_instance():
        """Singleton Pattern"""
        if BachelorOverTelecom.instance is None:
            BachelorOverTelecom()
        return BachelorOverTelecom.instance

    def __init__(self):
        if BachelorOverTelecom.instance is not None:
            raise RuntimeError(f"Trying to instanciate a second object of {__class__}")
        BachelorOverTelecom.instance = self

        intents = discord.Intents.default()
        intents.members = True
        intents.presences = True
        intents.reactions = True

        super().__init__(command_prefix="$", intents=intents)

        self.slash = SlashCommand(self, sync_commands=True)

    async def on_ready(self):
        """This is called when the connection to disord's API is established"""
        logging.info(f"Logged on as {self.user}!")
        await self.change_presence(
            status=discord.Status.idle,
            activity=discord.Game("Hiding students in the basement")  # Thanks Copilot
        )
