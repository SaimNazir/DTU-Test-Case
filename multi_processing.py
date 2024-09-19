import pandas as pd
import numpy as np
import datetime
import time
import multiprocessing as mp


x = datetime.datetime(1993, 12, 9, 0, 0)

simulated_dates = []

for i in range(2000000):
    x += datetime.timedelta(minutes=60)
    simulated_dates.append(x)

df = pd.DataFrame(simulated_dates, columns=['Dates'])

print(df.shape)


def add_hour(dates):
    return dates + pd.Timedelta(hours=1)

# Without multiprocessing
start_time = time.time()
df['Dates'] = df['Dates'].apply(add_hour)
end_time = time.time()

print("Without multiprocessing:", end_time - start_time, "seconds")



# With multiprocessing
def process_chunk(chunk):
    return add_hour(chunk)

start_time = time.time()
num_cores = mp.cpu_count()
chunk_size = len(df) // num_cores
chunks = [df['Dates'][i:i+chunk_size] for i in range(0, len(df), chunk_size)]

with mp.Pool(processes=num_cores) as pool:
    df['Dates'] = pd.concat(pool.map(process_chunk, chunks))
end_time = time.time()

print("With multiprocessing:", end_time - start_time, "seconds")
