import asyncio
import datetime

async def gen_data(quantity: int, data: asyncio.Queue):
    print(f"[gen_data] Wait gen of data: {quantity}")
    for idx in range(1, quantity + 1):
        item = idx * idx
        await data.put((item, datetime.datetime.now())) # put() is async
        await asyncio.sleep(0.001)
        
    print(f"{quantity} data generated successfully")
    
async def process_data(quantity: int, data: asyncio.Queue):
    print(f"[process_data] Wait gen of data: {quantity}")
    processed = 0
    while processed < quantity:
        await data.get()
        processed += 1
        await asyncio.sleep(0.001)
        
    print(f"Were processed {quantity} items")

def main():
    total = 5_000
    data = asyncio.Queue()
    
    print(f"Computing {total * 2:.2f} data")
    
    el = asyncio.get_event_loop()
    
    task_1 = el.create_task(gen_data(total, data))
    task_2 = el.create_task(gen_data(total, data))
    task_3 = el.create_task(process_data(total * 2, data))
    
    tasks = asyncio.gather(task_1, task_2, task_3)
    
    el.run_until_complete(tasks) # Transform function in a Future
    el.close()
    

if __name__ == "__main__":
    main()