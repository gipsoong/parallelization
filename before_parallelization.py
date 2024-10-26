import logging
import threading
import time
import requests
import urllib.request
from timeit import default_timer as timer
from datetime import timedelta
from data import *
import zipfile

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(1)
    logging.info("Thread %s: finishing", name)


def download(item, file_name, directory, file_format):
    # Code to send a response so the program does not get hit with a limit
    url = item
    headers = {'User-Agent': 'Media Downloader (for a school project) (https://github.com/gipsoong/parallelization)'}
    response = requests.get(url, headers=headers)

    full_path = directory + file_name + file_format
    urllib.request.urlretrieve(item, full_path)


def single_threaded_download(items, file_format):
    start = timer()

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    counter = 1

    for i in items:
        directory = ''
        if file_format == '.jpg':
            directory = 'images/'
        else:
            directory = 'videos/'

        file_name = i.split('/')[-1]

        logging.info("Before creating thread")
        thread = threading.Thread(target=download, args=(i, file_name, directory, file_format))
        logging.info("Before running thread")
        thread.start()
        logging.info("Wait for the thread to finish")
        thread.join()
        logging.info(f"Thread {counter} is finished.")

        counter += 1

    end = timer()
    duration = (timedelta(seconds=end - start)).total_seconds()

    print(f'Entire process has finished in {duration} second(s).')


def single_threaded_zip(items):
    start = timer()

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    with zipfile.ZipFile("videos.zip", mode="w") as archive:
        for filename in items:
            archive.write(filename)

    end = timer()
    duration = (timedelta(seconds=end - start)).total_seconds()

    print(f'Entire process has finished in {duration} second(s).')