import logging
import threading
import time

thread_list = [1, 2, 3, 4, 5]


def thread_function(name):
    logging.info("Thread %s: starting", name)
    logging.info("Thread %s: finishing", name)


def loop():
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

    print('Entire process has finished.')


loop()


def main():
    """Original code to create, start and end thread(s)."""
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(2,))
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    x.join()
    logging.info("Main    : all done")

# main()
