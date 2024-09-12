import asyncio
from delay import delay

async def main() -> None:
	t1 = asyncio.create_task(delay(3))
	t2 = asyncio.create_task(delay(3))
	t3 = asyncio.create_task(delay(3))

	await t1
	await t2
	await t3
	print('three seconds has passed')

if __name__ == '__main__':
	asyncio.run(main())