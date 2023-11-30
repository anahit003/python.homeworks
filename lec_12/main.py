import random
import time
with open('Numbers.txt', 'w') as file:
    for _ in range(100):
        numbers = [str(random.randint(1, 1000)) for _ in range(20)]
        file.write(' '.join(numbers) + '\n')

with open('Numbers.txt', 'r') as file:
    lines = file.readlines()

result = list(map(lambda line: list(map(int, line.split())), lines))

print("map to int : ",result)
print("------------------------------------")

filtered_result = list(map(lambda line: list(filter(lambda num: num > 40, line)), result))

print("filter numbers>40 : ",filtered_result)
print("------------------------------------")

with open('Numbers.txt', 'w') as file:
    for line in filtered_result:
        file.write(' '.join(map(str, line)) + '\n')

print("Filtered data has been written to 'Numbers.txt'.\n")

print("------------------------------------")

def read_file_generator(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            yield list(map(int, line.split()))


file_name = 'Numbers.txt'
generator = read_file_generator(file_name)


for line in generator:
    print(line)

print("------------------------------------")

def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} took {execution_time:.4f} seconds to execute.")
        return result
    return wrapper


@measure_execution_time
def example_function():
    time.sleep(2)
    print("Function executed.")

example_function() 
