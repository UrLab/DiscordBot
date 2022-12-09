
import logging

from discord.ext import commands
from discord.ext.commands import Context

logger = logging.getLogger(__name__)


class CommandCog(commands.Cog):
    def __init__(self, ENVIRONMENT: list = None):
        self.ENVIRONMENT = ENVIRONMENT

    @commands.command()
    async def ping(self, ctx: Context):
        """
        Replies with pong
        """
        logger.info(f"Received command ping from {ctx.author}")
        await ctx.send("pong")
        logger.info("Replied with pong")
