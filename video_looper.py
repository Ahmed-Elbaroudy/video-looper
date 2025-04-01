import sys
import os
import time
import threading
from datetime import timedelta
import msvcrt
from colorama import Fore, Style, init
from moviepy.editor import VideoFileClip, concatenate_videoclips
from pathlib import Path
import numpy as np
import cv2

# Initialize colorama
init()

def loading_animation(duration):
    try:
        frames = ["|", "/", "-", "\\"]
        start_time = time.time()
        while time.time() - start_time < duration:
            for frame in frames:
                if hasattr(sys, 'exit_flag') and sys.exit_flag:
                    return
                remaining = duration - (time.time() - start_time)
                print(Fore.YELLOW + f"\rProcessing video {frame} (Time remaining: {timedelta(seconds=int(remaining))})" + Style.RESET_ALL, end="")
                time.sleep(0.1)
        print(Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"\nError in loading animation: {str(e)}" + Style.RESET_ALL)
        print(Style.RESET_ALL)

def print_banner():
    try:
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
        print(Fore.GREEN + banner + Style.RESET_ALL)
        print(Fore.LIGHTBLACK_EX + " " * 30 + "Made by Ahmed Elbaroudy" + Style.RESET_ALL)
        print("\n")
    except Exception as e:
        print(Fore.RED + f"\nError printing banner: {str(e)}" + Style.RESET_ALL)

def validate_video_path(video_path):
    try:
        if not video_path:
            raise ValueError("Video path cannot be empty")
            
        # Check if file exists
        if not os.path.exists(video_path):
            print(Fore.RED + "\nFile not found." + Style.RESET_ALL)
            return False

        # Check if it's a file
        if not os.path.isfile(video_path):
            print(Fore.RED + "\nThis is not a file." + Style.RESET_ALL)
            return False

        # Check file permissions
        try:
            # Check read permissions
            with open(video_path, 'rb') as f:
                f.read(1)
        except PermissionError:
            print(Fore.RED + "\nNo read permissions for this file." + Style.RESET_ALL)
            return False
        except Exception as e:
            print(Fore.RED + f"\nError accessing file: {str(e)}" + Style.RESET_ALL)
            return False

        # Check file size
        try:
            file_size = os.path.getsize(video_path)
            if file_size > 10 * 1024 * 1024 * 1024:  # 10GB limit
                print(Fore.RED + "\nFile is too large (over 10GB)." + Style.RESET_ALL)
                return False
        except Exception as e:
            print(Fore.RED + f"\nError checking file size: {str(e)}" + Style.RESET_ALL)
            return False

        return True

    except Exception as e:
        print(Fore.RED + f"\nError validating video: {str(e)}" + Style.RESET_ALL)
        return False

def analyze_video_content(video_path):
    """Analyze video content to determine optimal loop points"""
    try:
        # Open video file
        cap = cv2.VideoCapture(video_path)
        
        # Get video properties
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = frame_count / fps
        
        # Analyze frame similarity
        frame_interval = int(fps * 2)  # Check every 2 seconds
        similarity_threshold = 0.95
        
        # Process frames
        frame_data = []
        for i in range(0, frame_count, frame_interval):
            cap.set(cv2.CAP_PROP_POS_FRAMES, i)
            ret, frame = cap.read()
            if not ret:
                break
                
            # Convert to grayscale and resize for faster processing
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            small = cv2.resize(gray, (100, 100))
            frame_data.append(small.flatten())
        
        cap.release()
        
        # Convert to numpy array
        frame_data = np.array(frame_data)
        
        # Calculate similarity between frames
        similarities = []
        for i in range(len(frame_data) - 1):
            similarity = np.corrcoef(frame_data[i], frame_data[i + 1])[0, 1]
            similarities.append(similarity)
        
        # Find optimal loop points
        optimal_points = []
        for i in range(len(similarities) - 1):
            if similarities[i] > similarity_threshold:
                frame_time = (i * frame_interval) / fps
                optimal_points.append(frame_time)
        
        # If no good points found, use default
        if not optimal_points:
            optimal_points = [duration / 2]
        
        # Return the best loop point
        return max(optimal_points)
        
    except Exception as e:
        print(Fore.RED + f"\nError analyzing video content: {str(e)}" + Style.RESET_ALL)
        return None

def ensure_directory_exists(directory):
    try:
        if not directory:
            raise ValueError("Directory path cannot be empty")
            
        # Check if directory exists
        if not os.path.exists(directory):
            # Try to create directory
            try:
                os.makedirs(directory)
            except PermissionError:
                print(Fore.RED + "\nPermission denied to create directory." + Style.RESET_ALL)
                return False
            except Exception as e:
                print(Fore.RED + f"\nError creating directory: {str(e)}" + Style.RESET_ALL)
                return False

        # Check write permissions
        try:
            test_file = os.path.join(directory, "test_permission.txt")
            with open(test_file, 'w') as f:
                f.write("test")
            os.remove(test_file)
        except PermissionError:
            print(Fore.RED + "\nNo write permissions in this directory." + Style.RESET_ALL)
            return False
        except Exception as e:
            print(Fore.RED + f"\nError checking permissions: {str(e)}" + Style.RESET_ALL)
            return False

        return True

    except Exception as e:
        print(Fore.RED + f"\nError ensuring directory exists: {str(e)}" + Style.RESET_ALL)
        return False

def render_video(final_clip, output_path, fps):
    try:
        print(Fore.GREEN + "\nStarting video rendering..." + Style.RESET_ALL)
        
        # Set up optimized rendering parameters
        final_clip.write_videofile(
            output_path,
            fps=fps,
            codec='libx264',
            audio_codec='aac',
            preset='ultrafast',
            threads=8,
            bitrate='2000k',
            verbose=True,
            logger='bar'
        )
        
        print(Fore.GREEN + "\nVideo rendering complete!" + Style.RESET_ALL)
        
    except Exception as e:
        print(Fore.RED + f"\nError during video rendering: {str(e)}" + Style.RESET_ALL)
        print(Fore.YELLOW + "\nTrying alternative rendering method..." + Style.RESET_ALL)
        
        try:
            # Try with even faster settings
            final_clip.write_videofile(
                output_path,
                fps=fps,
                preset='ultrafast',
                threads=8,
                bitrate='1000k',
                verbose=True
            )
            print(Fore.GREEN + "\nVideo rendering complete using alternative method!" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"\nFailed to render video: {str(e)}" + Style.RESET_ALL)
            print(Fore.YELLOW + "\nPlease check the video file and try again." + Style.RESET_ALL)

def create_looping_video(clip, num_loops, duration, fps):
    """Create the looping video with optimized settings"""
    try:
        # Create a progress indicator
        print(Fore.YELLOW + "\nCreating video loop..." + Style.RESET_ALL)
        
        # Create the looped video
        if num_loops:
            clips = [clip] * num_loops
            final_clip = concatenate_videoclips(clips)
        else:
            # Calculate number of repeats needed
            num_repeats = int(duration / clip.duration) + 1
            clips = [clip] * num_repeats
            final_clip = concatenate_videoclips(clips)
            final_clip = final_clip.subclip(0, duration)

        # Optimize the final clip
        final_clip = final_clip.set_fps(fps)
        final_clip = final_clip.set_duration(duration)
        
        return final_clip

    except Exception as e:
        print(Fore.RED + f"\nError creating video loop: {str(e)}" + Style.RESET_ALL)
        raise

def get_valid_input(prompt, type_func, error_msg, min_value=None, max_value=None):
    while True:
        try:
            value = type_func(input(prompt))
            if min_value is not None and value < min_value:
                raise ValueError(f"Value must be at least {min_value}")
            if max_value is not None and value > max_value:
                raise ValueError(f"Value cannot exceed {max_value}")
            return value
        except ValueError as e:
            print(Fore.RED + f"{error_msg}: {str(e)}" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error getting input: {str(e)}" + Style.RESET_ALL)

def loop_video():
    try:
        print_banner()
        
        # Get video file path
        video_path = ""
        while True:
            try:
                video_path = input(Fore.GREEN + "Enter the path to the video file (right click the video file and select 'Copy path'): " + Style.RESET_ALL)
                video_path = video_path.strip('"')
                
                if validate_video_path(video_path):
                    break
                
            except KeyboardInterrupt:
                print("\n" + Fore.YELLOW + "Operation cancelled by user." + Style.RESET_ALL)
                return
            except Exception as e:
                print(Fore.RED + f"\nError processing video path: {str(e)}" + Style.RESET_ALL)

        # Ask if user wants to save the looped video
        save_choice = ""
        while True:
            try:
                save_choice = input(Fore.GREEN + "\nDo you want to save the looped video? (y/n): " + Style.RESET_ALL).lower()
                if save_choice in ['y', 'n']:
                    save_video = save_choice == 'y'
                    break
                print(Fore.RED + "Please enter 'y' or 'n'" + Style.RESET_ALL)
            except KeyboardInterrupt:
                print("\n" + Fore.YELLOW + "Operation cancelled by user." + Style.RESET_ALL)
                return
            except Exception as e:
                print(Fore.RED + f"\nError processing save choice: {str(e)}" + Style.RESET_ALL)

        # Ask for save path if saving
        save_path = None
        if save_video:
            default_save_path = os.path.dirname(video_path)
            while True:
                try:
                    save_path = input(Fore.GREEN + f"\nEnter the path where you want to save the video, press Enter for default ({default_save_path}): " + Style.RESET_ALL)
                    if save_path.strip():
                        save_path = save_path.strip('"')
                        if os.path.exists(save_path) and os.path.isdir(save_path):
                            if ensure_directory_exists(save_path):
                                break
                        print(Fore.RED + "Directory not found or invalid. Please enter a valid directory path." + Style.RESET_ALL)
                    else:
                        if ensure_directory_exists(default_save_path):
                            save_path = default_save_path
                            break
                except KeyboardInterrupt:
                    print("\n" + Fore.YELLOW + "Operation cancelled by user." + Style.RESET_ALL)
                    return
                except Exception as e:
                    print(Fore.RED + f"\nError processing save path: {str(e)}" + Style.RESET_ALL)

        try:
            # Open the video file
            clip = VideoFileClip(video_path)

            # Get video properties
            fps = clip.fps
            frame_width = int(clip.w)
            frame_height = int(clip.h)
            total_frames = int(clip.duration * fps)
            video_duration = clip.duration  # in seconds

            # Set up video writer if saving
            output_filename = os.path.splitext(os.path.basename(video_path))[0] + "_looped.mp4"
            output_path = os.path.join(save_path, output_filename)
            
            # Ensure the output directory exists
            if not ensure_directory_exists(save_path):
                print(Fore.RED + "\nFailed to create output directory. Please check permissions." + Style.RESET_ALL)
                return

            print(Fore.GREEN + f"\nOutput file will be saved as: {output_path}" + Style.RESET_ALL)

            # Ask user for playback mode
            mode = 0
            while True:
                try:
                    print(Fore.YELLOW + "\nChoose playback mode:" + Style.RESET_ALL)
                    print(Fore.YELLOW + "1. Loop for a specific number of times" + Style.RESET_ALL)
                    print(Fore.YELLOW + "2. Loop for a specific duration (in minutes)" + Style.RESET_ALL)
                    mode = int(input(Fore.GREEN + "Enter your choice (1 or 2): " + Style.RESET_ALL))
                    if mode in [1, 2]:
                        break
                    print(Fore.RED + "Please enter 1 or 2" + Style.RESET_ALL)
                except ValueError:
                    print(Fore.RED + "Please enter a number (1 or 2)" + Style.RESET_ALL)
                except KeyboardInterrupt:
                    print("\n" + Fore.YELLOW + "Operation cancelled by user." + Style.RESET_ALL)
                    return
                except Exception as e:
                    print(Fore.RED + f"\nError processing playback mode: {str(e)}" + Style.RESET_ALL)

            # Get playback parameters based on mode
            num_loops = None
            duration = None
            
            if mode == 1:
                num_loops = get_valid_input(
                    Fore.GREEN + "Enter the number of times to loop the video: " + Style.RESET_ALL,
                    int,
                    "Please enter a valid number of loops",
                    min_value=1
                )
            elif mode == 2:
                duration = get_valid_input(
                    Fore.GREEN + "Enter the duration to loop the video (in minutes): " + Style.RESET_ALL,
                    float,
                    "Please enter a valid duration in minutes",
                    min_value=0.1,
                    max_value=120  # Limit to 2 hours max
                ) * 60

            # Analyze video content to determine optimal loop points
            print(Fore.YELLOW + "\nAnalyzing video content for optimal loop points..." + Style.RESET_ALL)
            optimal_duration = analyze_video_content(video_path)
            
            if optimal_duration is None:
                print(Fore.YELLOW + "\nUsing default loop duration." + Style.RESET_ALL)
                optimal_duration = video_duration * 2  # Default to double the original duration
            else:
                print(Fore.GREEN + f"\nFound optimal loop duration: {optimal_duration:.1f} seconds" + Style.RESET_ALL)

            # Create the looped video
            final_clip = create_looping_video(clip, num_loops, duration, fps)

            # Save the video if requested
            if save_video:
                render_video(final_clip, output_path, fps)

            # Clean up
            try:
                clip.close()
                final_clip.close()
            except Exception as e:
                print(Fore.YELLOW + f"\nWarning: Error during cleanup: {str(e)}" + Style.RESET_ALL)

            print("\n" + Fore.GREEN + "Video processing complete!" + Style.RESET_ALL)

        except Exception as e:
            print(Fore.RED + f"\nAn error occurred: {str(e)}" + Style.RESET_ALL)
            print(Fore.YELLOW + "\nPlease check the video file and try again." + Style.RESET_ALL)

    except Exception as e:
        print(Fore.RED + f"\nA critical error occurred: {str(e)}" + Style.RESET_ALL)
        print(Fore.YELLOW + "\nThe program will now exit." + Style.RESET_ALL)
        sys.exit(1)

if __name__ == "__main__":
    try:
        loop_video()

    except KeyboardInterrupt:
        print("\n" + Fore.YELLOW + "Program interrupted by user." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"\nAn unexpected error occurred: {str(e)}" + Style.RESET_ALL)
        print(Fore.YELLOW + "\nPlease check the video file and try again." + Style.RESET_ALL)
