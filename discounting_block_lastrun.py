#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.2),
    on Март 22, 2021, at 18:39
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.2'
expName = 'discounting_block'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\preprocess\\Documents\\Новая\\mnm_experiment-main\\discounting_block_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
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

# Initialize components for Routine "language"
languageClock = core.Clock()
lan_choose = keyboard.Keyboard()
language_text = visual.TextStim(win=win, name='language_text',
    text='Добро пожаловать, уважаемый участник!\nWelcome dear participant!\n\nДля русскоязычной версии нажмите "1"\nFor English language press "2"',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

if (lan_choose.keys == '1'):
        #defining russian language
    text1= 1
    text2= 2
    text3= 3
    text4= 4
    text6= 5
    text7= "total gain:"
    text8= "You are in level"
    text9= "press space to continue"
    text10 = 6
    text11 = 7
    textopt1= "for 67%"
    textopt2= "for 100%"
    textchance0 = "You did not get it!"
    textchance1 = "You got it!"
    
else:
    text1 = "Welcome dear participants\n\nThis game is about collecting as much M&Ms as you can!\n\nEach time you must choose from two options with different probability and waiting time. The exact amount and probability for each option is written on the screen.\n\nEven if you are confused now, take it easy and try to play. It will get to you.\n\nPress 'space' to play it a bit for yourself.."
    text2 = 'Please wait, you are expriencing the waiting duration!'
    text3 = "You had exprienced the waiting duration!\n\nPlease press 'space' to start choosing again."
    text4 = "(to choose this option press 1)            (To choose this option press 2)"
    text6 = "You saw how easy it was?! \n\n Have you noticed the amount of waiting duration that was different for small and large M&Ms? \n\n Their waiting duration will be presented at the beginning of the each 4 blocks of the game. \n\n You should know that you cannot increase the number of rounds by choosing the faster rewards. \n\n One more thing, for every 200 points you earn one hidden reward!  \n\n Press space to play the game for real!"
    text7 = "\n \ntotal gain:"
    text8 = "\n \nYou are in level"
    text9 = "\n \npress space to continue"
    text10 = "This block has ended. \n \nTo start and experience the waiting duration for the next block, press space.";
    text11 = "The experiment is finished\n                 Thank you!"
    text12 = "Waiting duration for shorter reward..."
    text13 = "Please wait, you are expriencing the waiting duration!"
    text14 = "Waiting duration for larger reward..."
    textopt1 = "  for 67%"
    textopt2 = "  for 100%"
    textchance0 = "You did not get it!"
    textchance1 = "You got it!"

# Initialize components for Routine "Instruction_2"
Instruction_2Clock = core.Clock()
Intro_1 = visual.TextStim(win=win, name='Intro_1',
    text='',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
intro_1_ending = keyboard.Keyboard()

# Initialize components for Routine "Initialization"
InitializationClock = core.Clock()

# Initialize components for Routine "begininbetween"
begininbetweenClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "fixFramed"
fixFramedClock = core.Clock()
fixImg = visual.ImageStim(
    win=win,
    name='fixImg', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.8, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text_13 = visual.TextStim(win=win, name='text_13',
    text='',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "inBetween"
inBetweenClock = core.Clock()
text_14 = visual.TextStim(win=win, name='text_14',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "delayFramed"
delayFramedClock = core.Clock()
delayImg = visual.ImageStim(
    win=win,
    name='delayImg', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.8, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text_130 = visual.TextStim(win=win, name='text_130',
    text='',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "intro4choose"
intro4chooseClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
bb = 1
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "choiceScreen"
choiceScreenClock = core.Clock()
choiceImg = visual.ImageStim(
    win=win,
    name='choiceImg', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.8, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
choiceResp = keyboard.Keyboard()
choiceWarning = visual.TextStim(win=win, name='choiceWarning',
    text='',
    font='Arial',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
intro = 0
bb = 0
total = 0
block = 0
nk = 0


short_reward = [16,16,16,16,16]
short_delay = [1,1,1,1,1]

long_reward = [32,32, 32, 32, 32]
long_delay = [3,1,15,30,7]


h = 'start'
n = 0

a = [0,0,0,0]
to_choose = visual.TextStim(win=win, name='to_choose',
    text='',
    font='Arial',
    pos=(0, -0.35), height=0.03, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "choiceLeft"
choiceLeftClock = core.Clock()
leftImg = visual.ImageStim(
    win=win,
    name='leftImg', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.8, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "feedbackLeft"
feedbackLeftClock = core.Clock()
rewardImgLeft = visual.ImageStim(
    win=win,
    name='rewardImgLeft', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.8, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
rewardText = visual.TextStim(win=win, name='rewardText',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "choiceRight"
choiceRightClock = core.Clock()
rightImg = visual.ImageStim(
    win=win,
    name='rightImg', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.8, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "feedbackRight"
feedbackRightClock = core.Clock()
rewardImgRight = visual.ImageStim(
    win=win,
    name='rewardImgRight', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.8, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
rightText = visual.TextStim(win=win, name='rightText',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "repeatScreen"
repeatScreenClock = core.Clock()
block4 = visual.ImageStim(
    win=win,
    name='block4', 
    image='sin', mask=None,
    ori=0, pos=(0.5, -0.2), size=(0.35, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
block3 = visual.ImageStim(
    win=win,
    name='block3', 
    image='sin', mask=None,
    ori=0, pos=(0.5, 0.2), size=(0.35, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
block2 = visual.ImageStim(
    win=win,
    name='block2', 
    image='sin', mask=None,
    ori=0, pos=(-0.5, -0.2), size=(0.35, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
block1 = visual.ImageStim(
    win=win,
    name='block1', 
    image='sin', mask=None,
    ori=0, pos=(-0.5, 0.2), size=(0.35, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
repeatText = visual.TextStim(win=win, name='repeatText',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
repeatResp = keyboard.Keyboard()
tl = [0,0,0,0]


# Initialize components for Routine "Block_screen"
Block_screenClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "endScreen"
endScreenClock = core.Clock()
endText = visual.TextStim(win=win, name='endText',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "language"-------
continueRoutine = True
# update component parameters for each repeat
lan_choose.keys = []
lan_choose.rt = []
_lan_choose_allKeys = []
# keep track of which components have finished
languageComponents = [lan_choose, language_text]
for thisComponent in languageComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
languageClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "language"-------
while continueRoutine:
    # get current time
    t = languageClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=languageClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *lan_choose* updates
    waitOnFlip = False
    if lan_choose.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        lan_choose.frameNStart = frameN  # exact frame index
        lan_choose.tStart = t  # local t and not account for scr refresh
        lan_choose.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(lan_choose, 'tStartRefresh')  # time at next scr refresh
        lan_choose.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(lan_choose.clock.reset)  # t=0 on next screen flip
    if lan_choose.status == STARTED and not waitOnFlip:
        theseKeys = lan_choose.getKeys(keyList=['1', '2'], waitRelease=False)
        _lan_choose_allKeys.extend(theseKeys)
        if len(_lan_choose_allKeys):
            lan_choose.keys = _lan_choose_allKeys[-1].name  # just the last key pressed
            lan_choose.rt = _lan_choose_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *language_text* updates
    if language_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        language_text.frameNStart = frameN  # exact frame index
        language_text.tStart = t  # local t and not account for scr refresh
        language_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(language_text, 'tStartRefresh')  # time at next scr refresh
        language_text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in languageComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "language"-------
for thisComponent in languageComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if lan_choose.keys in ['', [], None]:  # No response was made
    lan_choose.keys = None
thisExp.addData('lan_choose.keys',lan_choose.keys)
if lan_choose.keys != None:  # we had a response
    thisExp.addData('lan_choose.rt', lan_choose.rt)
thisExp.nextEntry()
thisExp.addData('language_text.started', language_text.tStartRefresh)
thisExp.addData('language_text.stopped', language_text.tStopRefresh)

if (lan_choose.keys == '1'):
        #defining russian language
    text1= "Добро пожаловать в игру! \n Ваша задача заключается в том, чтобы выиграть как можно больше M&Ms. Для этого в каждом раунде игры Вам необходимо выбрать один из двух вариантов c разным количеством M&Ms, вероятностью их получения и длительностью ожидания. Точное количество M&Ms и вероятность их получения будут написаны на экране. Для прояснения смысла – попробуйте сыграть. Нажмите ПРОБЕЛ чтобы запустить несколько пробных раундов."
    text2= "демонстрация длительности ожидания"
    text3= "Для того, чтобы начать выбирать, нажмите ПРОБЕЛ."
    text4= "Для выбора этой опции нажмите 1  Для выбора этой опции нажмите 2"
    text6= "«Ведь несложно? Заметили ли Вы, что ждать большую награду было дольше? Время ожидания для каждого выбора различается в каждом из 4 блоков эксперимента и будет продемонстрировано Вам в начале каждого из них. Количество раундов в игре предопределено и не может быть увеличено за счет выбора более быстрой награды. Также каждые 200 M&Ms Вас ждет дополнительная награда. Нажмите ПРОБЕЛ для начала игры."
    text7= "Итого:"
    text8= "Ваш уровень"
    text9= "Нажмите ПРОБЕЛ для продолжения"
    text10 = "Этот блок закончен. Для начала следующего блока нажмите ПРОБЕЛ."
    text11 = "Игра закончена. Спасибо за участие!"
    text12 = "демонстрация длительности ожидания меньшей награды."
    text13 = "демонстрация длительности ожидания"
    text14 = "демонстрация длительности ожидания большей награды"
    textopt1= "67%"
    textopt2= "100%"
    textchance0 = "Вы не получили M&Ms!"
    textchance1 = "Вы получили M&Ms!"
    
else:
    text1 = "Welcome dear participants\n\nThis game is about collecting as much M&Ms as you can!\n\nEach time you must choose from two options with different probability of being rewarded and waiting time. The exact amount and probability for each option is written on the screen.\n\nEven if you are confused now, take it easy and try to play. It will get to you.\n\nPress 'space' to play it a bit for yourself.."
    text2 = 'Please wait, you are expriencing the waiting duration!'
    text3 = "You had experienced the waiting duration!\n\nPlease press 'space' to start choosing again."
    text4 = "(to choose this option press 1)            (To choose this option press 2)"
    text6 = "You saw how easy it was?! \n\n Have you noticed thаt waiting duration for the larger amount of M&Ms was also larger? \n\n The waiting duration of each choice will be presented at the beginning of each 4 blocks of the game. \n\n You should know that you cannot increase the number of rounds by choosing the faster rewards. \n\n One more thing, for every 200 points you earn one hidden reward! \n\n Press space to play the game for real!"
    text7 = "\n \ntotal gain:"
    text8 = "\n \nYou are in level"
    text9 = "\n \npress space to continue"
    text10 = "This block has ended. \n \nTo start and experience the waiting duration for the next block, press space.";
    text11 = "The game is finished\n                 Thank you!"
    text12 = "Waiting duration for smaller reward..."
    text13 = "Please wait, you are expriencing the waiting duration!"
    text14 = "Waiting duration for larger reward..."
    textopt1 = "  for 67%"
    textopt2 = "  for 100%"
    textchance0 = "You did not get it!"
    textchance1 = "You got it!"

ending_text = text6
# the Routine "language" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instruction_2"-------
continueRoutine = True
# update component parameters for each repeat
Intro_1.setText(text1
)
intro_1_ending.keys = []
intro_1_ending.rt = []
_intro_1_ending_allKeys = []
# keep track of which components have finished
Instruction_2Components = [Intro_1, intro_1_ending]
for thisComponent in Instruction_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instruction_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instruction_2"-------
while continueRoutine:
    # get current time
    t = Instruction_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instruction_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Intro_1* updates
    if Intro_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Intro_1.frameNStart = frameN  # exact frame index
        Intro_1.tStart = t  # local t and not account for scr refresh
        Intro_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Intro_1, 'tStartRefresh')  # time at next scr refresh
        Intro_1.setAutoDraw(True)
    
    # *intro_1_ending* updates
    waitOnFlip = False
    if intro_1_ending.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_1_ending.frameNStart = frameN  # exact frame index
        intro_1_ending.tStart = t  # local t and not account for scr refresh
        intro_1_ending.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_1_ending, 'tStartRefresh')  # time at next scr refresh
        intro_1_ending.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(intro_1_ending.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(intro_1_ending.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if intro_1_ending.status == STARTED and not waitOnFlip:
        theseKeys = intro_1_ending.getKeys(keyList=['space'], waitRelease=False)
        _intro_1_ending_allKeys.extend(theseKeys)
        if len(_intro_1_ending_allKeys):
            intro_1_ending.keys = _intro_1_ending_allKeys[-1].name  # just the last key pressed
            intro_1_ending.rt = _intro_1_ending_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instruction_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instruction_2"-------
for thisComponent in Instruction_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Intro_1.started', Intro_1.tStartRefresh)
thisExp.addData('Intro_1.stopped', Intro_1.tStopRefresh)
# check responses
if intro_1_ending.keys in ['', [], None]:  # No response was made
    intro_1_ending.keys = None
thisExp.addData('intro_1_ending.keys',intro_1_ending.keys)
if intro_1_ending.keys != None:  # we had a response
    thisExp.addData('intro_1_ending.rt', intro_1_ending.rt)
thisExp.nextEntry()
# the Routine "Instruction_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
discountingBlockLong = data.TrialHandler(nReps=200, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='discountingBlockLong')
thisExp.addLoop(discountingBlockLong)  # add the loop to the experiment
thisDiscountingBlockLong = discountingBlockLong.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisDiscountingBlockLong.rgb)
if thisDiscountingBlockLong != None:
    for paramName in thisDiscountingBlockLong:
        exec('{} = thisDiscountingBlockLong[paramName]'.format(paramName))

for thisDiscountingBlockLong in discountingBlockLong:
    currentLoop = discountingBlockLong
    # abbreviate parameter names if possible (e.g. rgb = thisDiscountingBlockLong.rgb)
    if thisDiscountingBlockLong != None:
        for paramName in thisDiscountingBlockLong:
            exec('{} = thisDiscountingBlockLong[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Initialization"-------
    continueRoutine = True
    # update component parameters for each repeat
    chance = [textchance1, textchance0, textchance1,textchance0, textchance1, textchance1,textchance0, textchance1,textchance1 ]
    if (n % 2) == 0:
        tx = str(long_reward[block])+ ' M&Ms ' +textopt1+'              '+str(short_reward[block])+' M&Ms '+textopt2
        chanceLeft = chance[n%9]
        chanceRight = textchance1
        transparencyRight = 1
        transparencyLeft = 0
        fixedImage = 'img/even_'+str(round(short_reward[block]/4))+'_square.png'
        delayImage = 'img/even_8_square_'+str(round(short_reward[block]/4))+'.png'
        choiceImage = 'img/even_choice_'+str(round(short_reward[block]/4))+'.png'
        choiceImageLeft = 'img/even_8_circle_'+str(round(short_reward[block]/4))+'.png'
        choiceImageRight = 'img/even_'+str(round(short_reward[block]/4))+'_circle.png'
        rewardImageLeft = 'img/8m&m.png'
        rewardImageRight = 'img/'+str(round(short_reward[block]/4))+'m&m.png'
        rewardLeft = long_reward[block]
        rewardRight = short_reward[block]
        block_screen = 0
    else:
        tx = str(short_reward[block])+' M&Ms '+textopt2+'              '+str(long_reward[block])+' M&Ms '+textopt1
        chanceLeft= textchance1
        chanceRight= chance[n%9]
        transparencyRight = 0
        transparencyLeft = 1
        fixedImage = 'img/odd_'+str(round(short_reward[block]/4))+'_square.png'
        delayImage = 'img/odd_8_square_'+str(round(short_reward[block]/4))+'.png'
        choiceImage = 'img/odd_choice_'+str(round(short_reward[block]/4))+'.png'
        choiceImageLeft = 'img/odd_'+str(round(short_reward[block]/4))+'_circle.png'
        choiceImageRight = 'img/odd_8_circle_'+str(round(short_reward[block]/4))+'.png'
        rewardImageLeft = 'img/'+str(round(short_reward[block]/4))+'m&m.png'
        rewardImageRight = 'img/8m&m.png'
        rewardLeft = short_reward[block]
        rewardRight = long_reward[block]
        block_screen = 0
    # keep track of which components have finished
    InitializationComponents = []
    for thisComponent in InitializationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    InitializationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Initialization"-------
    while continueRoutine:
        # get current time
        t = InitializationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=InitializationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InitializationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Initialization"-------
    for thisComponent in InitializationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Initialization" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    blockbegin4 = data.TrialHandler(nReps=asarray(bb), method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='blockbegin4')
    thisExp.addLoop(blockbegin4)  # add the loop to the experiment
    thisBlockbegin4 = blockbegin4.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlockbegin4.rgb)
    if thisBlockbegin4 != None:
        for paramName in thisBlockbegin4:
            exec('{} = thisBlockbegin4[paramName]'.format(paramName))
    
    for thisBlockbegin4 in blockbegin4:
        currentLoop = blockbegin4
        # abbreviate parameter names if possible (e.g. rgb = thisBlockbegin4.rgb)
        if thisBlockbegin4 != None:
            for paramName in thisBlockbegin4:
                exec('{} = thisBlockbegin4[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "begininbetween"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        text_6.setText(text12)
        # keep track of which components have finished
        begininbetweenComponents = [text_6]
        for thisComponent in begininbetweenComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        begininbetweenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "begininbetween"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = begininbetweenClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=begininbetweenClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_6* updates
            if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_6.frameNStart = frameN  # exact frame index
                text_6.tStart = t  # local t and not account for scr refresh
                text_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
                text_6.setAutoDraw(True)
            if text_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_6.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_6.tStop = t  # not accounting for scr refresh
                    text_6.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_6, 'tStopRefresh')  # time at next scr refresh
                    text_6.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in begininbetweenComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "begininbetween"-------
        for thisComponent in begininbetweenComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        blockbegin4.addData('text_6.started', text_6.tStartRefresh)
        blockbegin4.addData('text_6.stopped', text_6.tStopRefresh)
        thisExp.nextEntry()
        
    # completed asarray(bb) repeats of 'blockbegin4'
    
    
    # set up handler to look after randomisation of conditions etc
    blockbegin1 = data.TrialHandler(nReps=bb, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='blockbegin1')
    thisExp.addLoop(blockbegin1)  # add the loop to the experiment
    thisBlockbegin1 = blockbegin1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlockbegin1.rgb)
    if thisBlockbegin1 != None:
        for paramName in thisBlockbegin1:
            exec('{} = thisBlockbegin1[paramName]'.format(paramName))
    
    for thisBlockbegin1 in blockbegin1:
        currentLoop = blockbegin1
        # abbreviate parameter names if possible (e.g. rgb = thisBlockbegin1.rgb)
        if thisBlockbegin1 != None:
            for paramName in thisBlockbegin1:
                exec('{} = thisBlockbegin1[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "fixFramed"-------
        continueRoutine = True
        # update component parameters for each repeat
        fixImg.setImage(fixedImage)
        text_13.setText(text13)
        # keep track of which components have finished
        fixFramedComponents = [fixImg, text_13]
        for thisComponent in fixFramedComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fixFramedClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "fixFramed"-------
        while continueRoutine:
            # get current time
            t = fixFramedClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fixFramedClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixImg* updates
            if fixImg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixImg.frameNStart = frameN  # exact frame index
                fixImg.tStart = t  # local t and not account for scr refresh
                fixImg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixImg, 'tStartRefresh')  # time at next scr refresh
                fixImg.setAutoDraw(True)
            if fixImg.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixImg.tStartRefresh + short_delay[block]-frameTolerance:
                    # keep track of stop time/frame for later
                    fixImg.tStop = t  # not accounting for scr refresh
                    fixImg.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixImg, 'tStopRefresh')  # time at next scr refresh
                    fixImg.setAutoDraw(False)
            
            # *text_13* updates
            if text_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_13.frameNStart = frameN  # exact frame index
                text_13.tStart = t  # local t and not account for scr refresh
                text_13.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
                text_13.setAutoDraw(True)
            if text_13.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_13.tStartRefresh + short_delay[block]-frameTolerance:
                    # keep track of stop time/frame for later
                    text_13.tStop = t  # not accounting for scr refresh
                    text_13.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_13, 'tStopRefresh')  # time at next scr refresh
                    text_13.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixFramedComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fixFramed"-------
        for thisComponent in fixFramedComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        blockbegin1.addData('text_13.started', text_13.tStartRefresh)
        blockbegin1.addData('text_13.stopped', text_13.tStopRefresh)
        # the Routine "fixFramed" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed bb repeats of 'blockbegin1'
    
    
    # set up handler to look after randomisation of conditions etc
    blockbegin3 = data.TrialHandler(nReps=asarray(bb), method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='blockbegin3')
    thisExp.addLoop(blockbegin3)  # add the loop to the experiment
    thisBlockbegin3 = blockbegin3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlockbegin3.rgb)
    if thisBlockbegin3 != None:
        for paramName in thisBlockbegin3:
            exec('{} = thisBlockbegin3[paramName]'.format(paramName))
    
    for thisBlockbegin3 in blockbegin3:
        currentLoop = blockbegin3
        # abbreviate parameter names if possible (e.g. rgb = thisBlockbegin3.rgb)
        if thisBlockbegin3 != None:
            for paramName in thisBlockbegin3:
                exec('{} = thisBlockbegin3[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "inBetween"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        text_14.setText(text14)
        # keep track of which components have finished
        inBetweenComponents = [text_14]
        for thisComponent in inBetweenComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        inBetweenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "inBetween"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = inBetweenClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=inBetweenClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_14* updates
            if text_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_14.frameNStart = frameN  # exact frame index
                text_14.tStart = t  # local t and not account for scr refresh
                text_14.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_14, 'tStartRefresh')  # time at next scr refresh
                text_14.setAutoDraw(True)
            if text_14.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_14.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_14.tStop = t  # not accounting for scr refresh
                    text_14.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_14, 'tStopRefresh')  # time at next scr refresh
                    text_14.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in inBetweenComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "inBetween"-------
        for thisComponent in inBetweenComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        blockbegin3.addData('text_14.started', text_14.tStartRefresh)
        blockbegin3.addData('text_14.stopped', text_14.tStopRefresh)
        thisExp.nextEntry()
        
    # completed asarray(bb) repeats of 'blockbegin3'
    
    
    # set up handler to look after randomisation of conditions etc
    blockbegin0 = data.TrialHandler(nReps=bb, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='blockbegin0')
    thisExp.addLoop(blockbegin0)  # add the loop to the experiment
    thisBlockbegin0 = blockbegin0.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlockbegin0.rgb)
    if thisBlockbegin0 != None:
        for paramName in thisBlockbegin0:
            exec('{} = thisBlockbegin0[paramName]'.format(paramName))
    
    for thisBlockbegin0 in blockbegin0:
        currentLoop = blockbegin0
        # abbreviate parameter names if possible (e.g. rgb = thisBlockbegin0.rgb)
        if thisBlockbegin0 != None:
            for paramName in thisBlockbegin0:
                exec('{} = thisBlockbegin0[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "delayFramed"-------
        continueRoutine = True
        # update component parameters for each repeat
        delayImg.setImage(delayImage)
        text_130.setText(text13)
        # keep track of which components have finished
        delayFramedComponents = [delayImg, text_130]
        for thisComponent in delayFramedComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        delayFramedClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "delayFramed"-------
        while continueRoutine:
            # get current time
            t = delayFramedClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=delayFramedClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *delayImg* updates
            if delayImg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                delayImg.frameNStart = frameN  # exact frame index
                delayImg.tStart = t  # local t and not account for scr refresh
                delayImg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(delayImg, 'tStartRefresh')  # time at next scr refresh
                delayImg.setAutoDraw(True)
            if delayImg.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > delayImg.tStartRefresh + long_delay[block]-frameTolerance:
                    # keep track of stop time/frame for later
                    delayImg.tStop = t  # not accounting for scr refresh
                    delayImg.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(delayImg, 'tStopRefresh')  # time at next scr refresh
                    delayImg.setAutoDraw(False)
            
            # *text_130* updates
            if text_130.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_130.frameNStart = frameN  # exact frame index
                text_130.tStart = t  # local t and not account for scr refresh
                text_130.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_130, 'tStartRefresh')  # time at next scr refresh
                text_130.setAutoDraw(True)
            if text_130.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_130.tStartRefresh + long_delay[block]-frameTolerance:
                    # keep track of stop time/frame for later
                    text_130.tStop = t  # not accounting for scr refresh
                    text_130.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_130, 'tStopRefresh')  # time at next scr refresh
                    text_130.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in delayFramedComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "delayFramed"-------
        for thisComponent in delayFramedComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "delayFramed" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed bb repeats of 'blockbegin0'
    
    
    # set up handler to look after randomisation of conditions etc
    blockbegin2 = data.TrialHandler(nReps=bb, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='blockbegin2')
    thisExp.addLoop(blockbegin2)  # add the loop to the experiment
    thisBlockbegin2 = blockbegin2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlockbegin2.rgb)
    if thisBlockbegin2 != None:
        for paramName in thisBlockbegin2:
            exec('{} = thisBlockbegin2[paramName]'.format(paramName))
    
    for thisBlockbegin2 in blockbegin2:
        currentLoop = blockbegin2
        # abbreviate parameter names if possible (e.g. rgb = thisBlockbegin2.rgb)
        if thisBlockbegin2 != None:
            for paramName in thisBlockbegin2:
                exec('{} = thisBlockbegin2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "intro4choose"-------
        continueRoutine = True
        # update component parameters for each repeat
        text_2.setText(text3)
        key_resp_3.keys = []
        key_resp_3.rt = []
        _key_resp_3_allKeys = []
        # keep track of which components have finished
        intro4chooseComponents = [text_2, key_resp_3]
        for thisComponent in intro4chooseComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        intro4chooseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "intro4choose"-------
        while continueRoutine:
            # get current time
            t = intro4chooseClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=intro4chooseClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_2* updates
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                text_2.setAutoDraw(True)
            bb = 0
            
            # *key_resp_3* updates
            waitOnFlip = False
            if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_3.frameNStart = frameN  # exact frame index
                key_resp_3.tStart = t  # local t and not account for scr refresh
                key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
                key_resp_3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_3.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_3_allKeys.extend(theseKeys)
                if len(_key_resp_3_allKeys):
                    key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                    key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in intro4chooseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "intro4choose"-------
        for thisComponent in intro4chooseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        blockbegin2.addData('text_2.started', text_2.tStartRefresh)
        blockbegin2.addData('text_2.stopped', text_2.tStopRefresh)
        # check responses
        if key_resp_3.keys in ['', [], None]:  # No response was made
            key_resp_3.keys = None
        blockbegin2.addData('key_resp_3.keys',key_resp_3.keys)
        if key_resp_3.keys != None:  # we had a response
            blockbegin2.addData('key_resp_3.rt', key_resp_3.rt)
        # the Routine "intro4choose" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed bb repeats of 'blockbegin2'
    
    
    # ------Prepare to start Routine "choiceScreen"-------
    continueRoutine = True
    # update component parameters for each repeat
    choiceImg.setImage(choiceImage)
    choiceResp.keys = []
    choiceResp.rt = []
    _choiceResp_allKeys = []
    choiceWarning.setText(tx)
    left = 0
    right = 0
    if nk < 3:
        delta = 2
    else:
        delta = 1
    
    
    to_choose.setText(text4)
    # keep track of which components have finished
    choiceScreenComponents = [choiceImg, choiceResp, choiceWarning, to_choose]
    for thisComponent in choiceScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    choiceScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "choiceScreen"-------
    while continueRoutine:
        # get current time
        t = choiceScreenClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=choiceScreenClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *choiceImg* updates
        if choiceImg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            choiceImg.frameNStart = frameN  # exact frame index
            choiceImg.tStart = t  # local t and not account for scr refresh
            choiceImg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choiceImg, 'tStartRefresh')  # time at next scr refresh
            choiceImg.setAutoDraw(True)
        
        # *choiceResp* updates
        waitOnFlip = False
        if choiceResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            choiceResp.frameNStart = frameN  # exact frame index
            choiceResp.tStart = t  # local t and not account for scr refresh
            choiceResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choiceResp, 'tStartRefresh')  # time at next scr refresh
            choiceResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(choiceResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(choiceResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if choiceResp.status == STARTED and not waitOnFlip:
            theseKeys = choiceResp.getKeys(keyList=['1', '2'], waitRelease=False)
            _choiceResp_allKeys.extend(theseKeys)
            if len(_choiceResp_allKeys):
                choiceResp.keys = _choiceResp_allKeys[-1].name  # just the last key pressed
                choiceResp.rt = _choiceResp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *choiceWarning* updates
        if choiceWarning.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            choiceWarning.frameNStart = frameN  # exact frame index
            choiceWarning.tStart = t  # local t and not account for scr refresh
            choiceWarning.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choiceWarning, 'tStartRefresh')  # time at next scr refresh
            choiceWarning.setAutoDraw(True)
        
        # *to_choose* updates
        if to_choose.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            to_choose.frameNStart = frameN  # exact frame index
            to_choose.tStart = t  # local t and not account for scr refresh
            to_choose.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(to_choose, 'tStartRefresh')  # time at next scr refresh
            to_choose.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in choiceScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "choiceScreen"-------
    for thisComponent in choiceScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if choiceResp.keys in ['', [], None]:  # No response was made
        choiceResp.keys = None
    discountingBlockLong.addData('choiceResp.keys',choiceResp.keys)
    if choiceResp.keys != None:  # we had a response
        discountingBlockLong.addData('choiceResp.rt', choiceResp.rt)
    thisExp.addData('small_reward', short_reward[block])
    thisExp.addData('Delay', long_delay[block])
    
    if (n % 2) == 0:
        left_delay = long_delay[block]
        right_delay = short_delay[block]
        if(choiceResp.keys == '1'):
    
            if(chanceLeft == textchance1):
                transparencyLeft = 1
                total += long_reward[block]
            left = 1 
            short_reward[block] = round(short_reward[block] + delta,2)
            h += choiceResp.keys
    
    
        elif(choiceResp.keys == '2'):
            if(chanceRight == textchance1):
                transparencyRight = 1
                total += short_reward[block]
            right = 1
            short_reward[block] = round(short_reward[block] - delta,2)
            h += choiceResp.keys
    
    
    else:
        left_delay = short_delay[block]
        right_delay = long_delay[block]
        
        if(choiceResp.keys == '1'):
            if(chanceLeft == textchance1):
                transparencyLeft = 1
                total += short_reward[block]
            left = 1 
            short_reward[block] = round(short_reward[block] - delta,2)
            h += choiceResp.keys
    
    
            
        elif(choiceResp.keys == '2'):
            if(chanceRight == textchance1):
                transparencyRight= 1
                total += long_reward[block]
            right = 1
            short_reward[block] = round(short_reward[block] + delta,2)
            h += choiceResp.keys
    
    if short_reward[block] > 30:
        short_reward[block] = 30
    elif short_reward[block] < 1:
        short_reward[block] = 1
        
    if block == 0:
        intro += 1
        if intro == 4:
            block +=1
            total = 0
            block_screen = 1
            bb = 1
            h = 'start'
            
    if h[-2:] == '11' or h[-2:] == '22' or short_reward[block] == 1 or short_reward[block] == 30:
    
        a[block-1] += short_reward[block]
        nk +=1
        
        if nk==6:
            a[block-1] = a[block-1] / 6
    
            block +=1
            h = 'start'
            block_screen = 1
            bb = 1
            nk = 0
    
    level = int(total/ 200)
    repeat_text = text7 + ' ' + str(round(total,2))+"\n" + text8 + ' ' + str(level)+"\n" + text9
    
    if level > 0:
        if total < 800:
            tl [int(level -1)] = 1
    
    n +=1
    # the Routine "choiceScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    choiceLeftLoop = data.TrialHandler(nReps=left, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='choiceLeftLoop')
    thisExp.addLoop(choiceLeftLoop)  # add the loop to the experiment
    thisChoiceLeftLoop = choiceLeftLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisChoiceLeftLoop.rgb)
    if thisChoiceLeftLoop != None:
        for paramName in thisChoiceLeftLoop:
            exec('{} = thisChoiceLeftLoop[paramName]'.format(paramName))
    
    for thisChoiceLeftLoop in choiceLeftLoop:
        currentLoop = choiceLeftLoop
        # abbreviate parameter names if possible (e.g. rgb = thisChoiceLeftLoop.rgb)
        if thisChoiceLeftLoop != None:
            for paramName in thisChoiceLeftLoop:
                exec('{} = thisChoiceLeftLoop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "choiceLeft"-------
        continueRoutine = True
        # update component parameters for each repeat
        leftImg.setImage(choiceImageLeft)
        # keep track of which components have finished
        choiceLeftComponents = [leftImg]
        for thisComponent in choiceLeftComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        choiceLeftClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "choiceLeft"-------
        while continueRoutine:
            # get current time
            t = choiceLeftClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=choiceLeftClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *leftImg* updates
            if leftImg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                leftImg.frameNStart = frameN  # exact frame index
                leftImg.tStart = t  # local t and not account for scr refresh
                leftImg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(leftImg, 'tStartRefresh')  # time at next scr refresh
                leftImg.setAutoDraw(True)
            if leftImg.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > leftImg.tStartRefresh + left_delay-frameTolerance:
                    # keep track of stop time/frame for later
                    leftImg.tStop = t  # not accounting for scr refresh
                    leftImg.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(leftImg, 'tStopRefresh')  # time at next scr refresh
                    leftImg.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in choiceLeftComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "choiceLeft"-------
        for thisComponent in choiceLeftComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "choiceLeft" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "feedbackLeft"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        rewardImgLeft.setOpacity(transparencyLeft)
        rewardImgLeft.setImage(rewardImageLeft)
        rewardText.setText(chanceLeft)
        thisExp.addData('result of chosen',chanceLeft )
        thisExp.addData('delay of chosen', left_delay)
        thisExp.addData('reward of chosen', rewardLeft)
        
        thisExp.addData('total amount', total)
        # keep track of which components have finished
        feedbackLeftComponents = [rewardImgLeft, rewardText]
        for thisComponent in feedbackLeftComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        feedbackLeftClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "feedbackLeft"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = feedbackLeftClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=feedbackLeftClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *rewardImgLeft* updates
            if rewardImgLeft.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                rewardImgLeft.frameNStart = frameN  # exact frame index
                rewardImgLeft.tStart = t  # local t and not account for scr refresh
                rewardImgLeft.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rewardImgLeft, 'tStartRefresh')  # time at next scr refresh
                rewardImgLeft.setAutoDraw(True)
            if rewardImgLeft.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rewardImgLeft.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    rewardImgLeft.tStop = t  # not accounting for scr refresh
                    rewardImgLeft.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rewardImgLeft, 'tStopRefresh')  # time at next scr refresh
                    rewardImgLeft.setAutoDraw(False)
            
            # *rewardText* updates
            if rewardText.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                rewardText.frameNStart = frameN  # exact frame index
                rewardText.tStart = t  # local t and not account for scr refresh
                rewardText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rewardText, 'tStartRefresh')  # time at next scr refresh
                rewardText.setAutoDraw(True)
            if rewardText.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rewardText.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    rewardText.tStop = t  # not accounting for scr refresh
                    rewardText.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rewardText, 'tStopRefresh')  # time at next scr refresh
                    rewardText.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackLeftComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "feedbackLeft"-------
        for thisComponent in feedbackLeftComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.nextEntry()
        
    # completed left repeats of 'choiceLeftLoop'
    
    
    # set up handler to look after randomisation of conditions etc
    choiceRightLoop = data.TrialHandler(nReps=right, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='choiceRightLoop')
    thisExp.addLoop(choiceRightLoop)  # add the loop to the experiment
    thisChoiceRightLoop = choiceRightLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisChoiceRightLoop.rgb)
    if thisChoiceRightLoop != None:
        for paramName in thisChoiceRightLoop:
            exec('{} = thisChoiceRightLoop[paramName]'.format(paramName))
    
    for thisChoiceRightLoop in choiceRightLoop:
        currentLoop = choiceRightLoop
        # abbreviate parameter names if possible (e.g. rgb = thisChoiceRightLoop.rgb)
        if thisChoiceRightLoop != None:
            for paramName in thisChoiceRightLoop:
                exec('{} = thisChoiceRightLoop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "choiceRight"-------
        continueRoutine = True
        # update component parameters for each repeat
        rightImg.setImage(choiceImageRight)
        # keep track of which components have finished
        choiceRightComponents = [rightImg]
        for thisComponent in choiceRightComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        choiceRightClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "choiceRight"-------
        while continueRoutine:
            # get current time
            t = choiceRightClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=choiceRightClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *rightImg* updates
            if rightImg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rightImg.frameNStart = frameN  # exact frame index
                rightImg.tStart = t  # local t and not account for scr refresh
                rightImg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rightImg, 'tStartRefresh')  # time at next scr refresh
                rightImg.setAutoDraw(True)
            if rightImg.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rightImg.tStartRefresh + right_delay-frameTolerance:
                    # keep track of stop time/frame for later
                    rightImg.tStop = t  # not accounting for scr refresh
                    rightImg.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rightImg, 'tStopRefresh')  # time at next scr refresh
                    rightImg.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in choiceRightComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "choiceRight"-------
        for thisComponent in choiceRightComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "choiceRight" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "feedbackRight"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        rewardImgRight.setOpacity(transparencyRight)
        rewardImgRight.setImage(rewardImageRight)
        rightText.setText(chanceRight)
        thisExp.addData('result of chosen',chanceRight)
        thisExp.addData('delay of chosen', right_delay)
        thisExp.addData('reward of chosen', rewardRight)
        
        thisExp.addData('total amount', total)
        # keep track of which components have finished
        feedbackRightComponents = [rewardImgRight, rightText]
        for thisComponent in feedbackRightComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        feedbackRightClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "feedbackRight"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = feedbackRightClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=feedbackRightClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *rewardImgRight* updates
            if rewardImgRight.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                rewardImgRight.frameNStart = frameN  # exact frame index
                rewardImgRight.tStart = t  # local t and not account for scr refresh
                rewardImgRight.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rewardImgRight, 'tStartRefresh')  # time at next scr refresh
                rewardImgRight.setAutoDraw(True)
            if rewardImgRight.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rewardImgRight.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    rewardImgRight.tStop = t  # not accounting for scr refresh
                    rewardImgRight.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rewardImgRight, 'tStopRefresh')  # time at next scr refresh
                    rewardImgRight.setAutoDraw(False)
            
            # *rightText* updates
            if rightText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rightText.frameNStart = frameN  # exact frame index
                rightText.tStart = t  # local t and not account for scr refresh
                rightText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rightText, 'tStartRefresh')  # time at next scr refresh
                rightText.setAutoDraw(True)
            if rightText.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rightText.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    rightText.tStop = t  # not accounting for scr refresh
                    rightText.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rightText, 'tStopRefresh')  # time at next scr refresh
                    rightText.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackRightComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "feedbackRight"-------
        for thisComponent in feedbackRightComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.nextEntry()
        
    # completed right repeats of 'choiceRightLoop'
    
    
    # ------Prepare to start Routine "repeatScreen"-------
    continueRoutine = True
    # update component parameters for each repeat
    block4.setOpacity(tl[3])
    block4.setImage('img/coffee.jpeg')
    block3.setOpacity(tl[2])
    block3.setImage('img/cake.jpeg')
    block2.setOpacity(tl[1])
    block2.setImage('img/gummi.jpeg')
    block1.setOpacity(tl[0])
    block1.setImage('img/tea.jpeg')
    repeatText.setText(repeat_text)
    repeatResp.keys = []
    repeatResp.rt = []
    _repeatResp_allKeys = []
    # keep track of which components have finished
    repeatScreenComponents = [block4, block3, block2, block1, repeatText, repeatResp]
    for thisComponent in repeatScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    repeatScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "repeatScreen"-------
    while continueRoutine:
        # get current time
        t = repeatScreenClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=repeatScreenClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *block4* updates
        if block4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block4.frameNStart = frameN  # exact frame index
            block4.tStart = t  # local t and not account for scr refresh
            block4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block4, 'tStartRefresh')  # time at next scr refresh
            block4.setAutoDraw(True)
        
        # *block3* updates
        if block3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block3.frameNStart = frameN  # exact frame index
            block3.tStart = t  # local t and not account for scr refresh
            block3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block3, 'tStartRefresh')  # time at next scr refresh
            block3.setAutoDraw(True)
        
        # *block2* updates
        if block2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block2.frameNStart = frameN  # exact frame index
            block2.tStart = t  # local t and not account for scr refresh
            block2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block2, 'tStartRefresh')  # time at next scr refresh
            block2.setAutoDraw(True)
        
        # *block1* updates
        if block1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block1.frameNStart = frameN  # exact frame index
            block1.tStart = t  # local t and not account for scr refresh
            block1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block1, 'tStartRefresh')  # time at next scr refresh
            block1.setAutoDraw(True)
        
        # *repeatText* updates
        if repeatText.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            repeatText.frameNStart = frameN  # exact frame index
            repeatText.tStart = t  # local t and not account for scr refresh
            repeatText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(repeatText, 'tStartRefresh')  # time at next scr refresh
            repeatText.setAutoDraw(True)
        
        # *repeatResp* updates
        waitOnFlip = False
        if repeatResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            repeatResp.frameNStart = frameN  # exact frame index
            repeatResp.tStart = t  # local t and not account for scr refresh
            repeatResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(repeatResp, 'tStartRefresh')  # time at next scr refresh
            repeatResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(repeatResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(repeatResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if repeatResp.status == STARTED and not waitOnFlip:
            theseKeys = repeatResp.getKeys(keyList=['space'], waitRelease=False)
            _repeatResp_allKeys.extend(theseKeys)
            if len(_repeatResp_allKeys):
                repeatResp.keys = _repeatResp_allKeys[-1].name  # just the last key pressed
                repeatResp.rt = _repeatResp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in repeatScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "repeatScreen"-------
    for thisComponent in repeatScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    discountingBlockLong.addData('block3.started', block3.tStartRefresh)
    discountingBlockLong.addData('block3.stopped', block3.tStopRefresh)
    discountingBlockLong.addData('block2.started', block2.tStartRefresh)
    discountingBlockLong.addData('block2.stopped', block2.tStopRefresh)
    discountingBlockLong.addData('block1.started', block1.tStartRefresh)
    discountingBlockLong.addData('block1.stopped', block1.tStopRefresh)
    # check responses
    if repeatResp.keys in ['', [], None]:  # No response was made
        repeatResp.keys = None
    discountingBlockLong.addData('repeatResp.keys',repeatResp.keys)
    if repeatResp.keys != None:  # we had a response
        discountingBlockLong.addData('repeatResp.rt', repeatResp.rt)
    
    if block == 5:
        discountingBlockLong.finished=True 
    # the Routine "repeatScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=block_screen, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
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
        
        # ------Prepare to start Routine "Block_screen"-------
        continueRoutine = True
        # update component parameters for each repeat
        text.setText(ending_text
)
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # keep track of which components have finished
        Block_screenComponents = [text, key_resp]
        for thisComponent in Block_screenComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Block_screenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Block_screen"-------
        while continueRoutine:
            # get current time
            t = Block_screenClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Block_screenClock)
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
            
            # *key_resp* updates
            waitOnFlip = False
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Block_screenComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Block_screen"-------
        for thisComponent in Block_screenComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        trials.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            trials.addData('key_resp.rt', key_resp.rt)
        trials.addData('key_resp.started', key_resp.tStartRefresh)
        trials.addData('key_resp.stopped', key_resp.tStopRefresh)
        ending_text = text10
        # the Routine "Block_screen" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed block_screen repeats of 'trials'
    
    thisExp.nextEntry()
    
# completed 200 repeats of 'discountingBlockLong'


# ------Prepare to start Routine "endScreen"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
endText.setText(text11)
maxa = max(a[0], a[1], a[2], a[3])
for i in range(4):
    a[i] = a[i] / maxa

k = (6*(a[3]+a[0]) +  8*(a[3]+a[1]) + 15*(a[1]+a[2]) ) / (29*2)
thisExp.addData('DelayFactor', k)
#for extracting to csv I can do sum of this column
# keep track of which components have finished
endScreenComponents = [endText]
for thisComponent in endScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "endScreen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *endText* updates
    if endText.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        endText.frameNStart = frameN  # exact frame index
        endText.tStart = t  # local t and not account for scr refresh
        endText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endText, 'tStartRefresh')  # time at next scr refresh
        endText.setAutoDraw(True)
    if endText.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > endText.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            endText.tStop = t  # not accounting for scr refresh
            endText.frameNStop = frameN  # exact frame index
            win.timeOnFlip(endText, 'tStopRefresh')  # time at next scr refresh
            endText.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "endScreen"-------
for thisComponent in endScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
