import asyncio

from utils.delay import delay
from utils.timer import async_timed

def call_later():
	print('i will be called soon!')

@async_timed()
async def main():
	loop = asyncio.get_running_loop()
	loop.call_soon(call_later)
	await delay(3)

asyncio.run(main())