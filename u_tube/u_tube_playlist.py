#==============================================================================

# 01/15/2025 - PLAYLISTS. Works perfectly, downloaded all saved on 8/13

from pytubefix import Playlist
from pytubefix.cli import on_progress
 
url = "https://youtube.com/playlist?list=PL381bIk3sgWF7V4IRk02pGILdxwc5mLZW&si=2g-lSkg42ocvJEdg"

pl = Playlist(url, use_oauth = True, allow_oauth_cache=True)

for video in pl.videos:
    print("downloading...")
    print(f'Title: {video.title}')
    print(f'URL: {video.watch_url}')
    print('---')
    ys = video.streams.get_highest_resolution()
    ys.download()


''' 01/15/2025
(python_venv) C:\_apps\python_venv\python_apps\py_tube>python u_tube_playlist.py
downloading...
Title: HOW TO TUNE YOUR UKULELE & USE A CLIP-ON TUNER
URL: https://youtube.com/watch?v=9ESYlESDJ90
---
downloading...
Title: DAY 1 - SET UP YOUR UKE ZONE - 30 DAY UKE CHALLENGE
URL: https://youtube.com/watch?v=QRAKvghfOxk
---
downloading...
Title: I'm Yours - Jason Mraz - Easy Beginner Song Ukulele Tutorial
URL: https://youtube.com/watch?v=5l2ASKiFlF8
---
downloading...
Title: Song 5 | I'm Yours by Jason Mraz | Uke Should Know Challenge
URL: https://youtube.com/watch?v=ZSYj3LdqUBo
---

(python_venv) C:\_apps\python_venv\python_apps\py_tube>
'''
