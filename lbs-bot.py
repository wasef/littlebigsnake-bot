import pyautogui
import time
import keyboard

# This program was written to evaluate the functionality of the PyAutoGUI API. PyAutoGUI lets your Python scripts
# capture the screen and detect images within. Additionally, it allows you to control the mouse and keyboard to
# automate interactions with other applications. The LittleBigSnake.com web-based game was a good candidate to test
# the API. Please refer to the README.md file for more information.

# The following three boolean values can be modified by the user:
#
# Prints debug messages to output if set to True.
debug_mode = False
#
# Set to True if a VIP (paid) account is being used; this will allow you to receive extra bonuses.
vip_acct = False
#
# Set to True if you are using a free account with an ad-blocker running; some bonuses will not be received.
# If you want to receive free bonuses, turn off your ad-blocker and set this to False; video ads will display in game.
using_ad_blocker = False

# Constant values not recommended to be modified by user
sleep_time = 1
std_confidence = 0.9
low_confidence = 0.7
max_x = 1920
max_y = 1080

# Initialize variables used by program
space_down = False

# Don't terminate program via FAILSAFE when mouse moves to x,y position of 0,0
# The check_abort() function is being used to perform this task.
pyautogui.FAILSAFE = False


# Move the mouse out of the way so that it won't block images from being detected
def clear_mouse():
    pyautogui.moveTo(1, 100)


# Find the screen coordinates of the image file passed to the function
def get_loc(img, conf):
    clear_mouse()
    return pyautogui.locateCenterOnScreen('img/' + img + '.png', confidence=conf)


# If power bar recovered from zero value then press space bar down again to boost the speed
def press_space():
    global space_down
    if space_down is False:
        pyautogui.keyDown('space')
        space_down = True
        print_debug("Space Down")


# If game play stopped, or snake lost all power, depress the space bar
def depress_space():
    global space_down
    if space_down is True:
        pyautogui.keyUp('space')
        space_down = False
        print_debug("Space Up")


# Print debug message along with coordinates of image located on screen
def print_debug_plus(label, loc):
    if debug_mode is True:
        print(time.time(), label, loc)
    # Take this opportunity to depress space bar in case it's still active from game play
    depress_space()


# Print basic debug message
def print_debug(label):
    if debug_mode is True:
        print(time.time(), label)


# Put the snake in auto mode and boost the snake speed
def smart_boost():
    time.sleep(sleep_time + 1)
    pyautogui.press('a')
    time.sleep(sleep_time)
    press_space()


# Jiggle the mouse at the left of screen to indicate that alt+x key combo was detected
def indicate():
    pyautogui.moveTo(1, 500)
    for x in range(2):
        pyautogui.moveTo(100, 500, 0.25)
        pyautogui.moveTo(1, 500, 0.25)


# Terminate the program if alt+x is simultaneously pressed
def check_abort():
    if keyboard.is_pressed('x') and keyboard.is_pressed('alt'):
        indicate()
        print_debug("User aborted program!")
        exit()


# Start the program if alt+x is simultaneously pressed
def check_start():
    if keyboard.is_pressed('x') and keyboard.is_pressed('alt'):
        indicate()
        print_debug("User started program!")
        return True
    else:
        return False


# Check the screen resolution; abort program if resolution is not max_x by max_y
def check_resolution():
    x, y = pyautogui.size()
    if (x != max_x) or (y != max_y):
        pyautogui.alert(f"Your screen resolution must be {max_x} x {max_y}\n\nProgram aborted!")
        exit()


# Waits for video ad to end or if the skip option appears.
# This deals with all 4 variants of ad messages displayed at top of screen during the viewing of video ads.
# Each ad message has the text "without ad" within; allowing us to use only one image for detection.
def wait_for_ad(msg):
    time.sleep(1)
    loc_ad = get_loc('ad', low_confidence)
    if loc_ad is not None:
        print_debug_plus("Ad is Playing for " + msg + ": ", loc_ad)
    while loc_ad is not None:
        check_abort()
        time.sleep(1)
        # Skip the ad if the option is available
        loc_ad_skip = get_loc('ad-skip', std_confidence)
        if loc_ad_skip is not None:
            pyautogui.click(loc_ad_skip)
            print_debug_plus("Ad Skip: ", loc_ad_skip)
        loc_ad = get_loc('ad', low_confidence)


# Check screen resolution requirements before allowing program to run
check_resolution()

# Wait for the user to simultaneously press alt+x before starting this bot program
while True:
    if check_start() is True:
        break
    else:
        time.sleep(1)

# First check if user is on the home page before entering the endless while loop of the main program code
loc_playhome = get_loc('play-home', std_confidence)
if loc_playhome is not None:
    pyautogui.click(loc_playhome)
    print_debug_plus("Home Play Button Detected: ", loc_playhome)

# Endless while loop until the user simultaneously presses alt+x
# The check_abort() function will be used to intermittently check for alt+x keypress during the endless loop
while True:
    time.sleep(sleep_time)
    check_abort()
    loc_play = get_loc('play', std_confidence)
    if loc_play is not None:
        print_debug_plus("Play Button Detected: ", loc_play)
        # Wait to ensure bonuses have time to display on screen after detecting the game button is visible.
        time.sleep(sleep_time + 1)

        # Check to see if any upgrades are available for VIP accounts or free accounts that don't use an ad-blocker.
        if (vip_acct is True) or (vip_acct is False and using_ad_blocker is False):
            loc_double = get_loc('double', std_confidence)
            loc_earnkeys = get_loc('earn-keys', low_confidence)
        else:
            # Set to None if the above criteria is not met. This will allow the if/then below to be skipped.
            loc_double = None
            loc_earnkeys = None
        loc_open = get_loc('open', std_confidence)
        loc_gainskin = get_loc('gain-skin', std_confidence)
        time.sleep(sleep_time)

        # Double the awards contents given from a chest.
        if loc_double is not None:
            pyautogui.click(loc_double)
            print_debug_plus("Double: ", loc_double)
            if vip_acct is False and using_ad_blocker is False:
                wait_for_ad("Double")

        # Earn extra keys.
        elif loc_earnkeys is not None:
            pyautogui.click(loc_earnkeys)
            print_debug_plus("Earn Keys: ", loc_earnkeys)
            if vip_acct is False and using_ad_blocker is False:
                wait_for_ad("Keys")

        # Open royal chest.
        elif loc_open is not None:
            pyautogui.click(loc_open)
            print_debug_plus("Open Chest: ", loc_open)

        # Unlock skin when 99 ruby's are reached.
        elif loc_gainskin is not None:
            pyautogui.click(loc_gainskin)
            print_debug_plus("Gain Skin: ", loc_gainskin)
            # Give the animation some time before proceeding to locate and click the play99 button.
            time.sleep(sleep_time + 1)
            loc_play99 = get_loc('play99', std_confidence)
            if loc_play99 is not None:
                pyautogui.click(loc_play99)
                print_debug_plus("Play 99: ", loc_play99)

        # If none of the above upgrades were available then proceed to click the play button.
        else:
            # Start the game
            pyautogui.click(loc_play)
            print_debug_plus("Play: ", loc_play)
            # Initiate auto mode and press space bar to boost speed
            smart_boost()

    else:
        check_abort()

        # Search for other items that are displayed when the play button is not visible and game is not in play mode.
        if (vip_acct is True) or (vip_acct is False and using_ad_blocker is False):
            loc_extralife = get_loc('extra-life', std_confidence)
        else:
            loc_extralife = None
        loc_click1 = get_loc('click1', low_confidence)
        loc_click2 = get_loc('click2', low_confidence)
        loc_ok = get_loc('ok', std_confidence)
        loc_cancel = get_loc('cancel', std_confidence)
        loc_collect = get_loc('collect', std_confidence)
        time.sleep(sleep_time)

        # Continue playing when extra life option is given after death; available for VIP accounts & video ad viewers.
        if loc_extralife is not None:
            pyautogui.click(loc_extralife)
            print_debug_plus("Extra Life: ", loc_extralife)
            if vip_acct is False and using_ad_blocker is False:
                wait_for_ad("Life")

            smart_boost()
            # Skip the remaining checks since the game is restarting.
            # Otherwise the 'click to continue' button may be prematurely pressed.
            continue

        # The 'click to continue' button is visible on almost all windows.
        if loc_click1 is not None:
            pyautogui.click(loc_click1)
            print_debug_plus("Click 1: ", loc_click1)
        elif loc_click2 is not None:
            pyautogui.click(loc_click2)
            print_debug_plus("Click 2: ", loc_click2)

        # Close the game results window.
        if loc_ok is not None:
            pyautogui.click(loc_ok)
            print_debug_plus("Ok: ", loc_ok)
            if vip_acct is False and using_ad_blocker is False:
                wait_for_ad("Play")

        # New skin awarded. Click cancel to skip the option to select the new skin.
        if loc_cancel is not None:
            pyautogui.click(loc_cancel)
            print_debug_plus("Cancel: ", loc_cancel)

        # New title banner awarded.
        if loc_collect is not None:
            pyautogui.click(loc_collect)
            print_debug_plus("Collect New Title: ", loc_collect)

        check_abort()

        # If the power bar image is detected, then the game is in play mode.
        # Use this detection to skip testing of other buttons and continue with the while loop.
        loc_power_zero = get_loc('power-zero', std_confidence)
        loc_power_good = get_loc('power-good', std_confidence)
        if loc_power_zero is not None:
            # If power level drops to zero, depress the space bar to allow power to increase.
            print_debug("Zero Power Detected")
            depress_space()
            continue
        if loc_power_good is not None:
            # If 33% of power has been restored, resume pressing the space bar for a power boost.
            # print_debug("Good Power Detected")
            press_space()
            continue

