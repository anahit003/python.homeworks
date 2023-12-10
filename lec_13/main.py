import time
import threading
from multiprocessing import Process, Manager

def count_words(filename):
    word_frequency = {}
    with open(filename, 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                word_frequency[word] = word_frequency.get(word, 0) + 1
    return word_frequency

def count_words_multithread(filename, number_of_threads):
    word_frequency = {}
    lock = threading.Lock()

    def chunk_of_process(chunk):
        local_frequency = {}
        for line in chunk:
            words = line.strip().split()
            for word in words:
                local_frequency[word] = local_frequency.get(word, 0) + 1

        with lock:
            for word, count in local_frequency.items():
                word_frequency[word] = word_frequency.get(word, 0) + count

    with open(filename, 'r') as file:
        lines = file.readlines()

    chunk_size = len(lines) // num_threads
    threads = []

    for i in range(number_of_threads):
        start = i * chunk_size
        end = start + chunk_size if i < number_of_threads - 1 else len(lines)
        chunk = lines[start:end]

        thread = threading.Thread(target=chunk_of_process, args=(chunk,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return word_frequency

def count_words_multiprocess(filename, number_of_processes):
    word_frequency = Manager().dict()

    def chunk_of_process(chunk, result_dictionry):
        local_frequency = {}
        for line in chunk:
            words = line.strip().split()
            for word in words:
                local_frequency[word] = local_frequency.get(word, 0) + 1

        for word, count in local_frequency.items():
            result_dictionary[word] = result_dictionary.get(word, 0) + count

    with open(filename, 'r') as file:
        lines = file.readlines()

    chunk_size = len(lines) // num_processes
    processes = []

    for i in range(number_of_processes):
        start = i * chunk_size
        end = start + chunk_size if i < number_of_processes - 1 else len(lines)
        chunk = lines[start:end]

        process = Process(target=process_chunk, args=(chunk, word_freq))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    return dict(word_frequency)

def measure_execution_time(function, *args):
    start = time.time()
    result = function(*args)
    end= time.time()
    execution = end - start
    return result, execution

def main(filename, number_of_threads, number_of_processes):
    sequential_result, sequential_time = measure_execution_time(count_words, filename)

    multithreading_result, multithreading_time = measure_execution_time(count_words_multithread, filename, num_threads)

    multiprocessing_result, multiprocessing_time = measure_execution_time(count_words_multiprocess, filename, num_processes)

    print("\nSequential Result:")
    print(sequential_result)
    print(f"Sequential Execution Time: {sequential_time:.4f} seconds")

    print("\nMultithreading Result:")
    print(multithreading_result)
    print(f"Multithreading Execution Time: {multithreading_time:.4f} seconds")

    print("\nMultiprocessing Result:")
    print(multiprocessing_result)
    print(f"Multiprocessing Execution Time: {multiprocessing_time:.4f} seconds")

    multithreading_speedup = sequential_time / multithreading_time
    multiprocessing_speedup = sequential_time / multiprocessing_time

    print(f"\nMultithreading Speedup: {multithreading_speedup:.4f}x")
    print(f"Multiprocessing Speedup: {multiprocessing_speedup:.4f}x")

main("lec_13/text.txt", 4, 4)