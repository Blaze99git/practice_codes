'''
10. Exponential Backoff
Problem: Implement an exponential backoff strategy that doubles the wait time between retries, 
starting from 1 second, but stops after 5 retries.
'''
import time
max_retries = 5
wait_time = 1  # initial wait time in seconds
for attempt in range(1, max_retries + 1):
    print(f"Attempt {attempt}: Waiting for {wait_time} seconds before retrying...")
    time.sleep(wait_time)
    wait_time *= 2  # double the wait time for the next attempt
print("Max retries reached. Stopping attempts.")