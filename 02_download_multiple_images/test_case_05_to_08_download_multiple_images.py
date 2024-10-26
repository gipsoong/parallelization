from before_parallelization import *
from after_parallelization import *
from data import *

list_of_2_images = images_2
list_of_4_images = images_4
list_of_8_images = images_8
list_of_16_images = images_16

# Test Case 05 - Downloading 2 Images (50 mb average)
# single_threaded_download(list_of_2_images, '.jpg') # 7.2s # 7.08s # 7.1 # 7.0s # 7.1s # 7.07s
# multi_threaded_download(list_of_2_images, '.jpg', 2) # 3.91s # 3.91s # 3.92s # 3.911s # 3.9s #
# multi_threaded_download(list_of_2_images, '.jpg', 4) # 3.91s # 3.9s # 3.91s # 3.92s #  3.92s # 3.91s #
# multi_threaded_download(list_of_2_images, '.jpg', 6) # 3.9s # 3.961s # 3.915s # 3.921s # 3.91s # 3.95s # 3.925s #

# Test Case 06 - Downloading 4 Images (50 mb average)
# single_threaded_download(list_of_4_images, '.jpg') # 13.96s # # 13.96s # 13.967s # 13.95s # 13.97s # 13.96s #
# multi_threaded_download(list_of_4_images, '.jpg', 2) # 7.62s # 7.6s # 7.61s # 7.6s # 7.61s #
# multi_threaded_download(list_of_4_images, '.jpg', 4) # 4s # # 4.07s # # 3.98s # # 3.96s # 4.01s
# multi_threaded_download(list_of_4_images, '.jpg', 6) # 4.01ss # 3.97s # 3.97s # 4.03s # 4.01s

# Test Case 07 - Downloading 8 Images (50 mb average)
# single_threaded_download(list_of_8_images, '.jpg') # 27.7s # 27.78s # 27.72s # 27.7s # 27.7s #
# multi_threaded_download(list_of_8_images, '.jpg', 2) # 14.89s # 14,91s # 14.9s # 14.89s # 14.89 s
# multi_threaded_download(list_of_8_images, '.jpg', 4) # 7.6s # 7.62s # 7.6s # 7.55s # 7.64s # 7.56s #
# multi_threaded_download(list_of_8_images, '.jpg', 6) # 7.74s # 7.95s # 7.97s # 7.8s # 8.04s #

# Test Case 08 - Downloading 16 Images (50 mb average)
# single_threaded_download(list_of_16_images, '.jpg') # 55.04s # 54.94s # 55.53s # 54.97s # 55.06
# multi_threaded_download(list_of_16_images, '.jpg', 2) # 27.9s # 28.1s # 28.06s # 28.08 # 28.05 # 28.01s # cc
# multi_threaded_download(list_of_16_images, '.jpg', 4) # 14.52s # 14.55s # 14.66s # 14.54s # 14.54 # 14.64
# multi_threaded_download(list_of_16_images, '.jpg', 6)  # 14.27s # 14.08s # 14.56s # 14.3s # 14.46s # 14.275s
