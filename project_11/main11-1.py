import pyautogui  # 마우스와 키보드 자동 제어
import os


os.chdir("./")

picPosition = pyautogui.locateOnScreen("mouseOut.png")
print(picPosition)

if picPosition is None:
    picPosition = pyautogui.locateOnScreen("mouseOn.png")
    print(picPosition)

if picPosition is None:
    picPosition = pyautogui.locateOnScreen("mouseClick.png")
    print(picPosition)
