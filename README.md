# YT Music Download

## Features

Users can download videos or audio-only by providing a link to a video or playlist to a desktop application.

## Limitations

- This application has not been tested on Mac OS or Linux systems
- For playlists of 400+ videos, downloads may be interrupted due to bot detection. This is a known issue. [See this article for details.](https://pytubefix.readthedocs.io/en/latest/user/po_token.html) 


## Source Code Set Up

### Requirements

- Python 3.6+
- Qt Creator Communit 18+

### Set Up Steps

1. Install dependencies: `pip install -r requirements.txt`
2. Run the application: `python main.py`

### Building UI Files

1. Edit the `.ui` file in Qt Creator
2. Build the `.py` file from the `.ui`:
    - (Bash): `pyside6-uic ./UI/downloader_ver2.ui -o ./UI/ui_downloader_ver2.py`
    - (CMD): `pyside6-uic .\UI\downloader_ver2.ui -o .\UI\ui_downloader_ver2.py`

## Contributors

- Project and technical lead: [thegooda](https://github.com/thegooda)
- Project support: [thesamuraiwho](https://github.com/thesamuraiwho)

## License

This project is licensed under the MIT license.

## Sources and Additional Licenses

This project uses the following code and licenses:

- Qt Community under the [LGPL license](https://www.qt.io/development/download-open-source)