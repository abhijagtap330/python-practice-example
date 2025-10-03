import time
from concurrent.futures import ProcessPoolExecutor

# Function to calculate sum of squares sequentially
def sum_of_squares_sequential(numbers):
    return sum(x**2 for x in numbers)

# Function to calculate sum of squares for a subset of numbers (used in parallel approach)
def sum_of_squares_sublist(numbers):
    return sum(x**2 for x in numbers)

# Sequential approach to calculate the sum of squares
def sequential_sum_of_squares():
    numbers = list(range(1, 150001))  # List of numbers from 1 to 10000
    start_time = time.time()  # Record start time
    result = sum_of_squares_sequential(numbers)
    end_time = time.time()  # Record end time
    print(f"Sequential Result: {result}")
    print(f"Sequential Execution Time: {end_time - start_time:.6f} seconds")

# Parallel approach to calculate the sum of squares using ProcessPoolExecutor
def parallel_sum_of_squares():
    numbers = list(range(1, 150001))  # List of numbers from 1 to 10000
    # Split the list into chunks for parallel processing
    chunk_size = len(numbers) // 4  # Using 4 processes
    chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]
    
    start_time = time.time()  # Record start time
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(sum_of_squares_sublist, chunks))
    
    # Sum the results from all processes
    result = sum(results)
    end_time = time.time()  # Record end time
    
    print(f"Parallel Result: {result}")
    print(f"Parallel Execution Time: {end_time - start_time:.6f} seconds")

# Run and compare both approaches
def compare_approaches():
    sequential_sum_of_squares()  # Calculate sequential sum of squares
    parallel_sum_of_squares()  # Calculate parallel sum of squares

if __name__ == "__main__":
    compare_approaches()
    
    
# start_time = time.time()
# sqaure = 0
# total = 0

# for i in range(10000):
#     sqaure = i**2
#     total += sqaure
# print(total)
# end_time = time.time()

# excuation_time = end_time - start_time 
# print(excuation_time)
