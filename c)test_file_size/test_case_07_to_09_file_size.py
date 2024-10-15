from before_parallelization import *
from after_parallelization import *
from data import *

list_of_images = images
list_of_videos = videos
list_of_25_videos = videos_25
list_of_50_videos = videos_50


# Test Case 01 - Downloading 25 Videos
# single_threaded_download(list_of_25_videos, '.webm')
# multi_threaded_download(list_of_25_videos, '.webm')

# Test Case 02 - Downloading 50 Videos
single_threaded_download(list_of_50_videos, '.webm')
# multi_threaded_download(list_of_50_videos, '.webm')

# Test Case 03 - Downloading 100 Videos
# single_threaded_download(list_of_25_videos, '.webm')
# multi_threaded_download(list_of_25_videos, '.webm')
