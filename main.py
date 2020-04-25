import os
import sys

from PIL import Image, ExifTags
import exifread

rootDir = "/Volumes/"
volumes = []


def checkArgs():
    NONAME = True
    args = sys.argv[1:]
    if len(args) != 0:
        NONAME = False


def checkVolume(volName):
    volumes.append(volName+"/")
    return os.path.isdir(rootDir + volName)


def loopDirs():
    for volume in volumes:
        for subdir, dirs, files in os.walk(rootDir+volume+"DCIM/"):
            for file in files:
                if os.path.join(subdir, file)[-4:] == ".CR2" or os.path.join(subdir, file)[-4:] == ".MP4" or os.path.join(subdir, file)[-4:] == ".JPG":
                    path = os.path.join(subdir, file)
                    if not(len(path.split(".")) > 2):
                        #print(path)
                        f = open(path, 'rb')
                        # Return Exif tags
                        tags = exifread.process_file(f)
                        #print(tags)
                        for tag in tags.keys():
                            if tag in ('EXIF DateTimeOriginal','Image Model'):
                                print("Key: %s, value %s" % (tag, tags[tag]))
                        #img = Image.open(path)
                        #exif = {ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS}

                        #print(exif)
print(sys.version)

__init__()
checkVolume("SD64GB01")
#checkVolume("SD64GB02")
loopDirs()
