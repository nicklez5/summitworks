import os
filename = "1.txt"
file_stats = os.stat(filename)
print(f'File Size in Bytes is {file_stats.st_size}')
