import asyncio
from chapter_2.timer import async_timed

@async_timed()
async def delay(delay: int) -> int:
	print(f'starting delay for {delay} seconds')
	await asyncio.sleep(delay)
	print(f'delay for {delay} seconds is over')
	return delay