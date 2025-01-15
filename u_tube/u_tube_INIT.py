

#==============================================================================


# 08/13/2024 - PLAYLISTS. Works perfectly, downloaded all saved on 8/13

from pytubefix import Playlist
from pytubefix.cli import on_progress
 
url = "https://youtube.com/playlist?list=PL381bIk3sgWGqbzDt63iv1NBtAb_zFO_a&si=-gyFNRH907zky316"

pl = Playlist(url, use_oauth = True, allow_oauth_cache=True)

for video in pl.videos:
    print("downloading...")
    print(f'Title: {video.title}')
    print(f'URL: {video.watch_url}')
    print('---')
    ys = video.streams.get_highest_resolution()
    ys.download()


''' 12/29/2024
(python_venv) C:\_apps\python_venv\Scripts>cd ..\pytube

(python_venv) C:\_apps\python_venv\pytube>python python_youtube.py
Enter the playlist url: https://youtube.com/playlist?list=PL381bIk3sgWHar5fI5CcsJ0Vvihr5F1w8&si=VapGA7u2cntt-VxA
Please select a resolution ['240p', '360p', '480p', '720p', '1080p', '1440p', '2160p']: 2160
Downloading playlist:   0%|                                                                                                       | 0/1 [00:00<?, ?video/s]Downloading The SHOCKING Truth About SYRIA in the Bible - URGENT MESSAGE FROM GOD.mp4 in 360p
----------------------------------
Downloading playlist: 100%|███████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:03<00:00,  3.27s/video]
'''


#==============================================================================

'''
# 08/11/2024 - INDIVIDUAL MP4. Works perfectly, downloaded all saved on 8/13

from pytubefix import YouTube
from pytubefix.cli import on_progress

url = "https://www.youtube.com/watch?v=u1p9IrG-gXY"
 
#yt = YouTube(url, on_progress_callback = on_progress)
# authentication, for age restriction issues and such

#yt = YouTube(url, use_oauth=True, allow_oauth_cache=True, on_progress_callback = on_progress)
# trying to download live
yt = YouTube(url, use_oauth=True, allow_oauth_cache=True, on_progress_callback = on_progress, client='MWEB')

print(yt.title)
 
ys = yt.streams.get_highest_resolution()
ys.download()

'''

''' 12/29/2024
(python_venv) C:\_apps\python_venv\py_tube>python python_youtube.py
✈️#911Truth Part 11: Feature Documentary: 9/11 Alchemy – Facing Reality by Wolf Clan Media
 ↳ |████████████████████████████████████████████████████████████████████████████████████████████████| 100.0%
(python_venv) C:\_apps\python_venv\py_tube>
'''

''' 12/32/2024

'''


#==============================================================================

''' 08/11/2024
from pytube import YouTube

# where to save 
SAVE_PATH = "/_apps/python_venv/pytube/saved"

# link of the video to be downloaded
#   Phil Wickham - House Of The Lord (Official Music Video)
#   https://www.youtube.com/watch?v=h8uKldEUrPE

link = "https://www.youtube.com/watch?v=YKtqN50FIL8"

try: 
    # object creation using YouTube 
    yt = YouTube(link) 
except: 
    #to handle exception 
    print("Connection Error") 

# Get all streams and filter for mp4 files

# AUDIO only
#mp4_streams = yt.streams.filter(file_extension='mp4').all()

# VIDEO and AUDIO
mp4_streams = yt.streams.filter(progressive=True).all()

# get the video with the highest resolution
d_video = mp4_streams[-1]

try: 
    # downloading the video 
    d_video.download(output_path=SAVE_PATH)
    print('Video downloaded successfully!')
except: 
    print("Some Error!")
'''

#==============================================================================

''' THIS WORKS - 05/03/2024
from pytube import YouTube

# where to save 
SAVE_PATH = "/Users/Murat/Desktop/pytube"

# link of the video to be downloaded 
link = "https://www.youtube.com/watch?v=h8uKldEUrPE"

try: 
    # object creation using YouTube 
    yt = YouTube(link) 
except: 
    #to handle exception 
    print("Connection Error") 

# Get all streams and filter for mp4 files
mp4_streams = yt.streams.filter(file_extension='mp4').all()

# get the video with the highest resolution
d_video = mp4_streams[-1]

try: 
    # downloading the video 
    d_video.download(output_path=SAVE_PATH)
    print('Video downloaded successfully!')
except: 
    print("Some Error!")
'''