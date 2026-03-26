# from time import clock
import time

def timeModule(nos: int) -> float:
    print(nos)
    for n in range(nos):
        startTime = time.perf_counter()
        print(f"Iteration {n} started at {startTime}")
        time.sleep(2)
        endTime = time.perf_counter()-startTime
        print(f"Iteration {n} ended at {endTime}")
        
    return endTime
    
timeModule(10)    

