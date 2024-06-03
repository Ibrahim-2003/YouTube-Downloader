import os

playlist_link = 'https://youtube.com/playlist?list=PLrnPJCHvNZuBhmqlWEQfvxbNtY6B_XJ3n'

new_file_location = '"/Users/jordanianjoker/Desktop/Code/Youtube Python Downloader/Android Studio/"'

os.system(f'cd {new_file_location}\nyoutube-dl -i -f mp4 --yes-playlist {playlist_link}')

# os.system(f'youtube-dl -i -f mp4 --yes-playlist {playlist_link}')