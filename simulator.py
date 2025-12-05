import time
import random
import requests

URL = "http://127.0.0.1:5001/update"

while True:
    # 0 se 100 ke beech random fill level
    fill = random.randint(0, 100)
    try:
        r = requests.post(URL, json={"fill": fill})
        print("Sent:", fill, "Server replied:", r.text)
    except Exception as e:
        print("Error:", e)

    time.sleep(3)  # har 3 second baad naya value bhejo
