import asyncio
from chapter_2 import timer, delay

@timer.async_timed()
async def cpu_bound():
	counter = 0
	for _ in range(100_000_000):
		counter += 1
	return counter

@timer.async_timed()
async def main():
	t1 = asyncio.create_task(cpu_bound())
	t2 = asyncio.create_task(cpu_bound())
	delay_task = asyncio.create_task(delay.delay(4))
	await t1
	await t2
	await delay_task

asyncio.run(main())