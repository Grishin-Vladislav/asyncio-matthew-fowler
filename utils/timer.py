import functools
import time

from typing import Callable, Any

def async_timed():
	def wrapper(func: Callable) -> Callable:
		@functools.wraps(func)
		async def wrapped(*args, **kwargs) -> Any:

			print(f'{func} is called with args: {args} {kwargs}')
			start = time.time()

			try:
				return await func(*args, **kwargs)
			finally:
				total = time.time() - start
				print(f'{func} is over in {total:.4f} sec.')
		
		return wrapped

	return wrapper