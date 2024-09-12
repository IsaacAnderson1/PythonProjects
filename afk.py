import pyautogui
import time
import keyboard


def press_keys():
    while True:
        time.sleep(5)
        pyautogui.mouseDown(button='right')
        pyautogui.mouseUp(button='right')
        print("typed")


if __name__ == "__main__":
    press_keys()
