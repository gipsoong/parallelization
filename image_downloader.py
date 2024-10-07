import urllib.request

images = [
    {'name': 'image_1', 'url': 'https://i.imgur.com/vgZrB5U.jpeg'},
    {'name': 'image_2', 'url': 'https://i.imgur.com/ZccahuC.jpeg'},
    {'name': 'image_3', 'url': 'https://i.imgur.com/O3lUGTr.jpeg'},
    {'name': 'image_4', 'url': 'https://i.imgur.com/HwIbeq1.jpeg'},
    {'name': 'image_5', 'url': 'https://i.imgur.com/NuqugTD.jpeg'},
]


def download_image(url, save_as):
    urllib.request.urlretrieve(url, save_as)


def dl(url, file_name, file_path):
    full_path = 'images/' + file_name + '.jpg'
    urllib.request.urlretrieve(url, full_path)


image_url = 'https://static01.nyt.com/images/2021/09/14/science/07CAT-STRIPES/07CAT-STRIPES-mediumSquareAt3X-v2.jpg'
save_as = 'images/cat.jpg'

# download_image(image_url, save_as)

if __name__ == '__main__':
    for x in images:
        print(x)
