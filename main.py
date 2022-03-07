import os
import subprocess
import time

def set_wallpaper(imagefilename):
    path = os.getcwd() + "/" + imagefilename
    command = "gsettings set org.gnome.desktop.background picture-uri file:" + path
    os.system(command)


os.chdir("/home/jovan/Documents/PythonProjects/WallpaperChanger/CarImages")

list_command = "ls > filenames.txt"
subprocess.call(list_command, shell = True)
filenames = open("filenames.txt", "r")
filelist = filenames.readlines()

while True:
    for imagefile in filelist:
        imagefile = imagefile[:-1]
        if imagefile.endswith(".jpg"):
            set_wallpaper(imagefile)
            time.sleep(45)
