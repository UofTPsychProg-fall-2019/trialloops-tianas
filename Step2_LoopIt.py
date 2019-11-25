#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build a trial loop Step 2
Use this template to turn Step 1 into a loop
@author: katherineduncan
"""

#%% your loop here
# start by copying your one trial here, then identify what needs to be
# changed on every trial.  Likely your stimuli, but you might want to change a few things

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'experiment'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/tianasimovic/Desktop/experiment/experiment.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='In this trial, you will hear instructions. Perform the instructed task by dragging and dropping the object into its appropriate bin.\n\nPress the SPACE BAR once the action is completed.\n\n\nPress the SPACE BAR to begin.',
    font='helvetica',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
start = keyboard.Keyboard()

# Initialize components for Routine "sentence1"
sentence1Clock = core.Clock()
grid1 = visual.ImageStim(
    win=win,
    name='grid1', 
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
arugula1 = visual.ImageStim(
    win=win,
    name='arugula1', 
    image='/Users/tianasimovic/Desktop/experiment/stimuli/trial1s1/arugula.png', mask=None,
    ori=0, pos=(-0.124, -0.27), size=(0.24, 0.26),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
thicktriangle1 = visual.ImageStim(
    win=win,
    name='thicktriangle1', 
    image='/Users/tianasimovic/Desktop/experiment/stimuli/trial1s1/thicktriangle.png', mask=None,
    ori=0, pos=(0.124, 0.01), size=(0.24, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
thintriangle1 = visual.ImageStim(
    win=win,
    name='thintriangle1', 
    image='/Users/tianasimovic/Desktop/experiment/stimuli/trial1s1/thintriangle.png', mask=None,
    ori=0, pos=(-0.371, 0.01), size=(0.24, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
fortunecookie1 = visual.ImageStim(
    win=win,
    name='fortunecookie1', 
    image='/Users/tianasimovic/Desktop/experiment/stimuli/trial1s1/fortunecookie.png', mask=None,
    ori=0, pos=(-0.358, 0.26), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
ducky1 = visual.ImageStim(
    win=win,
    name='ducky1', 
    image='/Users/tianasimovic/Desktop/experiment/stimuli/trial1s1/ducky.png', mask=None,
    ori=0, pos=(-.112, 0.26), size=(0.33, 0.33),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
duckyhat1 = visual.ImageStim(
    win=win,
    name='duckyhat1', 
    image='/Users/tianasimovic/Desktop/experiment/stimuli/trial1s1/duckyhat.png', mask=None,
    ori=0, pos=(0.371, 0.26), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
S1 = sound.Sound('/Users/tianasimovic/Desktop/experiment/stimuli/audio/triangle_S1.ogg', secs=-1, stereo=True, hamming=True,
    name='S1')
S1.setVolume(1)
myPics = [thintriangle1]


key_resp = keyboard.Keyboard()

# Initialize components for Routine "sentence2"
sentence2Clock = core.Clock()
grid2 = visual.ImageStim(
    win=win,
    name='grid2', 
    image='/Users/tianasimovic/Desktop/experiment/stimuli/trial1s2/grid', mask=None,
    ori=0, pos=(0, 0), size=(1, .8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()
arugula2 = visual.ImageStim(
    win=win,
    name='arugula2', 
    image='/Users/tianasimovic/Desktop/experiment/stimuli/trial1s2/arugula.png', mask=None,
    ori=0, pos=(-0.124, -0.27), size=(0.24, 0.26),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
thicktriangle2 = visual.ImageStim(
    win=win,
    name='thicktriangle2', 
    image='/Users/tianasimovic/Desktop/experiment/stimuli/trial1s2/thicktriangle.png', mask=None,
    ori=0, pos=(0.124, 0.01), size=(0.24, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
thintriangle2 = visual.ImageStim(
    win=win,
    name='thintriangle2', 
    image='/Users/tianasimovic/Desktop/experiment/stimuli/trial1s2/thintriangle.png', mask=None,
    ori=0, pos=(0.371, 0.01), size=(0.24, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
fortunecookie2 = visual.ImageStim(
    win=win,
    name='fortunecookie2', 
    image='/Users/tianasimovic/Desktop/experiment/stimuli/trial1s2/fortunecookie.png', mask=None,
    ori=0, pos=(-0.358, 0.26), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
ducky2 = visual.ImageStim(
    win=win,
    name='ducky2', 
    image='/Users/tianasimovic/Desktop/experiment/stimuli/trial1s2/ducky.png', mask=None,
    ori=0, pos=(-.112, 0.26), size=(0.33, 0.33),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
duckyhat2 = visual.ImageStim(
    win=win,
    name='duckyhat2', 
    image='/Users/tianasimovic/Desktop/experiment/stimuli/trial1s2/duckyhat.png', mask=None,
    ori=0, pos=(0.371, 0.26), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
myPics = [thintriangle1, thintriangle2]
S2 = sound.Sound('/Users/tianasimovic/Desktop/experiment/stimuli/audio/triangle_S2.ogg', secs=-1, stereo=True, hamming=True,
    name='S2')
S2.setVolume(1)
key_resp_2 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructions"-------
# update component parameters for each repeat
start.keys = []
start.rt = []
# keep track of which components have finished
InstructionsComponents = [text, start]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *start* updates
    waitOnFlip = False
    if start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start.frameNStart = frameN  # exact frame index
        start.tStart = t  # local t and not account for scr refresh
        start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start, 'tStartRefresh')  # time at next scr refresh
        start.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(start.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if start.status == STARTED and not waitOnFlip:
        theseKeys = start.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "sentence1"-------
# update component parameters for each repeat
grid1.setOpacity(1)
grid1.setPos((0, 0))
grid1.setSize((1, .8))
grid1.setOri(0)
grid1.setImage('/Users/tianasimovic/Desktop/experiment/stimuli/trial1s1/grid.jpg')
# setup some python lists for storing info about the mouse
gotValidClick = False  # until a click is received
S1.setSound('/Users/tianasimovic/Desktop/experiment/stimuli/audio/triangle_S1.ogg', hamming=True)
S1.setVolume(1, log=False)
key_resp.keys = []
key_resp.rt = []
# keep track of which components have finished
sentence1Components = [grid1, mouse, arugula1, thicktriangle1, thintriangle1, fortunecookie1, ducky1, duckyhat1, S1, key_resp]
for thisComponent in sentence1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
sentence1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "sentence1"-------
while continueRoutine:
    # get current time
    t = sentence1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=sentence1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *grid1* updates
    if grid1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        grid1.frameNStart = frameN  # exact frame index
        grid1.tStart = t  # local t and not account for scr refresh
        grid1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(grid1, 'tStartRefresh')  # time at next scr refresh
        grid1.setAutoDraw(True)
    
    # *arugula1* updates
    if arugula1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        arugula1.frameNStart = frameN  # exact frame index
        arugula1.tStart = t  # local t and not account for scr refresh
        arugula1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(arugula1, 'tStartRefresh')  # time at next scr refresh
        arugula1.setAutoDraw(True)
    
    # *thicktriangle1* updates
    if thicktriangle1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        thicktriangle1.frameNStart = frameN  # exact frame index
        thicktriangle1.tStart = t  # local t and not account for scr refresh
        thicktriangle1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thicktriangle1, 'tStartRefresh')  # time at next scr refresh
        thicktriangle1.setAutoDraw(True)
    
    # *thintriangle1* updates
    if thintriangle1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        thintriangle1.frameNStart = frameN  # exact frame index
        thintriangle1.tStart = t  # local t and not account for scr refresh
        thintriangle1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thintriangle1, 'tStartRefresh')  # time at next scr refresh
        thintriangle1.setAutoDraw(True)
    
    # *fortunecookie1* updates
    if fortunecookie1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        fortunecookie1.frameNStart = frameN  # exact frame index
        fortunecookie1.tStart = t  # local t and not account for scr refresh
        fortunecookie1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fortunecookie1, 'tStartRefresh')  # time at next scr refresh
        fortunecookie1.setAutoDraw(True)
    
    # *ducky1* updates
    if ducky1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        ducky1.frameNStart = frameN  # exact frame index
        ducky1.tStart = t  # local t and not account for scr refresh
        ducky1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ducky1, 'tStartRefresh')  # time at next scr refresh
        ducky1.setAutoDraw(True)
    
    # *duckyhat1* updates
    if duckyhat1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        duckyhat1.frameNStart = frameN  # exact frame index
        duckyhat1.tStart = t  # local t and not account for scr refresh
        duckyhat1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(duckyhat1, 'tStartRefresh')  # time at next scr refresh
        duckyhat1.setAutoDraw(True)
    # start/stop S1
    if S1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        S1.frameNStart = frameN  # exact frame index
        S1.tStart = t  # local t and not account for scr refresh
        S1.tStartRefresh = tThisFlipGlobal  # on global time
        S1.play(when=win)  # sync with win flip
    for pic in myPics:
        if mouse.isPressedIn(pic):
            pic.pos = mouse.getPos() 
    
    # *key_resp* updates
    if key_resp.status == NOT_STARTED and t >= 0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
    if key_resp.status == STARTED:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in sentence1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "sentence1"-------
for thisComponent in sentence1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('grid1.started', grid1.tStartRefresh)
thisExp.addData('grid1.stopped', grid1.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse.getPos()
buttons = mouse.getPressed()
thisExp.addData('mouse.x', x)
thisExp.addData('mouse.y', y)
thisExp.addData('mouse.leftButton', buttons[0])
thisExp.addData('mouse.midButton', buttons[1])
thisExp.addData('mouse.rightButton', buttons[2])
thisExp.addData('mouse.started', mouse.tStart)
thisExp.addData('mouse.stopped', mouse.tStop)
thisExp.nextEntry()
thisExp.addData('arugula1.started', arugula1.tStartRefresh)
thisExp.addData('arugula1.stopped', arugula1.tStopRefresh)
thisExp.addData('thicktriangle1.started', thicktriangle1.tStartRefresh)
thisExp.addData('thicktriangle1.stopped', thicktriangle1.tStopRefresh)
thisExp.addData('thintriangle1.started', thintriangle1.tStartRefresh)
thisExp.addData('thintriangle1.stopped', thintriangle1.tStopRefresh)
thisExp.addData('fortunecookie1.started', fortunecookie1.tStartRefresh)
thisExp.addData('fortunecookie1.stopped', fortunecookie1.tStopRefresh)
thisExp.addData('ducky1.started', ducky1.tStartRefresh)
thisExp.addData('ducky1.stopped', ducky1.tStopRefresh)
thisExp.addData('duckyhat1.started', duckyhat1.tStartRefresh)
thisExp.addData('duckyhat1.stopped', duckyhat1.tStopRefresh)
S1.stop()  # ensure sound has stopped at end of routine
thisExp.addData('S1.started', S1.tStartRefresh)
thisExp.addData('S1.stopped', S1.tStopRefresh)
# the Routine "sentence1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=3, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions.xlsx', selection='0:2'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "sentence2"-------
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_2
    gotValidClick = False  # until a click is received
    S2.setSound('/Users/tianasimovic/Desktop/experiment/stimuli/audio/triangle_S2.ogg', hamming=True)
    S2.setVolume(1, log=False)
    key_resp_2.keys = []
    key_resp_2.rt = []
    # keep track of which components have finished
    sentence2Components = [grid2, mouse_2, arugula2, thicktriangle2, thintriangle2, fortunecookie2, ducky2, duckyhat2, S2, key_resp_2]
    for thisComponent in sentence2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    sentence2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "sentence2"-------
    while continueRoutine:
        # get current time
        t = sentence2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=sentence2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *grid2* updates
        if grid2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            grid2.frameNStart = frameN  # exact frame index
            grid2.tStart = t  # local t and not account for scr refresh
            grid2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(grid2, 'tStartRefresh')  # time at next scr refresh
            grid2.setAutoDraw(True)
        
        # *arugula2* updates
        if arugula2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            arugula2.frameNStart = frameN  # exact frame index
            arugula2.tStart = t  # local t and not account for scr refresh
            arugula2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(arugula2, 'tStartRefresh')  # time at next scr refresh
            arugula2.setAutoDraw(True)
        
        # *thicktriangle2* updates
        if thicktriangle2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            thicktriangle2.frameNStart = frameN  # exact frame index
            thicktriangle2.tStart = t  # local t and not account for scr refresh
            thicktriangle2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(thicktriangle2, 'tStartRefresh')  # time at next scr refresh
            thicktriangle2.setAutoDraw(True)
        
        # *thintriangle2* updates
        if thintriangle2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            thintriangle2.frameNStart = frameN  # exact frame index
            thintriangle2.tStart = t  # local t and not account for scr refresh
            thintriangle2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(thintriangle2, 'tStartRefresh')  # time at next scr refresh
            thintriangle2.setAutoDraw(True)
        
        # *fortunecookie2* updates
        if fortunecookie2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fortunecookie2.frameNStart = frameN  # exact frame index
            fortunecookie2.tStart = t  # local t and not account for scr refresh
            fortunecookie2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fortunecookie2, 'tStartRefresh')  # time at next scr refresh
            fortunecookie2.setAutoDraw(True)
        
        # *ducky2* updates
        if ducky2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ducky2.frameNStart = frameN  # exact frame index
            ducky2.tStart = t  # local t and not account for scr refresh
            ducky2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ducky2, 'tStartRefresh')  # time at next scr refresh
            ducky2.setAutoDraw(True)
        
        # *duckyhat2* updates
        if duckyhat2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            duckyhat2.frameNStart = frameN  # exact frame index
            duckyhat2.tStart = t  # local t and not account for scr refresh
            duckyhat2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(duckyhat2, 'tStartRefresh')  # time at next scr refresh
            duckyhat2.setAutoDraw(True)
        for pic in myPics:
            if mouse.isPressedIn(pic):
                pic.pos = mouse.getPos() 
        # start/stop S2
        if S2.status == NOT_STARTED and tThisFlip >= 0.4-frameTolerance:
            # keep track of start time/frame for later
            S2.frameNStart = frameN  # exact frame index
            S2.tStart = t  # local t and not account for scr refresh
            S2.tStartRefresh = tThisFlipGlobal  # on global time
            S2.play(when=win)  # sync with win flip
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sentence2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "sentence2"-------
    for thisComponent in sentence2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('grid2.started', grid2.tStartRefresh)
    trials.addData('grid2.stopped', grid2.tStopRefresh)
    # store data for trials (TrialHandler)
    x, y = mouse_2.getPos()
    buttons = mouse_2.getPressed()
    trials.addData('mouse_2.x', x)
    trials.addData('mouse_2.y', y)
    trials.addData('mouse_2.leftButton', buttons[0])
    trials.addData('mouse_2.midButton', buttons[1])
    trials.addData('mouse_2.rightButton', buttons[2])
    trials.addData('mouse_2.started', mouse_2.tStart)
    trials.addData('mouse_2.stopped', mouse_2.tStop)
    trials.addData('arugula2.started', arugula2.tStartRefresh)
    trials.addData('arugula2.stopped', arugula2.tStopRefresh)
    trials.addData('thicktriangle2.started', thicktriangle2.tStartRefresh)
    trials.addData('thicktriangle2.stopped', thicktriangle2.tStopRefresh)
    trials.addData('thintriangle2.started', thintriangle2.tStartRefresh)
    trials.addData('thintriangle2.stopped', thintriangle2.tStopRefresh)
    trials.addData('fortunecookie2.started', fortunecookie2.tStartRefresh)
    trials.addData('fortunecookie2.stopped', fortunecookie2.tStopRefresh)
    trials.addData('ducky2.started', ducky2.tStartRefresh)
    trials.addData('ducky2.stopped', ducky2.tStopRefresh)
    trials.addData('duckyhat2.started', duckyhat2.tStartRefresh)
    trials.addData('duckyhat2.stopped', duckyhat2.tStopRefresh)
    S2.stop()  # ensure sound has stopped at end of routine
    trials.addData('S2.started', S2.tStartRefresh)
    trials.addData('S2.stopped', S2.tStopRefresh)
    # the Routine "sentence2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 3 repeats of 'trials'


# make a list or a pd.DataFrame that contains trial-specific info (stimulus, etc)
# e.g. stim = ['1.jpg','2.jpg','3.jpg']

bin3 = sound.Sound('/Users/tianasimovic/Desktop/experiment/stimuli/audio/bin3.ogg')
bin9 = sound.Sound('/Users/tianasimovic/Desktop/experiment/stimuli/audio/bin9.ogg')
bin11 = sound.Sound('/Users/tianasimovic/Desktop/experiment/stimuli/audio/bin11.ogg')

stim = ['bin3', 'bin9', 'bin11']
np.random.shuffle(bins)


# make your loop

# define a list of sound files:
stim = ['audio/bin3.ogg','audio/bin9.ogg','audio/bin11.ogg']
shuffle(stim)

audio = sound.Sound() # create a sound object for playing later

for t in stim:
	if trials.thisN in range(0:3):
    		current_sound = stim.pop()
    		audio.setSound(current_sound) # update the sound object with it
    		audio.play()

win = visual.Window()
win.flip()
nextFlip = win.getFutureFlipTime(

# on every trial, record the sound name in the data file:
thisExp('stim', current_sound)


# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()
