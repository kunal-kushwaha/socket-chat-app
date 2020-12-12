import requests
import math
from tqdm import tqdm
url = 'http://www.africau.edu/images/default/sample.pdf'
r = requests.get(url, stream=True)
CHUNK_SIZE = 256
total = math.ceil(int(r.headers['Content-Length']) / CHUNK_SIZE)

with open("file.pdf", "wb") as file:
    for chunk in tqdm(r.iter_content(CHUNK_SIZE), total=total):
        file.write(chunk)
