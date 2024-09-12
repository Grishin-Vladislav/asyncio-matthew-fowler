import asyncio
from chapter_2.timer import async_timed

@async_timed()
async def cpu_bound() -> int:
	counter = 0
	for _ in range(100_000_000):
		counter += 1
	return counter

@async_timed()
async def main():
	t1 = asyncio.create_task(cpu_bound())
	t2 = asyncio.create_task(cpu_bound())

	await t1
	await t2

asyncio.run(main())