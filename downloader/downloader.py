import sys
import pytubefix
import ffmpeg
import time
from datetime import datetime

# gets first argv in cmd line

# youtube_url = sys.argv[1]

youtube_url = input("Enter youtube link: ")
# Specifty output file name to download audio to

filename = f"audios/" #Select folder
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") # time of download
filename += f"audio_{timestamp}.mp3" # name of file

time.sleep(2)

# Create a Yotube Object and fetch the stream URL
print('Downloading audio from youtube...')
yt = pytubefix.YouTube(youtube_url)

# Gets first avaibable stream (usually audio)
print('Fetching audio stream...')
stream = yt.streams[0].url 

#Use ffmpeg to convert audio stream to .mp3 file
print('Use ffmpeg to convert the audio stream to a .mp3 file...')
ffmpeg.input(stream).output(filename, format='mp3', loglevel="error").run()

#save the filename
text_file = open(f"filename_audio.txt", "w")
text_file.write(f"{filename}")
text_file.close()

print(f"Audio downloaded and saved as {filename}")
