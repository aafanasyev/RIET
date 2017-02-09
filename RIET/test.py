#import os

#framesDir = "frames"
#framesExt = ".dng"

#def framesCounterInDirectory(Dir,Ext):
#      list_dir = []
#      list_dir = os.listdir(Dir)
#      count = 0
#      for file in list_dir:
#        if file.endswith(Ext):
#          count += 1
#      return int(count)
#print (framesCounterInDirectory(framesDir,framesExt))
#
#listDir = []
#dictFrame = {}
#
#for file in os.listdir(framesDir):
#    if file.endswith(framesExt):
#        pathToFrame = os.path.join(framesDir,file)
#        print (pathToFrame)
#        for i in range(0, framesCounterInDirectory(framesDir,framesExt)):
#            dictFrame[i] = pathToFrame
#            listDir.append(dictFrame.copy())
#
#print(dictFrame)
#print(listDir)

d={}
datalist=['d0', 'd1', 'd2']
dlist=[]
for key, data in datalist:
    if key in d:
        d[key].append(data)
    else:
        d[key]=data    
    print(d)
print(dlist)

