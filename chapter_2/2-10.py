import asyncio
from utils.delay import delay

async def hello() -> None:
	for i in range(2):
		await asyncio.sleep(1)
		print('hello world')

async def main() -> None:
	t1 = asyncio.create_task(delay(3))
	t2 = asyncio.create_task(delay(3))

	await hello()
	await t1
	await t2
	print('end of programm')

if __name__ == '__main__':
	asyncio.run(main())