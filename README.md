# Video Looper

```
 ██▒   █▓ ██▓▓█████▄ ▓█████  ▒█████      ██▓     ▒█████   ▒█████   ██▓███  ▓█████  ██▀███  
▓██░   █▒▓██▒▒██▀ ██▌▓█   ▀ ▒██▒  ██▒   ▓██▒    ▒██▒  ██▒▒██▒  ██▒▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒
 ▓██  █▒░▒██▒░██   █▌▒███   ▒██░  ██▒   ▒██░    ▒██░  ██▒▒██░  ██▒▓██░ ██▓▒▒███   ▓██ ░▄█ ▒
  ▒██ █░░░██░░▓█▄   ▌▒▓█  ▄ ▒██   ██░   ▒██░    ▒██   ██░▒██   ██░▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  
   ▒▀█░  ░██░░▒████▓ ░▒████▒░ ████▓▒░   ░██████▒░ ████▓▒░░ ████▓▒░▒██▒ ░  ░░▒████▒░██▓ ▒██▒
   ░ ▐░  ░▓   ▒▒▓  ▲░ ▒░ ░░ ▒░▒░▒░    ░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
   ░ ░░   ▒ ░ ░ ▒  ▲  ░ ░  ░  ░ ▒ ▒░    ░ ░ ▒  ░  ░ ▒ ▒░   ░ ▒ ▒░ ░▒ ░      ░ ░  ░  ░▒ ░ ▒░
     ░░   ▒ ░ ░ ░  ░    ░   ░ ░ ░ ▒       ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒  ░░          ░     ░░   ░ 
      ░   ░     ░       ░  ░    ░ ░         ░  ░    ░ ░      ░ ░              ░  ░   ░     
     ░        ░
```

A simple Python program that allows users to loop a video file and optionally save the looped video.

## Demo

[![Video Looper Demo](https://img.youtube.com/vi/rmEFWojuPbU/0.jpg)](https://youtu.be/rmEFWojuPbU)

## Features

- Simple and intuitive user interface
- Supports any video format supported by OpenCV
- Real-time video playback
- Two playback modes:
  - Loop for a specific number of times
  - Loop for a specific duration (in minutes)
- Option to save the looped video
- Progress indicator showing which loop is currently playing
- Ability to quit at any time by pressing 'q'

## Installation

1. Install the required package:
```bash
pip install -r requirements.txt
```

## Usage

Run the program:
```bash
python video_looper.py
```

The program will prompt you to:
1. Enter the path to your video file
2. Choose whether to save the looped video
3. Choose a playback mode:
   - Loop for a specific number of times
   - Loop for a specific duration (in minutes)
4. Enter the desired number of loops or duration

The video will play in a window. A progress indicator will show which loop is currently playing. Press 'q' at any time to quit.

If you chose to save the video, it will be saved as "[original_filename]_looped.mp4" in the same directory as the original video.

## Requirements

- Python 3.x
- OpenCV (cv2)
