import logging
from timeit import default_timer as timer
from datetime import timedelta
import urllib.request
import concurrent.futures

images = [
    {'name': 'image_1', 'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/A-Cat.jpg/2560px-A-Cat.jpg'},
    {'name': 'image_2',
     'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Cat_img.jpg/1280px-Cat_img.jpg'},
    {'name': 'image_3',
     'url': 'https://images.squarespace-cdn.com/content/v1/5452d441e4b0c188b51fef1a/1615326541809'
            '-TW01PVTOJ4PXQUXVRLHI/male-orange-tabby-cat.jpg'},
    {'name': 'image_4',
     'url': 'https://images.squarespace-cdn.com/content/v1/5452d441e4b0c188b51fef1a/1615326541809'
            '-TW01PVTOJ4PXQUXVRLHI/male-orange-tabby-cat.jpg'},
    {'name': 'image_5',
     'url': 'https://images.squarespace-cdn.com/content/v1/5452d441e4b0c188b51fef1a/1615326541809'
            '-TW01PVTOJ4PXQUXVRLHI/male-orange-tabby-cat.jpg'},
    {'name': 'image_6',
     'url': 'https://images.squarespace-cdn.com/content/v1/5452d441e4b0c188b51fef1a/1615326541809'
            '-TW01PVTOJ4PXQUXVRLHI/male-orange-tabby-cat.jpg'},
    {'name': 'image_7',
     'url': 'https://images.squarespace-cdn.com/content/v1/5452d441e4b0c188b51fef1a/1615326541809'
            '-TW01PVTOJ4PXQUXVRLHI/male-orange-tabby-cat.jpg'},
    {'name': 'image_8',
     'url': 'https://images.squarespace-cdn.com/content/v1/5452d441e4b0c188b51fef1a/1615326541809'
            '-TW01PVTOJ4PXQUXVRLHI/male-orange-tabby-cat.jpg'},
    {'name': 'image_9',
     'url': 'https://images.squarespace-cdn.com/content/v1/5452d441e4b0c188b51fef1a/1615326541809'
            '-TW01PVTOJ4PXQUXVRLHI/male-orange-tabby-cat.jpg'},
    {'name': 'image_10',
     'url': 'https://t4.ftcdn.net/jpg/00/97/58/97/360_F_97589769_t45CqXyzjz0KXwoBZT9PRaWGHRk5hQqQ.jpg'}
]


def download_images(url, file_name, file_path):
    full_path = 'images/' + file_name + '.jpg'
    urllib.request.urlretrieve(url, full_path)


def prev():
    start = timer()

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    for x in images:
        url = x['url']
        file_name = x['name']
        file_path = 'images/'
        download_images(url, file_name, file_path)

    end = timer()
    duration = (timedelta(seconds=end - start)).total_seconds()

    print(f'Entire process has finished in {duration} second(s).')


def new():
    count = 0
    for i in images:
        count += 1

    start = timer()

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    with concurrent.futures.ThreadPoolExecutor(max_workers=count) as executor:
        executor.map(download_images(), range(3))

    end = timer()
    duration = (timedelta(seconds=end - start)).total_seconds()

    print(f'Entire process has finished in {duration} second(s).')
