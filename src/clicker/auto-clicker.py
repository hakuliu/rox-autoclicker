import pyautogui
import pytesseract
import cv2
import numpy as np
import time
import difflib
from PIL import Image, ImageEnhance, ImageFilter


def get_click_point():
    print("Position your mouse cursor where you want to click...")
    print("Press Enter when ready (you have 3 seconds after pressing Enter)")
    
    input("Press Enter to start countdown...")
    
    # Give user time to position mouse
    for i in range(3, 0, -1):
        print(f"Capturing position in {i}...")
        time.sleep(1)
    
    # Get current mouse position
    x, y = pyautogui.position()
    print(f"Captured position: ({x}, {y})")
    
    return x, y

def click_at_position(x, y, clicks=1, delay=0.5):
    print(f"Clicking at position ({x}, {y})")
    pyautogui.click(x, y, clicks=clicks)
    time.sleep(delay)

def parse_text(screenshot):
    # Default tesseract config for better accuracy
    custom_config = '--oem 3 --psm 6'
    
    # Extract text
    return pytesseract.image_to_string(screenshot, config=custom_config)

def hasPrompt(text):
    li = text.split()
    if not li:
        return False
    matches_please = difflib.get_close_matches('please', li, n=2, cutoff=0.8)
    matches_answering = difflib.get_close_matches('answering', li, n=2, cutoff=0.8)
    print(matches_please)
    print(matches_answering)
    return len(matches_please) > 0 or len(matches_answering) > 0

def garden():
    try:
        # Get click point from user
        # x, y = get_click_point()
        x = 600
        y = 515
        # Confirm before clicking
        cont = True
        while(cont):
            wait = 6
            click_at_position(x, y)
            x_offset = -210
            y_offset = -6
            w = 200
            h = 80
            screen = pyautogui.screenshot(region=(x + x_offset, y + y_offset, w, h))
            text = parse_text(screen)
            print(f'grabbed text...{text}')
            print(f"Clicking in {wait} seconds...")
            time.sleep(wait)
            cont = not hasPrompt(text)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"Error: {e}")


def main():
    # Disable PyAutoGUI failsafe (remove this line if you want failsafe)
    # pyautogui.FAILSAFE = False
    garden()

if __name__ == "__main__":
    main()