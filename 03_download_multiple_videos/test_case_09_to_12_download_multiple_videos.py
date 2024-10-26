from before_parallelization import *
from after_parallelization import *
from data import *

list_of_5_videos = videos_5
list_of_10_videos = videos_10
list_of_20_videos = videos_20
list_of_40_videos = videos_40

# Test Case 09 - Downloading 5 Videos (126mb average)
# single_threaded_download(list_of_5_videos, '.webm') # 43.7s #43.53 #43.52 #43.68 #43.57
# multi_threaded_download(list_of_5_videos, '.webm', 2) #26.07 #26.09 #26.08 #26.82 #26.14
# multi_threaded_download(list_of_5_videos, '.webm', 4) # 17.07 # 16.94 # 17.14 # 16.95 #16.94
# multi_threaded_download(list_of_5_videos, '.webm', 6) # 11.92s # 12.15 # 12.23 # 12.24s # 12.18s # 11.71s #

# Test Case 10 - Downloading 10 Videos (125mb average)
# single_threaded_download(list_of_10_videos, '.webm') # 88.51s # 88.6s #88.6 #88.6 #88.58 # 88.52 #
# multi_threaded_download(list_of_10_videos, '.webm', 2) # 46.05s # 46.1 # 46s # # 46.01s # 46.06s
# multi_threaded_download(list_of_10_videos, '.webm', 4) # 27.8s # 27.6 # 27.7 # 27.7s # 27.45s
# multi_threaded_download(list_of_10_videos, '.webm', 6) # 24.57s # 23.8s # 24.01s # 24.77s # 24.9s # 24.5s # 24.3s

# Test Case 11 - Downloading 20 Videos (125mb average)n
# single_threaded_download(list_of_20_videos, '.webm') # 176.5s # 176.45 # 176.45 # 176.55 #176.48 # 176.7s # 176.64s
# multi_threaded_download(list_of_20_videos, '.webm', 2) #89.6s #89.64 #89.58 #89.78 #89.527 # 89.55s
# multi_threaded_download(list_of_20_videos, '.webm', 4) #45.9 #46.61 #48.31 #46.6s # 46.81s # 46.67
# multi_threaded_download(list_of_20_videos, '.webm', 6) # 46.89s # 47.52s # 46.26s # 45.8s # 46.8s

# Test Case 12 - Downloading 40 Videos (125mb average)
# single_threaded_download(list_of_40_videos, '.webm') # 354.6s # 355s # 354s # 354.5s # 354.8s # 354.6s
# multi_threaded_download(list_of_40_videos, '.webm', 2) # 178s # 178.7s # 178.3s # 178.4s # 178.46 # 178.5s
# multi_threaded_download(list_of_40_videos, '.webm', 4) # 96.54s # 93.29 # 92.84s # 93.26s # 92.85s # 92.68
# multi_threaded_download(list_of_40_videos, '.webm', 6) # 92.12s # 93.6 # 92.53s # 93.18
