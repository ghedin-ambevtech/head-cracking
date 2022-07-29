import asyncio
from time import sleep


async def main():
    task = asyncio.create_task(other_function())
    print("A")
    # await other_function()
    await asyncio.sleep(3)
    print("B")
    await task


async def other_function():
    print("1")
    await asyncio.sleep(2)
    print("2")


asyncio.run(main())
