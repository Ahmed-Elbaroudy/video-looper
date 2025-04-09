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

A simple Python program that allows users to loop a video file and save it.

## Demo

[![Video Looper Demo](https://img.youtube.com/vi/rmEFWojuPbU/0.jpg)](https://youtu.be/rmEFWojuPbU)

## Features

- Simple and intuitive user interface
- Supports any video format supported by OpenCV
- Progress indicator 
- Ability to quit at any time by pressing 'q'
- Two playback modes:
  - Loop for a specific number of times
  - Loop for a specific duration (in minutes)

## Installation

1. Install the required package:
```bash
pip install -r requirements.txt
```

## Usage

Run the program NOTE: Run this program in a terminal that has admin permission or else the program will not work
```bash
python video_looper.py
```

The program will prompt you to:
1. Enter the path to your video file
2. Choose a playback mode:
   - Loop for a specific number of times
   - Loop for a specific duration (in minutes)
4. Enter the desired number of loops or duration


when you save the video, it will be saved as "[original_filename]_looped.mp4" in the same directory as the original video.

## Requirements

- Python 3.x
- OpenCV (cv2)
