import os
rawFramesDir = "frames"
rawFramesExt = ".dng"

def listOfFrames(framesDir, framesExt):
        for root, dirs, files in os.walk(framesDir):
            for file in files:
                if file.endswith(framesExt):
                     return(os.path.join(root, file))

print(listOfFrames(rawFramesDir, rawFramesExt))