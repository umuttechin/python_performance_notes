"""
Asynchronous
    Inspired from the other languages
    Reduce potential for bugs
    Maximize core utilization
    New syntax, concepts and tools

Asynchronous
    Low overhead(no switching between threads, happens in inly main thread)
    Low potential for bugs
    Learning curve
    Compatibility constraints

Threads
    High overhead
    High potential for bugs
    Simple syntax
    High compatibility

"""

import asyncio

async def process_order():
    await asyncio.sleep(1)
    print("Order complete.")


async def main():
    await process_order()
    await process_order()
    print("Finished!")

asyncio.run(main())