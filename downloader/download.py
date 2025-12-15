import sys
import os
import pytubefix
import ffmpeg
import time
import random
from datetime import datetime
from pytubefix import Playlist
from pytubefix import YouTube

def music_download(folder_path, youtube_url, file_type):
    if "list=" in youtube_url:

        yt_pl = Playlist(youtube_url)
        print(f"Found {len(yt_pl.video_urls)} videos")
        
        count = 1
        for video_url in yt_pl.video_urls:
            try:
                yt = YouTube(video_url, client='WEB')
                print(f"Downloading: {count}- {yt.title}")         
                
                stream = yt.streams.get_audio_only()
                stream.download(
                    output_path=folder_path, 
                    skip_existing=True, 
                    filename_prefix=f"{count}- ", 
                    timeout=4, 
                    max_retries=1
                    )
                
            except Exception as e:
                error_line = f"{datetime.now()} | {video_url} | {str(e)[:200]}\n"
                
                print(f"Error: {str(e)[:80]} (skipped)")
                
                with open('Error.txt', 'a') as file:
                    file.write(error_line)
            
            if count % 10 == 0:
                cooldown = random.uniform(20, 40)
                print(f"\nCooling down for {cooldown:.1f} sec to avoid rate limits…")
                time.sleep(cooldown)

            count += 1
            time.sleep(random.uniform(4, 7.5))
        
    else:    #if single video 
        # Create a Yotube Object and fetch the stream URL 
        print('Downloading audio from single youtube video...')
        yt = YouTube(youtube_url, client='WEB')
        
        # get audio only and download to path given
        print('Fetching audio stream...')
        stream = yt.streams.get_audio_only()
        stream.download(output_path=folder_path, skip_existing=True)