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