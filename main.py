import yt_dlp
import tkinter as tk
from tkinter import filedialog

ydl_opts = {}


def download_video(url, path):
    ydl_opts['outtmpl'] = path + '/%(title)s.%(ext)s'

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f'Selected folder: {folder}')

    return folder


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    print('#' * 50)
    print('{:=^50}'.format(' Youtube Video Downloader '))
    print('#' * 50)

    video_url = input("URL: ")
    save_path = open_file_dialog()

    if save_path:
        download_video(video_url, save_path)
    else:
        print('No folder selected')
