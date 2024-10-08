import logging
import threading
import time
from timeit import default_timer as timer
from datetime import timedelta
import urllib.request

images = [
    {'name': 'image_1', 'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/A-Cat.jpg/2560px-A-Cat.jpg'},
    {'name': 'image_2',
     'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Cat_img.jpg/1280px-Cat_img.jpg'},
    {'name': 'image_3',
     'url': 'https://images.squarespace-cdn.com/content/v1/5452d441e4b0c188b51fef1a/1615326541809-TW01PVTOJ4PXQUXVRLHI/male-orange-tabby-cat.jpg'},
]

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(1)
    logging.info("Thread %s: finishing", name)

def download_images(url, file_name, file_path):
    full_path = 'images/' + file_name + '.jpg'
    urllib.request.urlretrieve(url, full_path)

if __name__ == '__main__':
    start = timer()

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    for i in images:
        url = i['url']
        file_name = i['name']
        file_path = 'images/'
        thread = threading.Thread(target=download_images, args=(url, file_name, file_path))
        thread.start()
        thread.join()

    end = timer()
    duration = (timedelta(seconds=end - start)).total_seconds()

    print(f'Entire process has finished in {duration} second(s).')
