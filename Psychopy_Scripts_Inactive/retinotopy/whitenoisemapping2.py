from psychopy import visual, logging, core, filters, event, monitors
import pylab, math, random, numpy, time, imp, sys
from os import path,makedirs
sys.path.append("C:/Users/fitzlab1/Desktop/psychopy/triggers") #path to trigger classes


mon= monitors.Monitor('dualmonitors')
clock = core.Clock() 

 
myWin = visual.Window(size=[3840,1080],monitor=mon,fullscr=True,screen=1, useFBO = 'true',allowGUI=False, waitBlanking=False,blendMode='add')
stimDuration = 0.033;
fullConditions = 2000; #number of images
trialset =1

#set up natural image display
#right is contra
imageRight = visual.ImageStim(win=myWin, name='image',units='pix', pos=[-960,0], size=[1080,1080])

#collect full stimulus set
stimSet = numpy.asarray(range(0,fullConditions))
stiminfo = stimSet.flatten()

#set up spike2 triggers
#Triggering type
triggerType = 'OutOnly' # 'SerialDaqOut' OR 'OutOnly' OR 'NoTrigger'
serialPortName = 'COM2' # ignored if triggerType is "COM3"
adjustDurationToMatch2P=True
import time
dataPath='//mpfiwdtfitz68/Spike2Data/'
date = (time.strftime("%Y-%m-%d"))
logFilePath =dataPath+date+'\\'+date+'.txt' #including filepath

stimCodeName=path.dirname(path.realpath(__file__))+'\\'+path.basename(__file__)

#Set up the trigger behavior
trigger = None
if triggerType == "NoTrigger":
    import noTrigger
    trigger = noTrigger.noTrigger(None) 
elif triggerType == "SerialDaqOut" or triggerType == 'OutOnly':
    import serialTriggerDaqOut
    print 'Imported trigger serialTriggerDaqOut'
    trigger = serialTriggerDaqOut.serialTriggerDaqOut(serialPortName) 
    # determine the Next experiment file name
    #--------#
    expName=trigger.getNextExpName([dataPath,date])
    #--------#
    print "Trial name: ",expName
    if triggerType == 'OutOnly':
        trigger.readSer=False
    #Record a bunch of serial triggers and fit the stim duration to an exact multiple of the trigger time
    if adjustDurationToMatch2P:
        print "Waiting for serial Triggers"
        stimDuration = trigger.extendStimDurationToFrameEnd(stimDuration)
    # store the stimulus data and prepare the directory
    #--------#
    trigger.preTrialLogging([dataPath,date,expName,stimCodeName,stiminfo,logFilePath]) 
    #--------#
elif triggerType=="DaqIntrinsicTrigger":
    import daqIntrinsicTrigger
    trigger = daqIntrinsicTrigger.daqIntrinsicTrigger(None) 
else:
    print "Unknown trigger type", triggerType

imageRight.setAutoDraw(True)

for nTrials in range(0,1):
    clock.reset()
    for nStim in stimSet:

        Iname='C:/Users/fitzlab1/Desktop/psychopy/retinotopy/spatcloud/px_48_spatscal_10_trial_'+format(trialset)+'/im_' + '{:04.0f}'.format(nStim+1)+ '.png'
        #print nStim - worried going to slow
        trigger.preStim(nStim+1)
        imageRight.setImage(Iname)
        myWin.flip()
        trigger.postFlip(None)
        time.sleep(stimDuration)
trigger.wrapUp([logFilePath, expName])
print 'Finished all stimuli.'