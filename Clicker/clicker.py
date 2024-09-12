import pyautogui
import time
from PIL import ImageGrab
import keyboard

# screen size
screen_width, screen_height = pyautogui.size()

# calculate the region to ignore top 20%
ignore_top = int(screen_height * 0.2)

# timeout duration (in seconds)
timeout_duration = 10

# start time
start_time = time.time()


# main function
k = 0
m = 0
o = 0
while True:
    if keyboard.is_pressed('k') and k == 0:
        k = 1
        print("k was pressed. Starting the script.")
        # reset start time to continue the 10 second countdown
        start_time = time.time()


    while k == 1:
        # check if the elapsed time exceeds the timeout duration
        elapsed_time = time.time() - start_time
        if elapsed_time > timeout_duration:
            print("Timeout reached. Exiting program.")
            quit()
       
        # check if the cursor is over an object that looks like "image1221.jpg" (an image of the target)
        image_center = pyautogui.locateCenterOnScreen('image1221.jpg', confidence=0.8, region=(0, ignore_top, screen_width, screen_height - ignore_top))
        if image_center is not None:
            # get the coordinates of the center of the image
            image_x, image_y = image_center
            # click the left mouse button at the center of the image
            pyautogui.click(x=image_x, y=image_y)
            # print when image is clicked
            print("click")
            # reset the start time to continue the 10 second countdown
            start_time = time.time()
        if image_center is None:
            print("none")

        #quit function
        if keyboard.is_pressed('m') and m == 0:
            m = 1
            print("m was pressed. Ending the script.")
            quit()

        #pause function
        if keyboard.is_pressed('o'):
            k = 0
            print("o was pressed. Pausing the script.")

        # add a small delay to prevent the script from operating too fast
        pyautogui.sleep(0.01)
