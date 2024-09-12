import asyncio
from asyncio.exceptions import TimeoutError

from utils.delay import delay

async def main():
	delay_task = asyncio.create_task(delay(2))
	try:
		result = await asyncio.wait_for(delay_task, timeout=1)
		print(result)
	except TimeoutError:
		print('time-out!')
		print(f'task cancelled - {delay_task.cancelled()}')

asyncio.run(main())
