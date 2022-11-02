import pyautogui  # 마우스와 키보드 자동 제어
import pyperclip  # 한글 클립보드 이용을 위해서
import time  # 시간 설정을 위해서


def send_message():

    picPosition = pyautogui.locateOnScreen("mouseOut.png")
    print(picPosition)

    if picPosition is None:
        picPosition = pyautogui.locateOnScreen("mouseOn.png")
        print(picPosition)

    if picPosition is None:
        picPosition = pyautogui.locateOnScreen("mouseClick.png")
        print(picPosition)

    clickPosition = pyautogui.center(picPosition)
    pyautogui.doubleClick(clickPosition)

    pyperclip.copy("잠시 자리를 비웠습니다...")
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1.0)

    pyautogui.write(["enter"])
    time.sleep(1.0)

    pyautogui.write(["escape"])
    time.sleep(1.0)


while True:
    try:
        send_message()
    except:
        pass
