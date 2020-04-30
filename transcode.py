import os
import shutil
import sys
import subprocess
import autoImp as ai

def pathFormatter(path):
    formattedPath = "\ ".join(path.split(" "))
    return formattedPath

SCREEN_FOLDER = "/Users/maxvanlaarhoven/Documents/Screenshots/"
STORAGE_FOLDER = "/Volumes/Samsung T5/Video/ScreenRecStorage/"

fileList = ai.fileFinder(SCREEN_FOLDER, [".mov"])

for file in fileList:
    inputFile = pathFormatter(file)
    outputFile = "Screenshots/Export".join(str(inputFile[:-4]+".mp4").split("Screenshots"))
    command = "HandBrakeCLI --preset-import-file /Users/maxvanlaarhoven/Documents/Screenshots/ScreenRec.json -Z "+'"ScreenRec"'+" -i "+inputFile+" -o "+outputFile
    subprocess.call(command, shell=True)
    shutil.move(file,STORAGE_FOLDER)

path = "/Users/maxvanlaarhoven/Documents/Screenshots/Screen Recording 2020-04-26 at 13.16.09.mov"
print(pathFormatter(path))
