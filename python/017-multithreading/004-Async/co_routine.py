import asyncio

async def say_hi():
    print("Hi...")
    
el = asyncio.get_event_loop()
el.run_until_complete(say_hi())
el.close()