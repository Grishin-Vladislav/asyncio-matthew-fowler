import os
import threading

print(f"current process with id:{os.getpid()}")

total_threads = threading.active_count()
thread_name = threading.current_thread().name

print(f"threads count: {total_threads}")
print(f"current_thread: {thread_name}")
