#!/usr/bin/python3

import asyncio
import time
import random

# ANSI colors
c = (
    "\033[32m",
    "\033[36m",
    "\033[31m",
    "\033[34m",
    "\033[35m",
    "\033[93m",
    "\033[91m",
    "\033[96m",
)
eofc = "\033[0m"


async def say_after(delay: int, what: str):
    await asyncio.sleep(delay)
    print(random.choice(c) + what + eofc)


async def main():
    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'guys'))

    print(f"started at {time.strftime('%X')}")

    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())
