import threading
import time

counter = 0

lock_counter = threading.Lock()


def n_thread():
    global counter
    for _ in range(1000000):
        with lock_counter:
            local_counter = counter
            local_counter += 1
            counter = local_counter
        # local_counter = counter
        # local_counter += 1
        # counter = local_counter


def m_thread():
    global counter
    for _ in range(1000000):
        with lock_counter:
            local_counter = counter
            local_counter -= 1
            counter = local_counter
        # local_counter = counter
        # local_counter -= 1
        # counter = local_counter


def run_threads(n, m):
    start_time = time.time()

    threads = []

    for _ in range(n):
        thread = threading.Thread(target=n_thread)
        threads.append(thread)
        thread.start()

    for _ in range(m):
        thread = threading.Thread(target=m_thread)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()

    print(f"Значение счетчика: {counter}")
    print(f"Время выполнения: {end_time - start_time} сек.")


n = 2
m = 2
run_threads(n, m)
