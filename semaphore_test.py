import asyncio


async def myWorker(semaphore):
    await semaphore.acquire()
    print("Successfully acquire the semaphore!")
    await asyncio.sleep(3)
    print("Releasing semaphore...")
    semaphore.release()
    
async def main():
    mySemaphore = asyncio.BoundedSemaphore(value=4)
    await asyncio.wait([myWorker(mySemaphore), 
                        myWorker(mySemaphore), 
                        myWorker(mySemaphore), 
                        myWorker(mySemaphore), 
                        myWorker(mySemaphore)])
    print("Finished all Workers!!")
    
    
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
print("Our loop has completed")
loop.close()
