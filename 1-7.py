import time
import requests


def read_page() -> None:
    response = requests.get("https://google.com")
    print(response.status_code)


sync_start = time.time()

for i in range(15):
    read_page()

sync_end = time.time()

print(f"sync completion time - {sync_end - sync_start:.4f}s.")
