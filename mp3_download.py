import os

with open('/Users/jordanianjoker/Desktop/Code/Youtube Python Downloader/ytmp3_links.txt') as file:
    links = file.read().split('\n')

# playlist_link = 'https://www.youtube.com/watch?v=wYQHwxcpHus&ab_channel=%D9%83%D8%AD%D9%8A%D9%84%D8%A7%D9%86%D8%A3%D9%81%D8%B6%D9%84%D8%A7%D9%84%D8%B4%D9%8A%D9%84%D8%A7%D8%AA-kahilanafdalalshailat'
for link in links:
    new_file_location = '"/Users/jordanianjoker/Desktop/Code/Youtube Python Downloader/Jordan/"'

    os.system(f'cd {new_file_location}\nyoutube-dl -x --audio-format mp3 {link}')
