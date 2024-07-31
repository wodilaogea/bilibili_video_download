import asyncio


async def run0():
    print("a")
    await asyncio.sleep(2)
    print("b")
async def run1():
    print("1")
    await asyncio.sleep(3)
    print("2")

async def main():
    # await run0()
    tasks=[asyncio.create_task(run0()),
           asyncio.create_task(run1())]
    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())

