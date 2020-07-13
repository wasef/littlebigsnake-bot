## LittleBigSnake.com BOT using PyAutoGUI

This program was written to evaluate the functionality of the PyAutoGUI API. PyAutoGUI lets your Python scripts
capture the screen and detect images within. Additionally, it allows you to control the mouse and keyboard to automate 
interactions with other applications. The LittleBigSnake.com web-based game was a good candidate to test the API.

### Introduction

This program extends the autopilot functionality of the web-based game LittleBigSnake.com; allowing the game to play 
in an endless loop without user interaction.

The game has an autopilot function that will play the game for you using its simple A.I. However, once your snake dies, 
the game displays multiple dialog windows and then waits for your input to start a new game. This program deals with the 
multiple dialogs and begins a new game for you. It continues to do so until you end the program.

This program will continuously scan the screen and click on the relevant buttons to keep the game in motion. In doing
so, it is also claiming bonus awards for you (such as gold coins, ruby's, XP and more). These awarded items are used to
level-up your snake. By running this program for an extended period of time (AFK), it is essentially mining the game so
that you can level-up your snake for future game play.

### How to Use

After you execute the program, it will wait until you press the alt+x keys simultaneously before it takes control of 
the game. This gives you the opportunity to play the game until you need to step away from the computer; at this point 
you can give control to the program by pressing alt+x. Be sure to place your browser into full screen mode (F11) first.
Otherwise the program will not be able to properly detect key images on the screen.

You can give the program control (alt+x) at any time while you are on the Little Big Snake website. However, if you 
give the program control (alt+x) during a game session, you must turn on autopilot manually for the current game.
You may do this by hitting the 'a' key. Alternatively, you can just let your snake crash and die. The program will 
automatically turn the auto mode on after it starts the next game.

During game play, you will notice that your snake is traveling at high speeds (boosting). This program initiates speed
boosting when your health bar is above zero. If it drops to zero, the boost will be turned off until your health bar
reaches about 33-50%; wherein it will turn the boost back on.

You can end the program by pressing the alt+x keys simultaneously again. When you start and stop the program, the mouse
will jiggle slightly at the left of the screen to alert you that the alt+x keys were detected. Continuously hold the
alt+x key until you see this alert. Be sure to use alt+x to end the game before switching from the game screen to 
another application; otherwise the program may perform unwanted mouse clicks and keypress actions on your application. 

### Settings

There are three boolean values that need to be set before starting the program. The settings depends on what type of
account you're using and if an ad-blocker is being used in your browser.

If you are using a VIP (paid) account, set the boolean value `vip_acct = True`. Otherwise, set the boolean value as
`vip_acct = False`. VIP accounts allow you to receive extra bonus awards, such as double bonuses, earning extra keys, 
and using extra lives. Therefore, the boolean value is used to determine if the program should attempt to detect these
bonus awards on the screen. Additionally, VIP accounts do not display video ads; so the boolean value instructs the 
program not to bother detecting and waiting for the video ads to finish playing.

If you are using a free account with an ad-blocker, set the following boolean values `vip_acct = False`
and `using_ad_blocker = True`. If an ad-blocker is in use with a free account, the few awards mentioned above for VIP 
accounts will be ignored. The detection of video ads will also be ignored because the ad-blocker will block the
videos from being played.  

To receive the VIP awards while using a free account, turn off your ad-blocker and set the boolean values
`vip_acct = False` and `using_ad_blocker = False` to allow video ads to display. These video ads range between 15
and 30 seconds long. They sometimes display before a game and always display when claiming the VIP awards when using a
free account. This program will wait for the video ads to finish playing before proceeding to handle dialogs and game 
play actions.

Lastly, you can turn debug messages on (and off) with `debug_mode = True`. This allows you to review what has been 
detected by the program; along with the coordinates of the detected item and the epoch time of detection.

### Features

Works with both Free and VIP registered accounts.

Uses the alt+x hot key combo to start and end the program.

Can be started anytime before, during or after a gaming session.

Automatically turns on the built-in auto play mode.

Automatically turns speed boost on and off.

Waits for video ads to finish playing.

Handles all possible game events which include the following:
* Clicking the Play Game button
* Collecting Gold Coin awards
* Collecting Chest awards
* Collecting Royal Chest awards
* Collecting Ruby awards
* Collecting Snake Skin awards
* Collecting New Title Banner awards
* Initiating requests to Double your awards
* Initiating requests to Earn Keys
* Initiating requests to Use Extra Life
* Closing Level-Up notification windows
* Initiating Autopilot Mode
* Turning Speed Boost on & off as needed
* Skips video ads when available

### Requirements

This program was specifically made for a screen resolution of 1920 x 1080. It will not run properly otherwise. The game
must also run with the browser in full-screen mode (F11) on the primary monitor.

If you want this program to run on another screen resolution, you will have to re-create screen captures of all the
images found in the "img/" folder. Make sure the game is in full-screen mode when capturing these images.

Ensure that the autopilot feature is turned on in the game settings menu (the gear image at the bottom right of game 
screen). Otherwise this program will not be able to engage the autopilot mode and your snake will crash and die :(

You must use a free registered account or a paid VIP account. This bot was not programmed to deal with various windows 
that appear for non-registered accounts. Furthermore, you must manually play the game for the first few levels because 
this bot was not programmed to deal with various windows that appear for new players; such as hint window boxes and 
other such windows. So be sure to tick the "don't show again" boxes when these hint windows appear. Playing the first 
few levels manually will give you the opportunity to see how the game mechanics work, and how they relate to the code
in this program.

All of the above situations regarding non-registered accounts and new players can be addressed in this program if you 
wish to do so yourself. However in my case, the purpose of this bot was to test the PyAutoGUI functionality; therefore 
it was not in my scope of development to deal with the above mentioned situations.

### Dependencies

The following software components are required:
* Python3
* Pip3
* PyAutoGUI
* OpenCV
* Keyboard

On Windows, use pip to install the following dependencies:
> `pip3 install pyautogui` <br>
> `pip3 install opencv-python` <br>
> `pip3 install keyboard` <br>

On Linux, install the following:
> `sudo apt install python3-pip` <br>
> `sudo apt-get install -y python3-setuptools` <br>
> `python3 -m pip install pyautogui` <br>
> `sudo apt-get install scrot` <br>
> `sudo apt-get install python3-tk` <br>
> `sudo apt-get install python3-dev` <br>
> `pip3 install opencv-python` <br>
> `pip3 install keyboard` <br>

### In Conclusion

The PyAutoGUI performed very well for a simple game such as Little Big Snake. It was able to capture and detect image
locations at about 2.5 FPS. This value will of course vary depending on your computer specs. Sleep timers were used 
throughout the code because 2.5 FPS was overkill for this game. However, if the objective of this program was to 
control the snake to avoid obstacles and the like, the PyAutoGUI API would not be able to handle everything that needed
to be tracked, and responded to, in a timely manner. There are other API's out there that would be more feasible for
this purpose.

There were only a few minor drawbacks that I noticed while working with PyAutoGUI. First, you can only capture 
screenshots from the primary monitor. This wasn't an issue for this particular application. However it would have been
convenient to observe the automation on a secondary monitor while performing other work on the primary monitor. 

As for the second drawback, you can't use images of varying resolutions. This is the reason why this program requires 
the monitor to be running at a resolution of 1920 x 1080. If you wanted to support all or even just a few standard 
screen resolutions, you would have to re-capture the individual images found in the 'img/' folder for each screen 
resolution. With this, you could instruct the program to use the images corresponding with the current monitor 
resolution detected at start-up.

Lastly, you can only locate the position of one image at a time when capturing the screen. There were times that 
multiple images needed to be located on the same screenshot taken. In these cases, a screenshot of a static window 
needed to be taken multiple times to detect the screen position of each image. 

With all that said, the PyAutoGUI would perform very well for many applications that require automation; not just games.
It has a good set of functionality, many of which were used in this program.
