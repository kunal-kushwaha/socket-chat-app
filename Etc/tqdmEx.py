from tqdm import tqdm
import time

a = [1,3,2,4,5]
for i in tqdm(a):
    time.sleep(1)
    print(i)
