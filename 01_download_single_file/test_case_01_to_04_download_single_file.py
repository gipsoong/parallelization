from before_parallelization import *
from after_parallelization import *
from data import *

file_size_125mb = file_size_125mb
file_size_250mb = file_size_250mb
file_size_500mb = file_size_500mb
file_size_1gb = file_size_1gb

# Test Case 01 - Downloading a 125mb Video File
# single_threaded_download(file_size_125mb, '.webm') # 10.9s # 8.6s # 8.6s # 8.6s # 8.6s # 9.5s # 10.9s
# multi_threaded_download(file_size_125mb, '.webm', 2) # 8.65s # 8.66s # 8.66s
# multi_threaded_download(file_size_125mb, '.webm', 4) # 8.65s # # 8.66s # 8.66s
# multi_threaded_download(file_size_125mb, '.webm', 6) # 8.65s # 8.65s # 8.66s # 8.6s

# Test Case 02 - Downloading a 250mb Video File
# single_threaded_download(file_size_250mb, '.webm') # 17.68s # 17.68s # 17.67s # 17.68 #
# multi_threaded_download(file_size_250mb, '.webm', 2) # 17.68s # 17.66s # 17.69s
# multi_threaded_download(file_size_250mb, '.webm', 4) # 17.68s # 17.66s # 17.69s
# multi_threaded_download(file_size_250mb, '.webm', 6) # 17.68s # 17.66s # 17.69s

# Test Case 03 - Downloading a 500mb Video File
# single_threaded_download(file_size_500mb, '.webm') # 35.2s # 35.02s # 34.8s # 34.7s # 34.74 # ?185.6s
# multi_threaded_download(file_size_500mb, '.webm', 2) # 41.3s # 35.5s # 35.6 # # 34.8 #34.825
# multi_threaded_download(file_size_500mb, '.webm', 4) # 34.6s # #34.6 # 34.6 # 34.8s # # 34.7s
# multi_threaded_download(file_size_500mb, '.webm', 6) # 34.7s # 35.4 # 34.8s # 34.9s # #35.1

# Test Case 04 - Downloading a 1gb Video File
# single_threaded_download(file_size_1gb, '.webm') # 70.6s
# multi_threaded_download(file_size_1gb, '.webm', 2) # 41.3s # 35.5s # 35.6 # # 34.8 #34.825
# multi_threaded_download(file_size_1gb, '.webm', 4) # 70.4s
# multi_threaded_download(file_size_1gb, '.webm', 6) # 70.4s