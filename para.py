from concurrent.futures import ProcessPoolExecutor as ppe
from concurrent.futures import ThreadPoolExecutor as tpe
from concurrent.futures import as_completed as comp


def by_thread(func, items, callback, workers):
    with tpe(max_workers=workers) as executor:
        futures = (executor.submit(func, item) for item in items)
        for future in comp(futures):
            callback(future.result())


def by_process(func, items, callback, workers):
    with ppe(max_workers=workers) as executor:
        futures = (executor.submit(func, item) for item in items)
        for future in comp(futures):
            callback(future.result())
