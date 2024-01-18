import tkinter as tk
import vlc

# Create the main window
root = tk.Tk()
root.title("Video Player")
root.geometry("800x600")
# Create a vlc instance
instance = vlc.Instance("--no-xlib")
player = None

# Define a function to open and play a video file
def play_video():
    global player
    if player is not None:
        player.stop()
        player.release()

    media = instance.media_new(file_path)
    player = instance.media_player_new()
    player.set_media(media)

    # Embed the video player in the Tkinter window
    player.set_hwnd(video_frame.winfo_id())

    # Play the video
    player.play()


# Define a function to play the video
def play_pause_video():
    if player is not None:
        if player.get_state() == vlc.State.Paused:
            player.play()
        elif player.get_state() == vlc.State.Playing:
            player.pause()

# Define a function to open a video file
def open_file():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.avi *.mkv")])
    if file_path:
        play_video()

# Create a frame to hold the video player
video_frame = tk.Frame(root)
video_frame.pack(fill=tk.BOTH, expand=True)

# Create a button to open a video file
open_button = tk.Button(root, text="Open Video", command=open_file)
open_button.pack(pady=10)


# Create a button to play/pause the video
play_pause_button = tk.Button(root, text="Play/Pause Video", command=play_pause_video)
play_pause_button.pack(pady=10)

# Import filedialog for opening files
from tkinter import filedialog

# Run the main event loop
root.mainloop()
