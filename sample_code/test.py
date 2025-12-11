import sys
import os
import random
import time
from datetime import datetime
import pytubefix
from pytubefix import Playlist, YouTube
from pytubefix.cli import on_progress


# -----------------------------
# INPUT
# -----------------------------
youtube_url = input("Enter YouTube link: ").strip()
folder_name = input("Enter folder name: ").strip()

folder_path = os.path.join(folder_name, "")
os.makedirs(folder_path, exist_ok=True)

start_tick = time.time()

# -----------------------------
# SINGLE VIDEO
# -----------------------------
if "list=" not in youtube_url:
    print("Downloading audio from a single YouTube video...\n")

    yt = YouTube(
        youtube_url,
        on_progress_callback=on_progress
    )

    print(f"Title: {yt.title}")
    stream = yt.streams.get_audio_only()
    
    if stream:
        print(f"Downloading: {stream.filesize / (1024*1024):.2f} MB")
        stream.download(output_path=folder_path, skip_existing=True)
        print(f"\nDone! Saved at: {folder_name}")
    else:
        print("No audio stream found!")
    
    print(f"Execution time: {time.time() - start_tick:.2f} seconds")
    sys.exit()


# -----------------------------
# PLAYLIST MODE
# -----------------------------
print("\nLoading playlist… This may take a moment.\n")

yt_pl = Playlist(youtube_url)

print(f"Found {len(yt_pl.video_urls)} videos\n")

count = 1

for video_url in yt_pl.video_urls:
    try:
        print(f"\n[{count}/{len(yt_pl.video_urls)}]")
        
        yt = YouTube(video_url, on_progress_callback=on_progress)
        
        print(f"Title: {yt.title}")

        stream = yt.streams.get_audio_only()

        if stream:
            stream.download(
                output_path=folder_path,
                skip_existing=True,
                filename_prefix=f"{count}- "
            )
        else:
            print("No audio stream found, skipping...")

    except Exception as e:
        print(f"⚠️ Error: {str(e)[:80]} (skipped)")

    # -----------------------------
    # SLOW DOWN TO AVOID IP BAN
    # -----------------------------
    time.sleep(random.uniform(4, 9))

    # extra big rest every 10 videos
    if count % 10 == 0:
        cooldown = random.uniform(20, 40)
        print(f"\nCooling down for {cooldown:.1f} sec to avoid rate limits…")
        time.sleep(cooldown)

    count += 1

print(f"\nAll done! Saved at: {folder_name}")
print(f"Execution time: {time.time() - start_tick:.2f} seconds\n")

# import sys
# import os
# import random
# import time
# from datetime import datetime
# import pytubefix
# from pytubefix import Playlist, YouTube
# from pytubefix.cli import on_progress


# # -----------------------------
# # SAFETY SETTINGS
# # -----------------------------

# # Use music clients for audio downloads
# MUSIC_CLIENTS = ['WEB_MUSIC', 'ANDROID_MUSIC']


# # -----------------------------
# # INPUT
# # -----------------------------
# youtube_url = input("Enter YouTube link: ").strip()
# folder_name = input("Enter folder name: ").strip()

# folder_path = os.path.join(folder_name, "")
# os.makedirs(folder_path, exist_ok=True)

# start_tick = time.time()

# # -----------------------------
# # SINGLE VIDEO
# # -----------------------------
# if "list=" not in youtube_url:
#     print("Downloading audio from a single YouTube video...\n")

#     yt = YouTube(
#         youtube_url,
#         client='WEB_MUSIC',      # Better for audio content
#         use_po_token=True,
#         on_progress_callback=on_progress
#     )

#     stream = yt.streams.get_audio_only()
#     stream.download(output_path=folder_path, skip_existing=True)

#     print(f"\nDone! Saved at: {folder_name}")
#     print(f"Execution time: {time.time() - start_tick:.2f} seconds")
#     sys.exit()


# # -----------------------------
# # PLAYLIST MODE
# # -----------------------------
# print("\nLoading playlist… This may take a moment.\n")

# yt_pl = Playlist(
#     youtube_url,
#     client="WEB_MUSIC",
#     use_po_token=True
# )

# print(f"Found {len(yt_pl.video_urls)} videos\n")

# count = 1

# for video in yt_pl.videos:
#     try:
#         print(f"\n[{count}/{len(yt_pl.video_urls)}] {video.title}")

#         yt = YouTube(
#             video.watch_url,
#             client="WEB_MUSIC",  # Better for audio content
#             use_po_token=True
#         )

#         stream = yt.streams.get_audio_only()

#         stream.download(
#             output_path=folder_path,
#             skip_existing=True,
#             filename_prefix=f"{count}- "
#         )

#     except Exception as e:
#         print(f"⚠️ Error: {str(e)[:80]} (skipped)")

#     # -----------------------------
#     # SLOW DOWN TO AVOID IP BAN
#     # -----------------------------
#     time.sleep(random.uniform(4, 9))

#     # extra big rest every 10 videos
#     if count % 10 == 0:
#         cooldown = random.uniform(20, 40)
#         print(f"\nCooling down for {cooldown:.1f} sec to avoid rate limits…")
#         time.sleep(cooldown)

#     count += 1

# print(f"\nAll done! Saved at: {folder_name}")
# print(f"Execution time: {time.time() - start_tick:.2f} seconds\n")