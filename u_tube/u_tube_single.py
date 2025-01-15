#==============================================================================

# 01/15/2024 - INDIVIDUAL MP4. Works perfectly.

from pytubefix import YouTube
from pytubefix.cli import on_progress

url = "https://www.youtube.com/watch?v=KzsYaaT_NlI"
 
#yt = YouTube(url, on_progress_callback = on_progress)
# authentication, for age restriction issues and such

#yt = YouTube(url, use_oauth=True, allow_oauth_cache=True, on_progress_callback = on_progress)
# trying to download live
yt = YouTube(url, use_oauth=True, allow_oauth_cache=True, on_progress_callback = on_progress, client='MWEB')

print(yt.title)
 
ys = yt.streams.get_highest_resolution()
ys.download()

''' 01/15/2025
(python_venv) C:\_apps\python_venv\python_apps\py_tube>python u_tube_single.py
Christians and Israel Today Romans 96
 ↳ |██████████████████████████████████████████████████████████████████████████████████████████████████████| 100.0%
(python_venv) C:\_apps\python_venv\python_apps\py_tube>
'''
