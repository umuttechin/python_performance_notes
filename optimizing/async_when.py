"""
Use Asynchronizations
    I/O operations
    Many small tasks(better than multithreading, because it does not have switching overhead between thread)
    Avoid synchronizing threads
    Asynchronous dependencies
    Data processing pipelines
    Networking applications

Do Not Use Asynchronizations
    CPU - extensive tasks
    Blocking code
    Blocking dependencies

"""

import threading
from time import sleep
from urllib import request
import asyncio
import aiohttp

def download():
    return request.urlopen("https://google.com").read()


async def async_download(session, url):
    async with session.get(url) as response:
        return await response.text()

def synchronous():
    for _ in range(5):
        download()

async  def asynchronous():
    async with aiohttp.ClientSession() as session:
        coroutines = [async_download(session, "https://google.com") for _ in range(5)]
        await asyncio.gather(*coroutines)

@profile
def main():
    synchronous()
    asyncio.run(asynchronous())

main()