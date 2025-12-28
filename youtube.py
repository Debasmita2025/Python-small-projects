import yt_dlp
import tkinter as tk
from tkinter import filedialog, messagebox
import os

def download_audio(url, save_path):
    try:
        ydl_opts = {
            'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        messagebox.showinfo("Success", "Audio downloaded successfully!")
        
    except Exception as e:
        messagebox.showerror("Error", f"Download failed: {str(e)}")

def open_file_dialog():
    folder = filedialog.askdirectory(title="Select Download Folder")
    
    if folder:
        print(f"Selected folder: {folder}")
        return folder
    return None

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    
    video_url = input("Please enter a YouTube URL: ").strip()
    
    if not video_url:
        print("No URL provided")
        exit()
    
    save_dir = open_file_dialog()
    
    if save_dir:
        print("Starting download...")
        download_audio(video_url, save_dir)
    else:
        print("No save location selected")
