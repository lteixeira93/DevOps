import asyncio

async def say_long_hi():
    print("Hi...")
    await asyncio.sleep(2)
    print("Everyone...")
    
el = asyncio.get_event_loop()
el.run_until_complete(say_long_hi()) # Transform function in a Future
el.close()