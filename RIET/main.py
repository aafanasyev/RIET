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

    def listFramesDirectory(frames_Directory, frames_Extension):
        framesList = []
        for root, dirs, files in os.walk(frames_Directory):
            for file in files:
                if file.endswith(frames_Extension):
                    framesList.append(os.path.join(root,file))
        return framesList

if __name__ == '__main__':
    print (MainApp().main())
    pathToFrame = MainApp.listFramesDirectory(rawFramesDir,rawFramesExt)[0] 
    print (pathToFrame)
    print (pyexif.ver())
    exifData = pyexif.get_json(pathToFrame)
    print (json.dumps( exifData, sort_keys=True, indent=4, separators=(',', ': ')) )

    #print (fileType(MainApp.listFramesDirectory(rawFramesDir,rawFramesExt)[0]))

