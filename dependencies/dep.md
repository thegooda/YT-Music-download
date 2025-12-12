// Using 3.13.4 Venv

// Cmd for install

pip install pytubefix
pip install ffmpeg-python
pip install pandas
pip install nodejs-wheel
pip install pyside6



// Check if installs worked

python -c "import pytubefix, ffmpeg, pandas; print('OK')"

https://www.youtube.com/watch?v=3BFTio5296w

pyinstaller --noconsole --onefile main.py
pyside6-uic .\UI\downloader_ver1.ui -o .\UI\ui_downloader_ver1.py