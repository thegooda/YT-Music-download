from pytubefix import Playlist

youtube_url = input("Enter YouTube playlist link: ")

pl = Playlist(youtube_url)

print(f"Found {len(pl.video_urls)} videos.")
print("Downloading highest-quality audio (Opus)...\n")

for video in pl.videos:
    print(f"Downloading: {video.title}")

    stream = video.streams.get_audio_only()  # Best Opus track available
    out_file = stream.download()             # Saves .webm (Opus)

    print(f"Saved: {out_file}")

print("\nDone! Highest quality with minimal file size.")

