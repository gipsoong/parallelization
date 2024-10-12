import logging
import threading
import time
from timeit import default_timer as timer
from datetime import timedelta
import urllib.request
from data import *

list_of_images = images
list_of_videos = videos


def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(1)
    logging.info("Thread %s: finishing", name)


def download_images(image, file_name):
    full_path = 'images/' + file_name + '.jpg'
    urllib.request.urlretrieve(image, full_path)


def download_videos(video, file_name):
    full_path = 'videos/' + file_name + '.webm'
    urllib.request.urlretrieve(video, full_path)


def download_video_single_threaded():
    start = timer()

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    counter = 1

    for i in list_of_videos:
        file_name = i.split('/')[-1]

        logging.info("Before creating thread")
        thread = threading.Thread(target=download_videos, args=(i, file_name))
        logging.info("Before running thread")
        thread.start()
        logging.info("Wait for the thread to finish")
        thread.join()
        logging.info(f"Thread {counter} is finished.")

        counter += 1

    end = timer()
    duration = (timedelta(seconds=end - start)).total_seconds()

    print(f'Entire process has finished in {duration} second(s).')


def image():
    start = timer()

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    counter = 1

    for i in list_of_images:
        file_name = i.split('/')[-1]

        logging.info("Before creating thread")
        thread = threading.Thread(target=download_images, args=(i, file_name))
        logging.info("Before running thread")
        thread.start()
        logging.info("Wait for the thread to finish")
        thread.join()
        logging.info(f"Thread {counter} is finished.")

        counter += 1

    end = timer()
    duration = (timedelta(seconds=end - start)).total_seconds()

    print(f'Entire process has finished in {duration} second(s).')


download_video_single_threaded()
