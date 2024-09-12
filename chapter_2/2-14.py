from asyncio import Future


future = Future()

print(f'future is ready - {future.done()}')

future.set_result(42)

print(f'future is ready - {future.done()}')

print(f'future result - {future.result()}')
