# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 08:52:40 2016

@author: wilsond
"""


from psychopy import visual, logging, core, filters, event, monitors
import pylab, math, random, time, imp, sys
sys.path.append("C:/Users/fitzlab1/Desktop/psychopy/triggers") #path to trigger classes
import numpy as np
from os import path
import matplotlib.pyplot as plt
print "initialized"
np.set_printoptions(threshold='nan')
#---------- Stimulus Description ---------- #
'''Flashes grid squares''' 
#---------- Monitor Properties ----------#v
mon= monitors.Monitor('projector') #gets the calibration for stimMonitor
#---------- Constants --------------#
#emissionRes = .342 # camera pixels per um at 1x1 binning
#excitationRes = .2# monitor pixels per um

#---------- Parameters----------#
nTrials=1# runs forever!
doBlank = 1 #0 for no blank stim, 1 to have a blank stim. The blank will have the highest stimcode.
nBlank=1; # number of blanks to show per trial.
stimDuration =10000 # length of time each dot appears in seconds
isi = 0 # length of inter stimulus interval in seconds
winSize =10# window size in pixels
spotSize  =1# size of illumination spot in pixels->> 20 pix is ~100um
power = 1  # power of light spot, ranges from -1 to 1
initialDelay = 5 # initial delay in seconds    


 #Create window where we can draw stimuli
myWin = visual.Window(size=(winSize,winSize),pos=(0,0),monitor=mon,fullscr=True,screen=2, allowGUI=False, waitBlanking=True)
myWin.color = [-1, -1 ,-1] # make it black
 #Initialize Rect stim
boxStim = visual.Rect(win=myWin, units='pix', size=spotSize, pos=(0,0), lineColor = [0,0,0], lineWidth=0, fillColor = 'white')
boxStim.setAutoDraw(True)
 #create instance of clock object to use as timer
clock = core.Clock()

if initialDelay>0:
    print" waiting "+str(initialDelay)+ " seconds before starting stim to let system relax after flash"
    boxStim.setContrast(0)
    while clock.getTime()<initialDelay:
        myWin.flip()
        clock.reset()
    while clock.getTime()<stimDuration:
        boxStim.setContrast(power);
        trigger.preFlip(None)
        myWin.flip()
        trigger.postFlip(None)
