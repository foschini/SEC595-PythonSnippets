import asyncio
import random

async def random_sleep(counter):
    delay = random.random() * 5
    print(f"{counter} sleeps for {delay:.2f} seconds")
    await asyncio.sleep(delay)
    print(f"{counter} awakens")

async def five_sleepers():
    print("Creating five tasks")
    tasks = [
        asyncio.create_task(random_sleep(i)) for i in range(5)]
    print("Sleeping after starting five tasks")
    await asyncio.sleep(2)
    print("Waking and waiting for five tasks")
    await asyncio.wait(tasks)

async def main():
    await five_sleepers()

if __name__ == "__main__":
    asyncio.run(main())
    print("Done five tasks")