import asyncio
import time

# The 'async' keyword tells Python this function can be paused
async def simulated_api_call(request_id: int):
    print(f"Started API call {request_id}...")
    
    # 'await' is the magic word. It pauses this specific function 
    # and lets Python do other things while we wait for the 2 seconds.
    await asyncio.sleep(2) 
    
    print(f"Finished API call {request_id}!")
    return f"Result {request_id}"

async def main():
    start_time = time.time()
    
    print("Initiating 3 concurrent API calls...")
    
    # asyncio.gather fires off all 3 functions at the exact same time
    results = await asyncio.gather(
        simulated_api_call(1),
        simulated_api_call(2),
        simulated_api_call(3)
    )
    
    end_time = time.time()
    print(f"\nAll results: {results}")
    print(f"Total time taken: {end_time - start_time:.2f} seconds")

# This is the standard way to kick off an async Python script
if __name__ == "__main__":
    asyncio.run(main())