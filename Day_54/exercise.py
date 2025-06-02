import time


def speed_calc_decorator(func):
    # This decorator measures how long a function takes to run
    def wrapper(*args, **kwargs):
        # Record start time before function runs
        start_time = time.time()
        # Execute the original function and store its result
        result = func(*args, **kwargs)
        # Record end time after function completes
        end_time = time.time()
        # Calculate and print the execution time. func.__name__ gets the original function's name
        print(f"{func.__name__} run speed: {end_time - start_time}s")
        # Return the original function's result
        return result
    
    return wrapper


@speed_calc_decorator  # This function will be measured by the decorator
def fast_function():
    # Performs 1 million iterations of a simple calculation
    for i in range(1000000):
        i * i


@speed_calc_decorator  # This function will be measured by the decorator
def slow_function():
    # Performs 10 million iterations - should take about 10 times longer
    for i in range(10000000):
        i * i


# Run both functions to see the time difference
fast_function()
slow_function()