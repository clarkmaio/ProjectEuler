
import timeit

def avg_run_time(function, args, N: int) -> float:
    avg_time = timeit.timeit(lambda: function(*args), number=N) / N
    print(f'Execution time brute force: {avg_time}')
    return avg_time
