import sys
import os
import pytubefix
import ffmpeg
import time
import random
import pandas as pd
from datetime import datetime
from pytubefix import Playlist
from pytubefix.cli import on_progress
from pytubefix import YouTube


youtube_url = input("Enter YouTube link: ")
folder_name = input("Enter folder name: ")
folder_path = os.path.join(folder_name, "") # Adds correct separator automatically

start_tick = time.time()
if "list=" in youtube_url:

    yt_pl = Playlist(youtube_url, client="WEB_MUSIC", use_po_token=True)
    print(f"Found {len(yt_pl.video_urls)} videos")
    
    count = 1
    for video in yt_pl.videos:
        try:
            print(f"Downloading: {count}- {video.title}")            
            
            stream = video.streams.get_audio_only()
            stream.download(output_path=folder_path, skip_existing=True, filename_prefix=f"{count}- ", timeout=4)
            
        except Exception as e:
            print(F"Error: video is privated/deleted or age restricted, skipping video")
            
        count += 1
        time.sleep(random.uniform(.5, 2.5))
    print(f"\nFinish, saved at {folder_name}")
    
else:    #if single video 
    # Create a Yotube Object and fetch the stream URL 
    print('Downloading audio from single youtube video...')
    yt = YouTube(youtube_url, client='WEB_MUSIC', on_progress_callback=on_progress, use_po_token=True)
    
    # get audio only and download to path given
    print('Fetching audio stream...')
    stream = yt.streams.get_audio_only()
    stream.download(output_path=folder_path, skip_existing=True)
    
    print(f"\nFinish, saved at {folder_name}")

print(f"\nExecution time: {time.time() - start_tick: 2f} sceonds")