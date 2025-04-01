from setuptools import setup, find_packages

# ASCII art banner
banner = r"""
 ██▒   █▓ ██▓▓█████▄ ▓█████  ▒█████      ██▓     ▒█████   ▒█████   ██▓███  ▓█████  ██▀███  
▓██░   █▒▓██▒▒██▀ ██▌▓█   ▀ ▒██▒  ██▒   ▓██▒    ▒██▒  ██▒▒██▒  ██▒▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒
 ▓██  █▒░▒██▒░██   █▌▒███   ▒██░  ██▒   ▒██░    ▒██░  ██▒▒██░  ██▒▓██░ ██▓▒▒███   ▓██ ░▄█ ▒
  ▒██ █░░░██░░▓█▄   ▌▒▓█  ▄ ▒██   ██░   ▒██░    ▒██   ██░▒██   ██░▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  
   ▒▀█░  ░██░░▒████▓ ░▒████▒░ ████▓▒░   ░██████▒░ ████▓▒░░ ████▓▒░▒██▒ ░  ░░▒████▒░██▓ ▒██▒
   ░ ▐░  ░▓   ▒▒▓  ▲░ ▒░ ░░ ▒░▒░▒░    ░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
   ░ ░░   ▒ ░ ░ ▒  ▒  ░ ░  ░  ░ ▒ ▒░    ░ ░ ▒  ░  ░ ▒ ▒░   ░ ▒ ▒░ ░▒ ░      ░ ░  ░  ░▒ ░ ▒░
     ░░   ▒ ░ ░ ░  ░    ░   ░ ░ ░ ▒       ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒  ░░          ░     ░░   ░ 
      ░   ░     ░       ░  ░    ░ ░         ░  ░    ░ ░      ░ ░              ░  ░   ░     
     ░        ░
"""

setup(
    name="video_looper",
    version="1.0.0",
    description="A simple video looper application",
    long_description=f"""
{banner}

Video Looper is a simple Python program that allows users to loop video files.
It features automatic content analysis for optimal loop points, real-time playback,
and options to save the looped video.

Features:
- Loop videos for a specific number of times or duration
- Automatic content analysis for optimal loop points
- Real-time video playback
- Progress indicator during processing
- Option to save the looped video
- Command line interface with user-friendly prompts
    """,
    long_description_content_type='text/markdown',
    author="Ahmed Elbaroudy",
    url="https://github.com/Ahmed-Elbaroudy/video-looper.git",
    packages=find_packages(),
    install_requires=[
        'opencv-python>=4.5.0',
        'colorama>=0.4.6',
        'moviepy>=1.0.3',
        'numpy>=1.21.0',
        'pydub>=0.25.1'
    ],
    entry_points={
        'console_scripts': [
            'video_looper=video_looper:main'
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Operating System :: OS Independent',
        'Topic :: Multimedia :: Video'
    ],
    python_requires='>=3.7',
    keywords='video looper loop video playback',
    license='MIT'
)
