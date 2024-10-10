import urllib.request

images = [
    {'name': 'image_1', 'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/A-Cat.jpg/2560px-A-Cat.jpg'},
    {'name': 'image_2',
     'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Cat_img.jpg/1280px-Cat_img.jpg'},
    {'name': 'image_3',
     'url': 'https://images.squarespace-cdn.com/content/v1/5452d441e4b0c188b51fef1a/1615326541809-TW01PVTOJ4PXQUXVRLHI/male-orange-tabby-cat.jpg'},
]


def download_images(url, file_name, file_path):
    full_path = 'images/' + file_name + '.jpg'
    urllib.request.urlretrieve(url, full_path)


if __name__ == '__main__':
    for x in images:
        url = x['url']
        file_name = x['name']
        file_path = 'images/'
        download_images(url, file_name, file_path)


def dl(url, save_as):
    urllib.request.urlretrieve(url, save_as)


image_url = 'https://static01.nyt.com/images/2021/09/14/science/07CAT-STRIPES/07CAT-STRIPES-mediumSquareAt3X-v2.jpg'
save_as = 'images/cat.jpg'

dl(image_url, save_as)
