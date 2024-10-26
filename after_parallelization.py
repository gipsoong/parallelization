import logging
from timeit import default_timer as timer
from datetime import timedelta
import urllib.request
import requests
import concurrent.futures
from data import *
import zipfile


def download_images(item):
    # Code to send a response so the program does not get hit with a limit
    url = item
    headers = {'User-Agent': 'Media Downloader (for a school project) (https://github.com/gipsoong/parallelization)'}
    response = requests.get(url, headers=headers)

    file_name = item.split('/')[-1]
    full_path = 'images/' + file_name + '.jpg'
    urllib.request.urlretrieve(item, full_path)


def download_videos(item):
    # Code to send a response so the program does not get hit with a limit
    url = item
    headers = {'User-Agent': 'Media Downloader (for a school project) (https://github.com/gipsoong/parallelization)'}
    response = requests.get(url, headers=headers)

    file_name = item.split('/')[-1]
    full_path = 'videos/' + file_name + '.mp4'
    urllib.request.urlretrieve(item, full_path)


def multi_threaded_download(items, file_format, cores):
    start = timer()

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    if file_format == '.jpg':
        with concurrent.futures.ThreadPoolExecutor(max_workers=cores) as executor:
            executor.map(download_images, items)
    else:
        with concurrent.futures.ThreadPoolExecutor(max_workers=cores) as executor:
            executor.map(download_videos, items)

    end = timer()
    duration = (timedelta(seconds=end - start)).total_seconds()

    print(f'Entire process has finished in {duration} second(s).')


def zip_files(items):
    with zipfile.ZipFile("videos.zip", mode="w") as archive:
        archive.write(items)


def multi_threaded_zip(items, cores):
    start = timer()

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    with concurrent.futures.ThreadPoolExecutor(max_workers=cores) as executor:
        executor.map(zip_files, items)

    end = timer()
    duration = (timedelta(seconds=end - start)).total_seconds()

    print(f'Entire process has finished in {duration} second(s).')
