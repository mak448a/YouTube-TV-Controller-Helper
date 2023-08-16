# YouTube-TV-Controller-Helper
Control YouTube TV's web interface with a game controller!
Set your user agent as a [PS4](https://www.reddit.com/r/htpc/comments/y5o7mi/youtube_leanback_tv_useragent_for_4k_60fps/)
using [User Agent Switcher](https://addons.mozilla.org/en-US/firefox/addon/user-agent-string-switcher/), and load up [YouTube TV!](https://youtube.com/tv)

THIS ONLY WORKS ON LINUX SYSTEMS (Add a pull request if you want to add Windows support)

Note: This doesn't have press and hold support yet.


## Prerequisites
- For Linux: You need pactl installed
- For Linux: Xorg (or a browser that uses XWayland, e.g. [Firefox 100](https://download-installer.cdn.mozilla.net/pub/firefox/releases/100.0/linux-x86_64/en-US/) with [disabled updates](https://winaero.com/how-to-disable-firefox-background-updates/))
- Python (needs to be on your PATH variable)

## Setup and Run
Install dependencies
```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Run the program
```shell
python3 yt_tv.py
```

## Usage Guide
| Button | Function                      |
|--------|-------------------------------|
| Cross  | Confirm                       |
| Circle | Back                          |
| Start  | Set fullscreen browser window |
| D-Pad  | Move cursor                   |
