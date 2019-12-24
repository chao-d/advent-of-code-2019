import sys
import requests

url = "https://adventofcode.com/2019/day/" + sys.argv[1] + "/input"

with open("session_secret", "r") as f:
    session_id = f.readline().rstrip()

cookies = {"session": session_id}

r = requests.get(url, cookies=cookies)
file_name = "day" + sys.argv[1] + "input"

with open(file_name, "wb") as f:
    f.write(r.content)
