import time
import threading
import requests


def make_request() -> None:
    response = requests.get("https://google.com")
    print(response.status_code)


threads = [threading.Thread(target=make_request) for i in range(15)]

start_time = time.time()

for thread in threads:
    thread.start()

print("all threads are working")

for thread in threads:
    thread.join()

end_time = time.time()

print(f"multithreading completion time - {end_time - start_time:.4f}s.")
