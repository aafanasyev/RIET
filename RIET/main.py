import os
import sys
import rawpy
import pyexifinfo as pyexif
import json
from operator import itemgetter

""""Configuration"""
rawFramesDir = "frames"
rawFramesExt = ".dng"
exifCreationDate = "EXIF:DateTimeOriginal"
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
    #def listFramesIn

    def listCreationDateOrderedFrames(frames_Directory, frames_Extension):
        framesPathList = []
        framesCreationDateList = []

        for file in os.listdir(frames_Directory):
            if file.endswith(frames_Extension):
                #add path to frame to the list
                pathToFrame=os.path.join(frames_Directory,file)
                framesPathList.append(pathToFrame)
                #Read Frame Creation Date and add to the List
                exifData = pyexif.get_json(pathToFrame)
                encodedSortedJSONExifData = json.dumps( exifData, sort_keys=True, indent=4, separators=(',', ': '))
                decodedSortedJSONExifData = json.loads(encodedSortedJSONExifData)
                frameCreationDate = decodedSortedJSONExifData[0][exifCreationDate]
                framesCreationDateList.append (frameCreationDate)
        # merge lists to a dictionary and sort using json
        framesCreationDate_PathToFrameDict = dict(zip(framesCreationDateList, framesPathList))
        framesCreationDate_PathToFrameDictSorted = json.dumps( framesCreationDate_PathToFrameDict, sort_keys=True, indent=4, separators=(',', ': '))
        return framesCreationDate_PathToFrameDictSorted

#get frame
    def getEncodedJSONSortedFramesList(framesList):
        getDecodedJSONSortedFrameList = json.loads(framesList)
#get frames from json, sort it, read image RGB matrix, read green values, write.
        valuesList = []
        for key in sorted(getDecodedJSONSortedFrameList):
            #print (getDecodedJSONSortedFrameList[key])
            valuesList.append(getDecodedJSONSortedFrameList[key])
            raw = rawpy.imread(getDecodedJSONSortedFrameList[key])
#convert Bayer pattern in to a list:
            #print ("Bayer pattern:\n",raw.raw_pattern)
            bayerRawPatternList = []
            for i in range(0, len(raw.raw_pattern)):
                for n in range(0, len(raw.raw_pattern[i])):
                    bayerRawPatternList.append(raw.raw_pattern[i][n])
            #print(bayerRawPatternList)
#convert Bayer pattern and color description in to Dictionary
            bayerColorDescList = list(raw.color_desc.decode("utf-8"))
            #print ("Indices 0,1,2,3: ", bayerColorDescList)
            rawBayerPatternColorDic = dict(zip(bayerRawPatternList, bayerColorDescList))
            print (rawBayerPatternColorDic.value('G'))
# read pixel data of an image and save it in a binary file
            print ("Height of the image:",raw.sizes[0],"\nWidth of the image:",raw.sizes[1])
            for column in range(0, raw.sizes[0]):
                for row in range(0, raw.sizes[1]):
                    pass
                    #if ( raw.raw_color(row, column) = rawBayerPatternColorDic.value
                    #print (raw.raw_value(column, row))          
#
        return valuesList

if __name__ == '__main__':

#    print (MainApp().main())
#    pathToFrame = MainApp.listFramesDirectory(rawFramesDir,rawFramesExt)[0] 
#    print (pathToFrame)

#print dictionary with key as creation data of an image and value path to this image.

    listOfOrderedFrames = MainApp.listCreationDateOrderedFrames(rawFramesDir,rawFramesExt)
    print(listOfOrderedFrames)
    rawImagesPixelsData = MainApp.getEncodedJSONSortedFramesList(listOfOrderedFrames)
    print(rawImagesPixelsData)



    #print (fileType(MainApp.listFramesDirectory(rawFramesDir,rawFramesExt)[0]))

