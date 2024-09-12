import asyncio
from asyncio.exceptions import TimeoutError

from delay import delay

async def main():
	task = asyncio.create_task(delay(10))
	shield = asyncio.shield(task)

	try:
		result = await asyncio.wait_for(shield, timeout=5)
		print(result)
	except TimeoutError:
		print('task is taking too long but it is shielded')
		result = await task
		print(result)

asyncio.run(main())