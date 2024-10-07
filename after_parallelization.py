from timeit import default_timer as timer
from datetime import timedelta
import urllib.request

images = [
    {'name': 'image_1', 'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/A-Cat.jpg/2560px-A-Cat.jpg'},
    {'name': 'image_2',
     'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Cat_img.jpg/1280px-Cat_img.jpg'},
    {'name': 'image_3',
     'url': 'https://images.squarespace-cdn.com/content/v1/5452d441e4b0c188b51fef1a/1615326541809'
            '-TW01PVTOJ4PXQUXVRLHI/male-orange-tabby-cat.jpg'},
]


def download_images(url, file_name, file_path):
    full_path = 'images/' + file_name + '.jpg'
    urllib.request.urlretrieve(url, full_path)


if __name__ == '__main__':
    start = timer()

    for x in images:
        url = x['url']
        file_name = x['name']
        file_path = 'images/'
        download_images(url, file_name, file_path)

    end = timer()
    duration = (timedelta(seconds=end - start)).total_seconds()

    print(f'Entire process has finished in {duration} second(s).')
