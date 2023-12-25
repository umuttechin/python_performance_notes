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

--------------------------------

kernprof -lv async_when.py
Wrote profile results to async_when.py.lprof
Timer unit: 1e-06 s

Total time: 2.50919 s
File: async_when.py
Function: main at line 40

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    40                                           @profile
    41                                           def main():
    42         1    1987187.0    2e+06     79.2      synchronous()
    43         1     522003.0 522003.0     20.8      asyncio.run(asynchronous())

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
