import aiohttp
from dataclasses import dataclass


@dataclass
class Parameters:

    url: str
    crypto_symbol: str
    headers: dict
    url_symbols: str


api_key = "API_KEY"

parameters = Parameters(
    url="https://api.api-ninjas.com/v1/cryptoprice?symbol={}",
    headers= {
        "X-Api-Key": "API_KEY",
    },
    url_symbols = 'https://api.api-ninjas.com/v1/cryptosymbols'
)

async def get_crypto_symbols():
    async with aiohttp.ClientSession(headers=parameters.headers) as session:
        async with session.get(parameters.url_symbols) as response:
            if (response.status == 200):
                symbols = await response.json()
                return symbols
    return None


async def get_data(sybmol):
    async with aiohttp.ClientSession(headers=parameters.headers) as session:
        url = parameters.url.format(sybmol)
        async with session.get(url) as response:
            if (response.status == 200):
                data = await response.json()
                return data 
    return None
