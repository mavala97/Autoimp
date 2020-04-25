import os
import sys
import datetime
import shutil

ROOT_PATHS = ["/Volumes/SD64GB01","/Volumes/SD64GB02","/Volumes/MICR16GB01","/Volumes/GOPROSD16"]
PROJECT_FOLDER = "/Volumes/Samsung T5/Video/Projects"
EXTENSION_LIST = [".CR2", ".WAV", ".MP4", ".JPG"]
TYPE_LIST = ["Photo", "Audio", "Video", "Photo"]
PROJECT_NAME = "newProject"


def getName():
    args = sys.argv[1:]
    if len(args) != 0:
        name = args[0]
        return name
    else:
        return PROJECT_NAME


def fileFinder(rootPath, extensionList):
    filePaths = []
    for r, d, f in os.walk(rootPath):
        for file in f:
            for ex in extensionList:
                if ex in file[-6:]:
                    filePaths.append(os.path.join(r, file))
    return filePaths


def creation_date(path):
    date = datetime.datetime.fromtimestamp(os.path.getctime(path))
    return date


def fileType(path):
    if path[-4:] in EXTENSION_LIST:
        index = EXTENSION_LIST.index(path[-4:])
        return TYPE_LIST[index]
    print("So sorry, we did not find a type for your file with the extension: " + str(path[-4:]))


def createFileObjects(path):
    return [path, fileType(path), creation_date(path)]


def createFileList():
    rootPath = findRootpath()
    filePaths = fileFinder(rootPath, EXTENSION_LIST)
    files = []
    for path in filePaths:
        file = createFileObjects(path)
        files.append(file)
    return files


def findRootpath():
    for rootPath in ROOT_PATHS:
        if os.path.isdir(rootPath):
            return rootPath
    print("Sorry, volume not found")


def organise(files):
    if not files:
        print("no files to import")
        return []

    year = creation_date(files[0][0]).year
    projectName = getName()

    #Making directories
    if os.path.isdir(PROJECT_FOLDER + "/" + str(year)):
        if not os.path.isdir(PROJECT_FOLDER + "/" + str(year) + "/" + str(projectName)):
            os.mkdir(PROJECT_FOLDER + "/" + str(year) + "/" + str(projectName))
    else:
        os.mkdir(PROJECT_FOLDER + "/" + str(year))
        os.mkdir(PROJECT_FOLDER + "/" + str(year) + "/" + str(projectName))

    for f in files:
        if os.path.isdir(PROJECT_FOLDER + "/" + str(year) + "/" + str(projectName) + "/" + f[-2]):
            shutil.move(f[0], PROJECT_FOLDER + "/" + str(year) + "/" + str(projectName) + "/" + f[-2] +"/"+ f[0].split('/')[-1])
        else:
            os.mkdir(PROJECT_FOLDER + "/" + str(year) + "/" + str(projectName) + "/" + f[-2])
            shutil.move(f[0], PROJECT_FOLDER + "/" + str(year) + "/" + str(projectName) + "/" + f[-2] +"/" + f[0].split('/')[-1])


l = createFileList()
organise(l)
