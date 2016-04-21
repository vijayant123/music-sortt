#!/usr/bin/python

import subprocess
from os import listdir
import os, sys
from os.path import isfile, join
from pygame import mixer

mypath = "/home/error-404/Desktop/songs"
savepath = "/home/error-404/Desktop/dance"
altpath = "/home/error-404/Desktop/others"

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

mixer.init()

flag = 0

for f in onlyfiles:
    print f
    mixer.music.load(join(mypath,f))
    mixer.music.play(0, 40)
    while True:
        a = raw_input()
        if(a == 'q'):
            sys.exit(0)
        elif(a >= '0' and a <= '9'):
            mixer.music.rewind()
            mixer.music.play(0, int(a)*10)
        elif(a == ''):
            mixer.music.stop()
            os.rename(join(mypath, f), join(altpath, f))
            break;
        elif(a == '/'):
            # t'is the chosen ONE!
            # move it to a secure location
            mixer.music.stop()
            os.rename(join(mypath, f), join(savepath, f))
            break;
        elif(a == 'p'):
            if(flag == 0):
                mixer.music.pause()
                flag = 1
            else:
                mixer.music.unpause()
                flag = 0

