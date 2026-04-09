import logging
import functools
import time

# Step - 1: Configure logging

logging.basicConfig(level = logging.DEBUG,
                    format = '%(asctime)s - %(levelname)s - %(message)s',
                    datefmt= '%Y-%m-%d %H:%M:%S'
                    )

# Step - 2: Create the instance of logger

logger = logging.getLogger(__name__)



# Step - 3: Create decorator to run function and log the message

def log_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.debug(f"Executing function '{func.__name__}' with args '{args} and key-word arguments {kwargs}")
        logger.info(f"Function '{func.__name__} execution started")
        start_time = time.perf_counter()
        try:
            result = func(*args, **kwargs)
            execution_time = time.perf_counter() - start_time
            logger.info(f"Executing ended '{func.__name__}' successfully!!!! Time taken {execution_time:.4f}.s")
            logger.debug(f"Function '{func.__name__}' ended and returned results: {result}")
            return result
        except Exception as e:
            logger.exception(f"Error occured in '{func.__name__}' and error is {str(e)} ")
    return wrapper


# 4. Apply the decorator to your functions

@log_execution
def process_data(data_id, scale_factor=1.0):
    """Simulates processing some data successfully."""
    time.sleep(0.2)  # Simulate work
    return data_id * scale_factor

@log_execution
def fetch_user_record(user_id):
    """Simulates a function that crashes."""
    # Simulating a crash by dividing by zero
    return user_id / 0 

# if __name__ == '__main__':
#     print("--- Testing Successful Execution ---")
#     process_data(100, scale_factor=2.5)
    
#     print("\n--- Testing Failed Execution ---")
#     try:
#         fetch_user_record(55)
#     except ZeroDivisionError:
#         print("(Error caught in main block)")


def logger_(func):
    def wrapper(*args, **kwargs):
        print("Before execution", func.__name__, "args: ", args )
        result = func(*args, **kwargs)        
        print("After Execution")
        return result 
    return wrapper


@logger_
def sum(a, b):
    return a + b


# result = sum(2,3)
# print(result)

def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

strs = ["flower", "flow", "flight"]
res = longest_common_prefix(strs)
print(res)