#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.4),
    on Tue Jun 14 14:13:54 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

### SET EXPERIMENT CONSTANTS ###
# trial image width/height size (in deg)
IMAGE_SIZE = 12
#trial 'click indicator' polygons' vertical offset
CLICKED_OFFSET = 9
#trial 'click indicator' polygons' size
CLICKED_SIZE = 0.5

# instruction screen example image size
IMAGE_SIZE_INST = 10

# instruction screen example image vertical offset
IMG_INST_V_OFFSET = 1

# instruction screen text vertical offset
TXT_INST_V_OFFSET = -5

# medium text size
MID_TXTSIZE = 0.6
LARGE_TXTSIZE = 1

# demonstration found/not found messages
NOTFOUND_TXT = 'Formen fanns här. Tryck höger knapp.'
FOUND_TXT = 'Precis, formen fanns här. Tryck höger knapp.'

# keyboard keys (or response button signals, if they are
# converted to keyboard presses) that are to be interpreted
# as left/right responses
LEFT_KEY = '3'
RIGHT_KEY = '1'
# it's not allowed to enter non-tuple/list variables in
# keyboard response components' 'allowed keys' fields,
# so also specify tuples to use
RESPONSE_KEYS = (LEFT_KEY, RIGHT_KEY)
LEFTKEY_TUPLE = (LEFT_KEY,)
RIGHTKEY_TUPLE = (RIGHT_KEY,)

# 'keyboard key' that MR trigger signal is
# converted into ('5' is commonly used)
MR_TRIGGERKEY_TUPLE = ('5',)

# trial image presentation durations
# Sapey/Boets:"The Gabor patterns dynamically evolved from a random
# orientation to a final orientation, within 5400 ms
# (following 12 logarithmic steps, including eleven 355 ms
# frames and one 1495 ms end frame)."
# specify end time of each image except the last one in the sets
# (last image is shown for a longer time than the others)
SHORT_DUR = 0.355
LONG_DUR = 1.495

### END SET EXPERIMENT CONSTANTS ###


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.4'
expName = 'gabor_object_recognition'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
}
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
    originPath='/Users/workingman/Documents/ASD_and_Synesthesia/Python/psychopy_shared_github/gabor_object_recognition/gabor_object_recognition.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 800], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='deg')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}
ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='ptb')

# Initialize components for Routine "instructions_part_one"
instructions_part_oneClock = core.Clock()
text_instructions_part_one = visual.TextStim(win=win, name='text_instructions_part_one',
    text='You will see images that change over time.\n\nThroughout the experiment, you will see a white dot in the center of the screen. Keep your eyes on it.\n\nIn some pictures, but not all, there is a pattern.\n\nPress the left button to see an example of when there is a pattern.',
    font='Arial',
    units='deg', pos=(0, 0), height=MID_TXTSIZE, wrapWidth=26, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_instructions_part_one = keyboard.Keyboard()

# Initialize components for Routine "stimulus_demonstration_pattern"
stimulus_demonstration_patternClock = core.Clock()
text_demo_pattern = visual.TextStim(win=win, name='text_demo_pattern',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "instructions_inter_demo"
instructions_inter_demoClock = core.Clock()
text_instructions_inter_demo = visual.TextStim(win=win, name='text_instructions_inter_demo',
    text='Did you see the pattern?\n\nPress the left button to see an example of when there is no pattern.',
    font='Arial',
    units='deg', pos=(0, TXT_INST_V_OFFSET), height=MID_TXTSIZE, wrapWidth=26, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_instructions_inter_demo = keyboard.Keyboard()
img_inter_demo = visual.ImageStim(
    win=win,
    name='img_inter_demo', units='deg', 
    image='stimuli/demo_img/RFP_OPP_1_12_highlighted.bmp', mask=None, anchor='center',
    ori=0, pos=(0, IMG_INST_V_OFFSET), size=(IMAGE_SIZE_INST, IMAGE_SIZE_INST),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)

# Initialize components for Routine "stimulus_demonstration_random"
stimulus_demonstration_randomClock = core.Clock()
text_demo_random = visual.TextStim(win=win, name='text_demo_random',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "instructions_part_two"
instructions_part_twoClock = core.Clock()
text_instructions_part_two = visual.TextStim(win=win, name='text_instructions_part_two',
    text='Some of the images you see will have patterns, as in the first example.\n\nAs soon as you see a pattern during the experiment, press the left button.\n\nWhen you have pressed the button, two small white boxes are shown.\n\nThe experiment takes about ten minutes. A message will appear when you are done.',
    font='Arial',
    units='deg', pos=(0, 0), height=MID_TXTSIZE, wrapWidth=26, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_instructions_part_two = keyboard.Keyboard()

# Initialize components for Routine "wait_for_mr_signal"
wait_for_mr_signalClock = core.Clock()
trigger_listener = keyboard.Keyboard()

# Initialize components for Routine "trial_gabor"
trial_gaborClock = core.Clock()
"""
Sets up lists of paths to image files for experiment stimuli and initializes
some variables/values that will be used throughout the experiment.
"""

import re
from random import sample, choices

def get_list_of_files(dir_name):
    """
    For the given path, gets a list of all files in the directory tree
    """
    # create a list of file and sub directory
    # names in the given directory
    # (excluding hidden files, ie those starting with a dot)
    list_of_files = [x for x in os.listdir(dir_name) if not x.startswith('.')]
    all_files = list()
    # Iterate over all the entries
    for entry in list_of_files:
        # Create full path
        full_path = os.path.join(dir_name, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(full_path):
            all_files = all_files + get_list_of_files(full_path)
        else:
            all_files.append(full_path)
    return all_files

def find_roots(target_dir, root_category):
    """
    finds roots of sets of files that hold stimulus sequence images, like
    'RFP_OPP_1' for the sequence 'RFP_OPP_1_1.bmp' through 'RFP_OPP_1_12.bmp'
    """
    roots = []
    for file_path in get_list_of_files(target_dir):
        if re.findall('bmp', file_path):
            new_root = (root_category, re.match(r'([A-Za-z].+_)[0-9]+\.bmp', file_path).group(1))
            roots.append(new_root)
    # ensure there are no duplicates
    roots = list(set(roots))
    return roots

# directory where all the stimuli images (or subdirectories containing the stimuli imgs)
# are stored
STIM_DIR = 'stimuli'
# name of subdirectory with 'grey' (blank) stimulus images
GREY_DIR = 'grey'
GREY_DIR = os.path.join(STIM_DIR, GREY_DIR)
# name of subdirectory with other (non-blank) stimuli images
# (assuming here a hierarchical directory structure where all non-grey stimuli
# images are stored in subdirectories of the 'non-blank' directory)
NONBLANK_DIR = 'Gabor stimuli Sapey Boets'
# name of sub-subdirectory with Random pattern stimuli images
RANDOM_DIR = 'RFP_RRR'
RANDOM_DIR = os.path.join(STIM_DIR, NONBLANK_DIR, RANDOM_DIR)
# name of sub-subdirectory with Contour stimuli images
CONTOUR_DIR = 'RFP_RCR'
CONTOUR_DIR = os.path.join(STIM_DIR, NONBLANK_DIR, CONTOUR_DIR)
# name of sub-subdirectory with Texture stimuli images
TEXTURE_DIR = 'RFP_OPP'
TEXTURE_DIR = os.path.join(STIM_DIR, NONBLANK_DIR, TEXTURE_DIR)
# name of sub-subdirectory with Contour & Texture stimuli images
CONTOUR_TEXTURE_DIR = 'RFP_RCP'
CONTOUR_TEXTURE_DIR = os.path.join(STIM_DIR, NONBLANK_DIR, CONTOUR_TEXTURE_DIR)
# name of sub-subdirectory with Contour # Texture Meaningful stimuli images
CONTOUR_TEXTURE_MEANINGFUL_DIR = 'Snod_RCP'
CONTOUR_TEXTURE_MEANINGFUL_DIR = os.path.join(
    STIM_DIR,
    NONBLANK_DIR,
    CONTOUR_TEXTURE_MEANINGFUL_DIR
)

# forming below lists of tuples, where each tuple has as its first 
# element the type of stimuli, and second element the filepath 
# to a stim image file (.bmp)

# get filepath root of each image set in the 'grey'/blank category
grey_filepath_roots = find_roots(GREY_DIR, 'grey')

# from Sapey-Triomphe, Boets et al article:
# "Participants performed two event-related fMRI runs. Each 
# fMRI run consisted of 67 trials: 10 presentations of each of 
# the five conditions (Random, Contour, Texture, Contour & 
# Texture Meaningless, Contour & Texture Meaningful) and 
# 17 fixation trials (baseline). "
# in this PsychoPy experiment, there are no two separate "runs" as 
# seen from the participant's perspective, since there is no pause 
# inbetween. stimuli are still split into two "runs" of 40 non-fixation 
# trials each however, to make the distribution of trials
# unpredictable but a bit more evenly spread out. to keep the ratio the 
# same. to keep the proportion of fixation/non-fixation trials the same, 
# here 17 * 40/50 = 13.6 ~= 14 fixation trials/"run" are used.
# form 14 copies of the 'grey' root, to ensure 14 fixation/baseline 
# trials per run. 
grey_filepath_roots = grey_filepath_roots * 14

# get filepath root of each image set in the nonblank categories
# (ensuring that there are 20 sets/trials for each category)
random_filepath_roots = find_roots(RANDOM_DIR, 'random')
random_filepath_roots = choices(random_filepath_roots, k=20)
contour_filepath_roots = find_roots(CONTOUR_DIR, 'contour')
contour_filepath_roots = sample(contour_filepath_roots, 20)
contour_texture_filepath_roots = find_roots(
    CONTOUR_TEXTURE_DIR,
    'contour_texture'
)
contour_texture_filepath_roots = sample(contour_texture_filepath_roots, 20)
contour_texture_meaningful_filepath_roots = find_roots(
    CONTOUR_TEXTURE_MEANINGFUL_DIR,
    'contour_texture_meaningful'
)
contour_texture_meaningful_filepath_roots = sample(contour_texture_meaningful_filepath_roots, 20)

# combine filepath roots in halves, first forming two separate
# "runs" (see comment above), and shuffle trials within-"runs"
run1 = (
 grey_filepath_roots +
 random_filepath_roots[:10] +
 contour_filepath_roots[:10] +
 contour_texture_filepath_roots[:10] +
 contour_texture_meaningful_filepath_roots[:10]
)

run2 = (
 grey_filepath_roots +
 random_filepath_roots[10:] +
 contour_filepath_roots[10:] +
 contour_texture_filepath_roots[10:] +
 contour_texture_meaningful_filepath_roots[10:]
)
shuffle(run1)
shuffle(run2)

# combine the two runs
all_filepath_roots = run1 + run2

# Sapey/Boets:"The Gabor patterns dynamically evolved from a random
# orientation to a final orientation, within 5400 ms
# (following 12 logarithmic steps, including eleven 355 ms
# frames and one 1495 ms end frame)."
# specify end time of each image except the last one in the sets
# (last image is shown for a longer time than the others)
img_duration_ls=[SHORT_DUR*mult for mult in range(1, 12)]+[999999]

# initialize image object
image_stimulus = visual.ImageStim(
    win=win, units='deg',
    name='image_stimulus',
    image=all_filepath_roots[0][1] + "1.bmp", mask=None,
    ori=0, pos=(0, 0), size=(IMAGE_SIZE, IMAGE_SIZE),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

key_resp_trial = keyboard.Keyboard()
polygon_trial_clicked_right = visual.Rect(
    win=win, name='polygon_trial_clicked_right',
    width=(CLICKED_SIZE, CLICKED_SIZE)[0], height=(CLICKED_SIZE, CLICKED_SIZE)[1],
    ori=0, pos=(CLICKED_OFFSET, 0), anchor='center',
    lineWidth=0,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=0, depth=-2.0, interpolate=True)
polygon_trial_clicked_left = visual.Rect(
    win=win, name='polygon_trial_clicked_left',
    width=(CLICKED_SIZE, CLICKED_SIZE)[0], height=(CLICKED_SIZE, CLICKED_SIZE)[1],
    ori=0, pos=(-CLICKED_OFFSET, 0), anchor='center',
    lineWidth=0,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=0, depth=-3.0, interpolate=True)

# Initialize components for Routine "jittered_blank"
jittered_blankClock = core.Clock()
blank_image = visual.ImageStim(
    win=win,
    name='blank_image', units='deg', 
    image='stimuli/grey/grey_1_1.bmp', mask=None, anchor='center',
    ori=0, pos=(0, 0), size=(IMAGE_SIZE, IMAGE_SIZE),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
# import 'choice' function, needed for the custom 'generate_intervals' function
from random import choice 

def generate_intervals(total_time, step_size, min_interval, max_interval):
    """
    generates a list of intervals in seconds
    """
    if max_interval > total_time or min_interval > total_time:
        raise ValueError("max/min interval time must be lower than total time")
    if max_interval < 0 or min_interval < 0 or step_size < 0:
        raise ValueError("passed values must not be negative")
    if max_interval < min_interval:
        raise ValueError("min interval must be less than max interval")
    if min_interval%step_size != 0 or max_interval%step_size != 0:
        raise ValueError("max/min interval time must both be \
        multiples of step_size")
    num_steps = round((max_interval - min_interval) / step_size) + 1
    possible_intervals = np.linspace(min_interval, max_interval, num_steps)
    return_intervals = []
    aggregated_time = 0
    num_addition_attempts = 0
    num_runs = 0
    while aggregated_time != total_time:
        num_addition_attempts += 1
        if num_addition_attempts > 200:
            aggregated_time = 0
            return_intervals = []
            num_addition_attempts = 0
            num_runs += 1
            if num_runs > 100:
                raise ValueError("unable to find a sequence that fulfills the constraints, please change them")
        ok_candidate = False
        new_time_candidate = choice(possible_intervals)
        possible_new_aggr_time = new_time_candidate + aggregated_time
        if possible_new_aggr_time > total_time:
            continue
        if possible_new_aggr_time == total_time:
            return_intervals.append(new_time_candidate)
            return return_intervals
        for interval in possible_intervals:
            if (possible_new_aggr_time + interval) < total_time:
                ok_candidate = True
        if ok_candidate:
            aggregated_time += new_time_candidate
            return_intervals.append(new_time_candidate)

# get the sum total inter-trial interval duration by taking 
# the number of trials and multiplying by 0.6 (average duration
# is to be 0.6s).
# generate random set of intervals of lengths 0.5s, 0.6s or 0.7s, 
# that add up to the calculated sum total duration, for jitter.
# (first multiplying each of the involved numbers by 10, 
# because integers must be used first when generating
# durations sequence,since floats lead to issues with 
# comparison operators)
sum_total_dur = len(all_filepath_roots) * 0.6
interval_durs = generate_intervals(total_time=int(sum_total_dur*10),
                               step_size=1,
                               min_interval=5,
                               max_interval=7)
# dividing each interval duration by 10 now that generation is done
interval_durs = [interval_dur/10 for interval_dur in interval_durs]

# initialize counter for stepping through interval durations
interval_counter = 0


# Initialize components for Routine "end_screen"
end_screenClock = core.Clock()
end_text = visual.TextStim(win=win, name='end_text',
    text='The experiment is now finished. Thank you!',
    font='Arial',
    units='deg', pos=(0, 0), height=LARGE_TXTSIZE, wrapWidth=26, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions_part_one"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_instructions_part_one.keys = []
key_resp_instructions_part_one.rt = []
_key_resp_instructions_part_one_allKeys = []
# keep track of which components have finished
instructions_part_oneComponents = [text_instructions_part_one, key_resp_instructions_part_one]
for thisComponent in instructions_part_oneComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructions_part_oneClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions_part_one"-------
while continueRoutine:
    # get current time
    t = instructions_part_oneClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructions_part_oneClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_instructions_part_one* updates
    if text_instructions_part_one.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_instructions_part_one.frameNStart = frameN  # exact frame index
        text_instructions_part_one.tStart = t  # local t and not account for scr refresh
        text_instructions_part_one.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_instructions_part_one, 'tStartRefresh')  # time at next scr refresh
        text_instructions_part_one.setAutoDraw(True)
    
    # *key_resp_instructions_part_one* updates
    waitOnFlip = False
    if key_resp_instructions_part_one.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_instructions_part_one.frameNStart = frameN  # exact frame index
        key_resp_instructions_part_one.tStart = t  # local t and not account for scr refresh
        key_resp_instructions_part_one.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_instructions_part_one, 'tStartRefresh')  # time at next scr refresh
        key_resp_instructions_part_one.status = STARTED
        # AllowedKeys looks like a variable named `LEFTKEY_TUPLE`
        if not type(LEFTKEY_TUPLE) in [list, tuple, np.ndarray]:
            if not isinstance(LEFTKEY_TUPLE, str):
                logging.error('AllowedKeys variable `LEFTKEY_TUPLE` is not string- or list-like.')
                core.quit()
            elif not ',' in LEFTKEY_TUPLE:
                LEFTKEY_TUPLE = (LEFTKEY_TUPLE,)
            else:
                LEFTKEY_TUPLE = eval(LEFTKEY_TUPLE)
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_instructions_part_one.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_instructions_part_one.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_instructions_part_one.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_instructions_part_one.getKeys(keyList=list(LEFTKEY_TUPLE), waitRelease=False)
        _key_resp_instructions_part_one_allKeys.extend(theseKeys)
        if len(_key_resp_instructions_part_one_allKeys):
            key_resp_instructions_part_one.keys = _key_resp_instructions_part_one_allKeys[-1].name  # just the last key pressed
            key_resp_instructions_part_one.rt = _key_resp_instructions_part_one_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_part_oneComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions_part_one"-------
for thisComponent in instructions_part_oneComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_instructions_part_one.keys in ['', [], None]:  # No response was made
    key_resp_instructions_part_one.keys = None
thisExp.addData('key_resp_instructions_part_one.keys',key_resp_instructions_part_one.keys)
if key_resp_instructions_part_one.keys != None:  # we had a response
    thisExp.addData('key_resp_instructions_part_one.rt', key_resp_instructions_part_one.rt)
thisExp.nextEntry()
# the Routine "instructions_part_one" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "stimulus_demonstration_pattern"-------
continueRoutine = True
# update component parameters for each repeat
### check for explanations in trial code snippet
# initialize counter for stepping through each set's images 
# the filenames go from "foobar_1.bmp" up to "foobar_12.bmp"
set_img_counter = 1

# set the filepath root for the set of images to use during
# the demonstration
demo_root = os.path.join(os.getcwd(), "stimuli", "Gabor stimuli Sapey Boets", "RFP_OPP", "RFP_OPP_1_")

# set first image to be drawn at beginning of routine
image_stimulus.image = demo_root + str(set_img_counter) + ".bmp"

# keep track of which components have finished
stimulus_demonstration_patternComponents = [text_demo_pattern]
for thisComponent in stimulus_demonstration_patternComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
stimulus_demonstration_patternClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "stimulus_demonstration_pattern"-------
while continueRoutine:
    # get current time
    t = stimulus_demonstration_patternClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=stimulus_demonstration_patternClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    ### check for explanations in trial code snippet
    # check if time for when last image should stop has passed
    if tThisFlip > SHORT_DUR*11+LONG_DUR:
        continueRoutine = False
    # check if the time for when previous image should stop has passed
    if tThisFlip > img_duration_ls[set_img_counter - 1]:
        image_stimulus.image = demo_root + str(set_img_counter) + ".bmp"
        set_img_counter += 1
    image_stimulus.draw()
    
    # *text_demo_pattern* updates
    if text_demo_pattern.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_demo_pattern.frameNStart = frameN  # exact frame index
        text_demo_pattern.tStart = t  # local t and not account for scr refresh
        text_demo_pattern.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_demo_pattern, 'tStartRefresh')  # time at next scr refresh
        text_demo_pattern.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in stimulus_demonstration_patternComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "stimulus_demonstration_pattern"-------
for thisComponent in stimulus_demonstration_patternComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
image_stimulus.autoDraw = False
# the Routine "stimulus_demonstration_pattern" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructions_inter_demo"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_instructions_inter_demo.keys = []
key_resp_instructions_inter_demo.rt = []
_key_resp_instructions_inter_demo_allKeys = []
# keep track of which components have finished
instructions_inter_demoComponents = [text_instructions_inter_demo, key_resp_instructions_inter_demo, img_inter_demo]
for thisComponent in instructions_inter_demoComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructions_inter_demoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions_inter_demo"-------
while continueRoutine:
    # get current time
    t = instructions_inter_demoClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructions_inter_demoClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_instructions_inter_demo* updates
    if text_instructions_inter_demo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_instructions_inter_demo.frameNStart = frameN  # exact frame index
        text_instructions_inter_demo.tStart = t  # local t and not account for scr refresh
        text_instructions_inter_demo.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_instructions_inter_demo, 'tStartRefresh')  # time at next scr refresh
        text_instructions_inter_demo.setAutoDraw(True)
    
    # *key_resp_instructions_inter_demo* updates
    waitOnFlip = False
    if key_resp_instructions_inter_demo.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_instructions_inter_demo.frameNStart = frameN  # exact frame index
        key_resp_instructions_inter_demo.tStart = t  # local t and not account for scr refresh
        key_resp_instructions_inter_demo.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_instructions_inter_demo, 'tStartRefresh')  # time at next scr refresh
        key_resp_instructions_inter_demo.status = STARTED
        # AllowedKeys looks like a variable named `LEFTKEY_TUPLE`
        if not type(LEFTKEY_TUPLE) in [list, tuple, np.ndarray]:
            if not isinstance(LEFTKEY_TUPLE, str):
                logging.error('AllowedKeys variable `LEFTKEY_TUPLE` is not string- or list-like.')
                core.quit()
            elif not ',' in LEFTKEY_TUPLE:
                LEFTKEY_TUPLE = (LEFTKEY_TUPLE,)
            else:
                LEFTKEY_TUPLE = eval(LEFTKEY_TUPLE)
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_instructions_inter_demo.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_instructions_inter_demo.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_instructions_inter_demo.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_instructions_inter_demo.getKeys(keyList=list(LEFTKEY_TUPLE), waitRelease=False)
        _key_resp_instructions_inter_demo_allKeys.extend(theseKeys)
        if len(_key_resp_instructions_inter_demo_allKeys):
            key_resp_instructions_inter_demo.keys = _key_resp_instructions_inter_demo_allKeys[-1].name  # just the last key pressed
            key_resp_instructions_inter_demo.rt = _key_resp_instructions_inter_demo_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *img_inter_demo* updates
    if img_inter_demo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        img_inter_demo.frameNStart = frameN  # exact frame index
        img_inter_demo.tStart = t  # local t and not account for scr refresh
        img_inter_demo.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(img_inter_demo, 'tStartRefresh')  # time at next scr refresh
        img_inter_demo.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_inter_demoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions_inter_demo"-------
for thisComponent in instructions_inter_demoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_instructions_inter_demo.keys in ['', [], None]:  # No response was made
    key_resp_instructions_inter_demo.keys = None
thisExp.addData('key_resp_instructions_inter_demo.keys',key_resp_instructions_inter_demo.keys)
if key_resp_instructions_inter_demo.keys != None:  # we had a response
    thisExp.addData('key_resp_instructions_inter_demo.rt', key_resp_instructions_inter_demo.rt)
thisExp.addData('key_resp_instructions_inter_demo.started', key_resp_instructions_inter_demo.tStartRefresh)
thisExp.addData('key_resp_instructions_inter_demo.stopped', key_resp_instructions_inter_demo.tStopRefresh)
thisExp.nextEntry()
# the Routine "instructions_inter_demo" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "stimulus_demonstration_random"-------
continueRoutine = True
# update component parameters for each repeat
### check for explanations in trial code snippet
# initialize counter for stepping through each set's images 
# the filenames go from "foobar_1.bmp" up to "foobar_12.bmp"
set_img_counter = 1

# set the filepath root for the set of images to use during
# the demonstration
demo_root = os.path.join(os.getcwd(), "stimuli", "Gabor stimuli Sapey Boets", "RFP_RRR", "RFP_RRR_1_")

# set first image to be drawn at beginning of routine
image_stimulus.image = demo_root + str(set_img_counter) + ".bmp"

# keep track of which components have finished
stimulus_demonstration_randomComponents = [text_demo_random]
for thisComponent in stimulus_demonstration_randomComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
stimulus_demonstration_randomClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "stimulus_demonstration_random"-------
while continueRoutine:
    # get current time
    t = stimulus_demonstration_randomClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=stimulus_demonstration_randomClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    ### check for explanations in trial code snippet
    # check if time for when last image should stop has passed
    if tThisFlip > SHORT_DUR*11+LONG_DUR:
        continueRoutine = False
    # check if the time for when previous image should stop has passed
    if tThisFlip > img_duration_ls[set_img_counter - 1]:
        image_stimulus.image = demo_root + str(set_img_counter) + ".bmp"
        set_img_counter += 1
    image_stimulus.draw()
    
    # *text_demo_random* updates
    if text_demo_random.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_demo_random.frameNStart = frameN  # exact frame index
        text_demo_random.tStart = t  # local t and not account for scr refresh
        text_demo_random.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_demo_random, 'tStartRefresh')  # time at next scr refresh
        text_demo_random.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in stimulus_demonstration_randomComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "stimulus_demonstration_random"-------
for thisComponent in stimulus_demonstration_randomComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
image_stimulus.autoDraw = False
# the Routine "stimulus_demonstration_random" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructions_part_two"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_instructions_part_two.keys = []
key_resp_instructions_part_two.rt = []
_key_resp_instructions_part_two_allKeys = []
# keep track of which components have finished
instructions_part_twoComponents = [text_instructions_part_two, key_resp_instructions_part_two]
for thisComponent in instructions_part_twoComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructions_part_twoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions_part_two"-------
while continueRoutine:
    # get current time
    t = instructions_part_twoClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructions_part_twoClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_instructions_part_two* updates
    if text_instructions_part_two.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_instructions_part_two.frameNStart = frameN  # exact frame index
        text_instructions_part_two.tStart = t  # local t and not account for scr refresh
        text_instructions_part_two.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_instructions_part_two, 'tStartRefresh')  # time at next scr refresh
        text_instructions_part_two.setAutoDraw(True)
    
    # *key_resp_instructions_part_two* updates
    waitOnFlip = False
    if key_resp_instructions_part_two.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_instructions_part_two.frameNStart = frameN  # exact frame index
        key_resp_instructions_part_two.tStart = t  # local t and not account for scr refresh
        key_resp_instructions_part_two.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_instructions_part_two, 'tStartRefresh')  # time at next scr refresh
        key_resp_instructions_part_two.status = STARTED
        # AllowedKeys looks like a variable named `LEFTKEY_TUPLE`
        if not type(LEFTKEY_TUPLE) in [list, tuple, np.ndarray]:
            if not isinstance(LEFTKEY_TUPLE, str):
                logging.error('AllowedKeys variable `LEFTKEY_TUPLE` is not string- or list-like.')
                core.quit()
            elif not ',' in LEFTKEY_TUPLE:
                LEFTKEY_TUPLE = (LEFTKEY_TUPLE,)
            else:
                LEFTKEY_TUPLE = eval(LEFTKEY_TUPLE)
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_instructions_part_two.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_instructions_part_two.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_instructions_part_two.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_instructions_part_two.getKeys(keyList=list(LEFTKEY_TUPLE), waitRelease=False)
        _key_resp_instructions_part_two_allKeys.extend(theseKeys)
        if len(_key_resp_instructions_part_two_allKeys):
            key_resp_instructions_part_two.keys = _key_resp_instructions_part_two_allKeys[-1].name  # just the last key pressed
            key_resp_instructions_part_two.rt = _key_resp_instructions_part_two_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_part_twoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions_part_two"-------
for thisComponent in instructions_part_twoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_instructions_part_two.started', text_instructions_part_two.tStartRefresh)
thisExp.addData('text_instructions_part_two.stopped', text_instructions_part_two.tStopRefresh)
# the Routine "instructions_part_two" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "wait_for_mr_signal"-------
continueRoutine = True
# update component parameters for each repeat
trigger_listener.keys = []
trigger_listener.rt = []
_trigger_listener_allKeys = []
# keep track of which components have finished
wait_for_mr_signalComponents = [trigger_listener]
for thisComponent in wait_for_mr_signalComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
wait_for_mr_signalClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "wait_for_mr_signal"-------
while continueRoutine:
    # get current time
    t = wait_for_mr_signalClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=wait_for_mr_signalClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *trigger_listener* updates
    waitOnFlip = False
    if trigger_listener.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        trigger_listener.frameNStart = frameN  # exact frame index
        trigger_listener.tStart = t  # local t and not account for scr refresh
        trigger_listener.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trigger_listener, 'tStartRefresh')  # time at next scr refresh
        trigger_listener.status = STARTED
        # AllowedKeys looks like a variable named `MR_TRIGGERKEY_TUPLE`
        if not type(MR_TRIGGERKEY_TUPLE) in [list, tuple, np.ndarray]:
            if not isinstance(MR_TRIGGERKEY_TUPLE, str):
                logging.error('AllowedKeys variable `MR_TRIGGERKEY_TUPLE` is not string- or list-like.')
                core.quit()
            elif not ',' in MR_TRIGGERKEY_TUPLE:
                MR_TRIGGERKEY_TUPLE = (MR_TRIGGERKEY_TUPLE,)
            else:
                MR_TRIGGERKEY_TUPLE = eval(MR_TRIGGERKEY_TUPLE)
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(trigger_listener.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(trigger_listener.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if trigger_listener.status == STARTED and not waitOnFlip:
        theseKeys = trigger_listener.getKeys(keyList=list(MR_TRIGGERKEY_TUPLE), waitRelease=False)
        _trigger_listener_allKeys.extend(theseKeys)
        if len(_trigger_listener_allKeys):
            trigger_listener.keys = _trigger_listener_allKeys[-1].name  # just the last key pressed
            trigger_listener.rt = _trigger_listener_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wait_for_mr_signalComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "wait_for_mr_signal"-------
for thisComponent in wait_for_mr_signalComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if trigger_listener.keys in ['', [], None]:  # No response was made
    trigger_listener.keys = None
thisExp.addData('trigger_listener.keys',trigger_listener.keys)
if trigger_listener.keys != None:  # we had a response
    thisExp.addData('trigger_listener.rt', trigger_listener.rt)
thisExp.addData('trigger_listener.started', trigger_listener.tStartRefresh)
thisExp.addData('trigger_listener.stopped', trigger_listener.tStopRefresh)
thisExp.nextEntry()
# the Routine "wait_for_mr_signal" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_gabor = data.TrialHandler(nReps=len(all_filepath_roots), method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_gabor')
thisExp.addLoop(trials_gabor)  # add the loop to the experiment
thisTrials_gabor = trials_gabor.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_gabor.rgb)
if thisTrials_gabor != None:
    for paramName in thisTrials_gabor:
        exec('{} = thisTrials_gabor[paramName]'.format(paramName))

for thisTrials_gabor in trials_gabor:
    currentLoop = trials_gabor
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_gabor.rgb)
    if thisTrials_gabor != None:
        for paramName in thisTrials_gabor:
            exec('{} = thisTrials_gabor[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial_gabor"-------
    continueRoutine = True
    routineTimer.add(5.400000)
    # update component parameters for each repeat
    # initialize counter for stepping through each set's images 
    # the filenames go from "foobar_1.bmp" up to "foobar_12.bmp"
    set_img_counter = 1
    
    # fetch the filepath root for the set of images to use during
    # this trial, by popping it off the list of filepath roots
    trial_root = all_filepath_roots.pop()
    
    # set first image to be drawn at beginning of routine
    image_stimulus.image = trial_root[1] + str(set_img_counter) + ".bmp"
    
    # make the polygons indicating clicks entirely transparent
    polygon_trial_clicked_left.opacity = 0
    polygon_trial_clicked_right.opacity = 0
    click_indicators_visible = False
    
    key_resp_trial.keys = []
    key_resp_trial.rt = []
    _key_resp_trial_allKeys = []
    # keep track of which components have finished
    trial_gaborComponents = [key_resp_trial, polygon_trial_clicked_right, polygon_trial_clicked_left]
    for thisComponent in trial_gaborComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_gaborClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial_gabor"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial_gaborClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_gaborClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # DISABLED - specifying time of 5.4s in routine components instead,
        # for the sake of non-slip timing
        # check if time for when last image should stop has passed
        #if tThisFlip > SHORT_DUR*11+LONG_DUR:
        #    continueRoutine = False
               
        # check if the time for when previous image should stop has passed
        if tThisFlip > img_duration_ls[set_img_counter - 1]:
            image_stimulus.image = trial_root[1] + str(set_img_counter) + ".bmp"
            set_img_counter += 1
        image_stimulus.draw()
        
        if not click_indicators_visible and key_resp_trial.keys and trial_root[0] !='grey':
            polygon_trial_clicked_left.opacity = 1
            polygon_trial_clicked_right.opacity = 1
            click_indicators_visible = True
        
        # *key_resp_trial* updates
        waitOnFlip = False
        if key_resp_trial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_trial.frameNStart = frameN  # exact frame index
            key_resp_trial.tStart = t  # local t and not account for scr refresh
            key_resp_trial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_trial, 'tStartRefresh')  # time at next scr refresh
            key_resp_trial.status = STARTED
            # AllowedKeys looks like a variable named `LEFTKEY_TUPLE`
            if not type(LEFTKEY_TUPLE) in [list, tuple, np.ndarray]:
                if not isinstance(LEFTKEY_TUPLE, str):
                    logging.error('AllowedKeys variable `LEFTKEY_TUPLE` is not string- or list-like.')
                    core.quit()
                elif not ',' in LEFTKEY_TUPLE:
                    LEFTKEY_TUPLE = (LEFTKEY_TUPLE,)
                else:
                    LEFTKEY_TUPLE = eval(LEFTKEY_TUPLE)
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_trial.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_trial.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_trial.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_trial.tStartRefresh + 5.4-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_trial.tStop = t  # not accounting for scr refresh
                key_resp_trial.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_trial, 'tStopRefresh')  # time at next scr refresh
                key_resp_trial.status = FINISHED
        if key_resp_trial.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_trial.getKeys(keyList=list(LEFTKEY_TUPLE), waitRelease=False)
            _key_resp_trial_allKeys.extend(theseKeys)
            if len(_key_resp_trial_allKeys):
                key_resp_trial.keys = _key_resp_trial_allKeys[-1].name  # just the last key pressed
                key_resp_trial.rt = _key_resp_trial_allKeys[-1].rt
        
        # *polygon_trial_clicked_right* updates
        if polygon_trial_clicked_right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_trial_clicked_right.frameNStart = frameN  # exact frame index
            polygon_trial_clicked_right.tStart = t  # local t and not account for scr refresh
            polygon_trial_clicked_right.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_trial_clicked_right, 'tStartRefresh')  # time at next scr refresh
            polygon_trial_clicked_right.setAutoDraw(True)
        if polygon_trial_clicked_right.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_trial_clicked_right.tStartRefresh + 5.4-frameTolerance:
                # keep track of stop time/frame for later
                polygon_trial_clicked_right.tStop = t  # not accounting for scr refresh
                polygon_trial_clicked_right.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_trial_clicked_right, 'tStopRefresh')  # time at next scr refresh
                polygon_trial_clicked_right.setAutoDraw(False)
        
        # *polygon_trial_clicked_left* updates
        if polygon_trial_clicked_left.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_trial_clicked_left.frameNStart = frameN  # exact frame index
            polygon_trial_clicked_left.tStart = t  # local t and not account for scr refresh
            polygon_trial_clicked_left.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_trial_clicked_left, 'tStartRefresh')  # time at next scr refresh
            polygon_trial_clicked_left.setAutoDraw(True)
        if polygon_trial_clicked_left.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_trial_clicked_left.tStartRefresh + 5.4-frameTolerance:
                # keep track of stop time/frame for later
                polygon_trial_clicked_left.tStop = t  # not accounting for scr refresh
                polygon_trial_clicked_left.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_trial_clicked_left, 'tStopRefresh')  # time at next scr refresh
                polygon_trial_clicked_left.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_gaborComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_gabor"-------
    for thisComponent in trial_gaborComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_gabor.addData('stimulus_type', trial_root[0])
    trials_gabor.addData('stimulus_path', trial_root[1])
    # check responses
    if key_resp_trial.keys in ['', [], None]:  # No response was made
        key_resp_trial.keys = None
    trials_gabor.addData('key_resp_trial.keys',key_resp_trial.keys)
    if key_resp_trial.keys != None:  # we had a response
        trials_gabor.addData('key_resp_trial.rt', key_resp_trial.rt)
    trials_gabor.addData('key_resp_trial.started', key_resp_trial.tStartRefresh)
    trials_gabor.addData('key_resp_trial.stopped', key_resp_trial.tStopRefresh)
    trials_gabor.addData('polygon_trial_clicked_right.started', polygon_trial_clicked_right.tStartRefresh)
    trials_gabor.addData('polygon_trial_clicked_right.stopped', polygon_trial_clicked_right.tStopRefresh)
    trials_gabor.addData('polygon_trial_clicked_left.started', polygon_trial_clicked_left.tStartRefresh)
    trials_gabor.addData('polygon_trial_clicked_left.stopped', polygon_trial_clicked_left.tStopRefresh)
    
    # ------Prepare to start Routine "jittered_blank"-------
    continueRoutine = True
    routineTimer.add(9999.000000)
    # update component parameters for each repeat
    # get this trial's interval duration
    interval_dur = interval_durs[interval_counter]
    # the image component's duration is set to 9999,
    # to achieve non-slip timing. to counteract the 
    # time added to the routine timer, subtract 9999.
    # then add the actual routine duration.
    # (more information at 
    # https://discourse.psychopy.org/t/confusion-
    # about-how-to-implement-non-slip-timing-
    # for-trials-with-known-end-points/4479/8)
    routineTimer.add(-9999.000000 + interval_dur)
    # keep track of which components have finished
    jittered_blankComponents = [blank_image]
    for thisComponent in jittered_blankComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    jittered_blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "jittered_blank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = jittered_blankClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=jittered_blankClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank_image* updates
        if blank_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank_image.frameNStart = frameN  # exact frame index
            blank_image.tStart = t  # local t and not account for scr refresh
            blank_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank_image, 'tStartRefresh')  # time at next scr refresh
            blank_image.setAutoDraw(True)
        if blank_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank_image.tStartRefresh + 9999-frameTolerance:
                # keep track of stop time/frame for later
                blank_image.tStop = t  # not accounting for scr refresh
                blank_image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank_image, 'tStopRefresh')  # time at next scr refresh
                blank_image.setAutoDraw(False)
        if tThisFlip >= interval_dur:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in jittered_blankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "jittered_blank"-------
    for thisComponent in jittered_blankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_gabor.addData('blank_image.started', blank_image.tStartRefresh)
    trials_gabor.addData('blank_image.stopped', blank_image.tStopRefresh)
    # increment interval counter by 1 to proceed to next interval duration
    # for next routine iteration
    interval_counter += 1
    thisExp.nextEntry()
    
# completed len(all_filepath_roots) repeats of 'trials_gabor'


# ------Prepare to start Routine "end_screen"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
end_screenComponents = [end_text]
for thisComponent in end_screenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
end_screenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end_screen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = end_screenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=end_screenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_text* updates
    if end_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_text.frameNStart = frameN  # exact frame index
        end_text.tStart = t  # local t and not account for scr refresh
        end_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text, 'tStartRefresh')  # time at next scr refresh
        end_text.setAutoDraw(True)
    if end_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_text.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            end_text.tStop = t  # not accounting for scr refresh
            end_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(end_text, 'tStopRefresh')  # time at next scr refresh
            end_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_screenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end_screen"-------
for thisComponent in end_screenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('end_text.started', end_text.tStartRefresh)
thisExp.addData('end_text.stopped', end_text.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
