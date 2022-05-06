from ast import Name
import asyncio
import logging
from unicodedata import name

import aiohttp
import pyxivapi
import os
from dotenv import load_dotenv
from pyxivapi.models import Filter, Sort


load_dotenv()
FF_KEY = os.getenv("PRIVATE_KEY")
CLIENT = pyxivapi.XIVAPIClient(api_key=FF_KEY)




async def fetch_example_results():

    # Search Lodestone for a character
    character = await CLIENT.character_search(
        world="exodus", 
        forename="Dorrai", 
        surname="Stark"
    )

    # await client.session.close()
    """
    add parsing func later
    """
    return character['Results'][0]['Name']

"""
executed when file is run directly
"""
# if __name__ == '__main__':
#     logging.basicConfig(level=logging.INFO, format='%(message)s', datefmt='%H:%M')
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(fetch_example_results())



