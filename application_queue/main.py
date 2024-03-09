from queue import Queue
import time
import random

requests_queue = Queue()

def generate_request():
    request_id = random.randint(1, 10000)
    print(f"Generating of application with ID: {request_id}")
    requests_queue.put(request_id)

def process_request():
    if not requests_queue.empty():
        request_id = requests_queue.get()
        print(f"Processing of application with ID: {request_id}")
        time.sleep(1)  
    else:
        print("Queue is empty.")

def main():
    for _ in range(5): 
        generate_request()
        time.sleep(2) 
        process_request()

if __name__ == "__main__":
    main()