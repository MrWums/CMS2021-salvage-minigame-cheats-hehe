import numpy as np
import pyautogui
import mss
import time
import keyboard
import threading

running = False
def toggle_running():
    global running
    running = not running

def clicker():
    global running
    clicked_mouse = False

    with mss.mss() as sct:
        monitor = {"top": 500, "left": 650, "width": 630, "height": 65}

        while True:
            if running == True:
                image = np.array(sct.grab(monitor))
                image = image[:, :, :3][:, :, ::-1]

                matches = np.all(image == [71, 244, 255], axis=-1)
                blue_pixels = np.argwhere(matches)

                if len(blue_pixels) < 1000 and clicked_mouse == False:
                    pyautogui.click(1920/2,1080/2)
                    time.sleep(1)
                    pyautogui.mouseDown(1920/2,1080/2)
                    pyautogui.mouseUp(1920/2,1080/2)
                    clicked_mouse = True

                if len(blue_pixels) > 0:
                    clicked_mouse = False

keyboard.add_hotkey("s",toggle_running)

threading.Thread(target=clicker, daemon=True).start()

keyboard.wait("esc")
