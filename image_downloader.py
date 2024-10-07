import urllib.request


def download_image(url, save_as):
    urllib.request.urlretrieve(url, save_as)


image_url = 'https://static01.nyt.com/images/2021/09/14/science/07CAT-STRIPES/07CAT-STRIPES-mediumSquareAt3X-v2.jpg'
save_as = 'images/cat.jpg'

download_image(image_url, save_as)