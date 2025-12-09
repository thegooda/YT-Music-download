import sys
import os
import pytubefix
import ffmpeg
import time
import pandas as pd
from datetime import datetime
from pytubefix import Playlist
from pytubefix.cli import on_progress
    

youtube_url = input("Enter youtube link: ")

pl = Playlist(youtube_url)

print(f"Found {len(pl.video_urls)} videos in playlist.")
print("Downloading...\n")


for video in pl.videos:
    print(f"Downloading: {video.title}")
    
    stream = video.streams.get_audio_only()
    out_file = stream.download()   # downloads .mp4 or .webm

    mp3_file = os.path.splitext(out_file)[0] + ".mp3"
    
    (
        ffmpeg
        .input(out_file)
        .output(mp3_file, **{'q:a': 3}, acodec="libmp3lame")
        .run(overwrite_output=True, quiet=True)
    )
    
    os.remove(out_file)  # delete original file
    
    print(f"Saved MP3: {mp3_file}")

print("\nDone!")
