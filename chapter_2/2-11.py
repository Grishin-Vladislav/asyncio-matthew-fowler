import asyncio
from asyncio import CancelledError
from delay import delay

async def main() -> None:
	long_task = asyncio.create_task(delay(100))

	time_elapsed = 0

	while not long_task.done():
		print('task is not over, next check in 1 second')
		await asyncio.sleep(1)
		time_elapsed += 1
		if time_elapsed == 5:
			long_task.cancel()

	try:
		await long_task
	except CancelledError:
		print('task is taking too long, cancelling...')

asyncio.run(main())