import os
import sys
import rawpy

class MainApp(object):
    def main (self):
        return (rawpy.libraw_version)

if __name__ == '__main__':
    print (MainApp().main())
