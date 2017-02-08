import os
import sys
import rawpy
import pyexifinfo as pyexif
import json

""""Configuration"""
rawFramesDir = "frames"
rawFramesExt = ".dng"
#framesList = []

"""Parse raw format frames"""

#class parser:
#    raw_frames = 'frames/'
    

"""Process frames"""

"""Display results"""

class MainApp(object):
    def main (self):
        return (rawpy.libraw_version)


# prints list of extention binded frames in a directory
    def listFramesDirectory(frames_Directory, frames_Extension):
        framesList = []
        for root, dirs, files in os.walk(frames_Directory):
            for file in files:
                if file.endswith(frames_Extension):
                    framesList.append(os.path.join(root,file))
        return framesList

#count number of files in a directory:
    def framesCounterInDirectory(frames_Directory,frames_Extension):
      list_dir = []
      list_dir = os.listdir(frames_Directory)
      count = 0
      for file in list_dir:
        if file.endswith(frames_Extension):
          count += 1
      return count

# prints a list with element consisting of a dictionary key (creation data) and dictionary value (path to frame)

    def listCreationDateOrderedFrames(frames_Directory, frames_Extension):
        creationDateAndPathOfFrameDict= {}
        unorderedByCreationDateFramesList = []
        for root, dirs, files in os.walk(frames_Directory):
            for file in files:
                if file.endswith(frames_Extension):
                    for i in xrange(0, framesCounterInDirectory):
                        pathToFrame=os.path.join(root,file)
                        exifData = pyexif.get_json(pathToFrame)
                        jsonEncodedSortedExifData = json.dumps( exifData, sort_keys=True, indent=4, separators=(',', ': '))
                        jsonDecodedSortedExifData = json.loads(jsonEncodedSortedExifData)
                        DateOfCreation = jsonDecodedSortedExifData[0]["EXIF:DateTimeOriginal"]
                        creationDateAndPathOfFrameDict[DateOfCreation] = pathToFrame
                        unorderedByCreationDateFramesList.append(creationDateAndPathOfFrameDict.copy())
        return unorderedByCreationDateFramesList  

if __name__ == '__main__':

#    print (MainApp().main())
#    pathToFrame = MainApp.listFramesDirectory(rawFramesDir,rawFramesExt)[0] 
#    print (pathToFrame)
#    exifData = pyexif.get_json(pathToFrame)
#    jsonEncodedSortedExifData = json.dumps( exifData, sort_keys=True, indent=4, separators=(',', ': '))
#    jsonDecodedSortedExifData = json.loads(jsonEncodedSortedExifData)
#    print (jsonDecodedSortedExifData[0]["EXIF:DateTimeOriginal"])
#    print (jsonEncodedSortedExifData)
#    "XMP:DateCreated": "2013:10:21 14:55:26"

#print dictionary with key as creation data of an image and value path to this image.

    listOfFrames = MainApp.listCreationDateOrderedFrames(rawFramesDir,rawFramesExt)
    print(listOfFrames) 


    #print (fileType(MainApp.listFramesDirectory(rawFramesDir,rawFramesExt)[0]))

