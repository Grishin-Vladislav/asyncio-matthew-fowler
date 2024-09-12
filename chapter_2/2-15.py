import asyncio
from asyncio import Future

async def set_future_value(future: Future, value: int) -> None:
	await asyncio.sleep(2)
	future.set_result(value)

def make_request() -> Future:
	future = Future()
	asyncio.create_task(set_future_value(future, 15))
	return future

async def main():
	future = make_request()
	print(f'future is ready - {future.done()}')
	await future
	print(f'future is ready - {future.done()}')

asyncio.run(main())
