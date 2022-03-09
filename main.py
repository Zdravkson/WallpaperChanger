#!/bin/env python3
import os
import subprocess
import time

WALLPAPER_DIRECTORY = "/home/jovan/Documents/PythonProjects/WallpaperChanger/CarImages"
SLEEP_TIME = 10
COMMAND = "gsettings set org.gnome.desktop.background picture-uri file:"


def set_wallpaper(imagefilename):
    path = imagefilename
    command = COMMAND + path
    print(command)
    os.system(command)


def get_images():
    for root, _, files in os.walk(WALLPAPER_DIRECTORY):
        return [
            os.path.join(root, filename)
            for filename in files
            if filename.endswith(".jpg")
        ]


if __name__ == "__main__":
    images = get_images()

    while True:
        for image in images:
            set_wallpaper(image)
            time.sleep(SLEEP_TIME)
