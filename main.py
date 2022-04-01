import datetime
import time
from functools import wraps


def time_wrapper(func):
    """
    Prints time of processing the function
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        output = func(*args, **kwargs)
        dt = time.time() - start
        print(f"---> Execution of function {func.__name__}: {dt} secs")
        return output
    return wrapper


def log_wrapper(filepath):
    """
    Logs data about running the function
    """
    def outer_wrapper(func):
        def inner_wrapper(*args, **kwargs):
            with open(filepath, 'a') as f:
                time_format = "%Y/%m/%d %H:%M"
                f.write(f"Function {func.__name__} launched at {datetime.datetime.now().strftime(time_format)}.\n")
                ret = func(*args, **kwargs)
                f.write(f"Function {func.__name__} finished at {datetime.datetime.now().strftime(time_format)} with result {ret}.\n\n")
            return ret
        return inner_wrapper
    return outer_wrapper


@log_wrapper(r"C:\Users\User\PycharmProjects\wrappers\logger.txt")
@time_wrapper
def pos_sum_calculator(l):
    """
    Calculates sum of positive values from the list
    """
    return sum([el for el in l if el > 0])


result = pos_sum_calculator(list(range(-1000000, 1000000, 1)))