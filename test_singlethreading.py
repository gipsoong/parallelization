import logging
import threading
import time
from timeit import default_timer as timer
from datetime import timedelta

thread_list = [1, 2, 3, 4, 5]


def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(1)
    logging.info("Thread %s: finishing", name)


def loop():
    start = timer()

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    for i in thread_list:
        logging.info("Before creating thread")
        x = threading.Thread(target=thread_function, args=(i,))
        logging.info("Before running thread")
        x.start()
        logging.info("Wait for the thread to finish")
        x.join()
        logging.info(f"Thread {i} is finished.")

    end = timer()
    duration = (timedelta(seconds=end - start)).total_seconds()

    print(f'Entire process has finished in {duration} second(s).')


loop()
