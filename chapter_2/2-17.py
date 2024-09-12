import asyncio

from utils.timer import async_timed
from utils.delay import delay

@async_timed()
async def main():
	t1 = asyncio.create_task(delay(2))
	t2 = asyncio.create_task(delay(3))

	await t1
	await t2

asyncio.run(main())