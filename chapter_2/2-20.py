import asyncio
import requests
from chapter_2.timer import async_timed

@async_timed()
async def make_request() -> int:
	return requests.get('https://google.com').status_code

@async_timed()
async def main():
	t1 = asyncio.create_task(make_request())
	t2 = asyncio.create_task(make_request())
	t3 = asyncio.create_task(make_request())
	await t1
	await t2
	await t3

asyncio.run(main())