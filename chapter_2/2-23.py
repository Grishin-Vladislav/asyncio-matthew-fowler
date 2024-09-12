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
	await t1

asyncio.run(main(), debug=True)