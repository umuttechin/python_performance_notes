"""
Asynchronous challenges
    Learning curve
    Debugging
    Compatibility

Learning curve
    New syntax: async and await
    New concepts: coroutine and event loop
    New libraries: aoihttp and aiomysql

Debugging
    Understand order of execution
    Understand state of application

Compatibility
    Third - party libraries
    Blocking code


--------------------------------

time python async_challenges.py       
Order complete.
Order complete.
Finished!
python3 async_challenges.py  0.04s user 0.02s system 5% cpu 1.078 total

--------------------------------

import asyncio
import time
async def process_order():
    await asyncio.sleep(1)
    time.sleep(3)
    print("Order complete.")


async def main():
    await asyncio.gather(process_order(), process_order())
    print("Finished!")

asyncio.run(main())

--------------------------------

time python async_challenges.py
Order complete.
Order complete.
Finished!
python3 async_challenges.py  0.06s user 0.02s system 1% cpu 7.152 total

--------------------------------

import asyncio
import time
async def process_order():
    #await asyncio.sleep(1)
    for _ in range(100_000_000):
        pass
    print("Order complete.")


async def main():
    await process_order()
    #await asyncio.gather(process_order(), process_order())
    print("Finished!")

asyncio.run(main())

--------------------------------

time python async_challenges.py
Order complete.
Finished!
python3 async_challenges.py  0.97s user 0.01s system 99% cpu 0.985 total

--------------------------------

import asyncio
import time
async def process_order():
    #await asyncio.sleep(1)
    for _ in range(100_000_000):
        pass
    print("Order complete.")


async def main():
    #await process_order()
    await asyncio.gather(process_order(), process_order())
    print("Finished!")

asyncio.run(main())

--------------------------------

time python async_challenges.py
Order complete.
Order complete.
Finished!
python3 async_challenges.py  1.90s user 0.02s system 97% cpu 1.965 total

"""

import asyncio
import time
async def process_order():
    #await asyncio.sleep(1)
    for _ in range(100_000_000):
        pass
    print("Order complete.")


async def main():
    #await process_order()
    await asyncio.gather(process_order(), process_order())
    print("Finished!")

asyncio.run(main())
