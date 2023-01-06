import json
import logging
# instead of that module, you can use a custom logger.py file I added in the main folder
# from logger import log

import coloredlogs
from hereby import Here

from models.cog import CommandCog
from models.client import BachelorOverTelecom

if __name__ == "__main__":
    here = Here(__file__)

    coloredlogs.install()
    logging.basicConfig(
        level=logging.INFO,
    )

    with open(here.abspath(".env.json")) as key:
        ENVIRONMENT = json.load(key)
        API_KEY = ENVIRONMENT.get("API_KEY", None)

    if API_KEY is None:
        logging.error("No API key found ! quitting")
    else:
        client = BachelorOverTelecom.get_instance()
        client.add_cog(CommandCog(ENVIRONMENT=ENVIRONMENT))
        # log("start", f"{client.user.name} is ready!")  # example usage of the logger.py :)
        logging.info(f"Starting application with env vars: {', '.join(ENVIRONMENT.keys())}")
        client.run(API_KEY)
