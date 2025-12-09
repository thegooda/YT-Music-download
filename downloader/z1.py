import sys
import os
import pytubefix
import ffmpeg
import time
import pandas as pd
from datetime import datetime
from pytubefix import Playlist
from pytubefix.cli import on_progress


youtube_url = input("Enter YouTube link: ")

folder_name = input("Enter folder name: ")
folder_path = os.path.join(folder_name, "") # Adds correct separator automatically

if "list" in youtube_url:
    yt_pl = Playlist(youtube_url)
    print(f"Found {len(yt_pl.video_urls)} videos")
    
    count = 1
    
    for video in yt_pl.videos:
        try:
            print(f"Downloading: {video.title} - {count}")
            stream = video.streams.get_audio_only()
            stream.download(output_path=folder_path,filename_prefix=f"{count}- ")
            
        except Exception as e:
            print(F"Error: video is privated or deleted, skipping video")
            
        count += 1
        time.sleep(5)
    print(f"\nFinish, saved at {folder_name}")
    
else:    #if single video 
    # Create a Yotube Object and fetch the stream URL 
    print('Downloading audio from single youtube video...')
    yt = pytubefix.YouTube(youtube_url)
    
    # get audio only and download to path given
    print('Fetching audio stream...')
    stream = yt.streams.get_audio_only()
    stream.download(output_path=folder_path)
    
    