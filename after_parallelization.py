import logging
from timeit import default_timer as timer
from datetime import timedelta
import urllib.request
import concurrent.futures
from data import *

def download(images):
    file_name = images['name']
    full_path = 'images/' + file_name + '.jpg'
    urllib.request.urlretrieve(images['url'], full_path)


if __name__ == '__main__':
    start = timer()

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        executor.map(download, images)

    end = timer()
    duration = (timedelta(seconds=end - start)).total_seconds()

    print(f'Entire process has finished in {duration} second(s).')
