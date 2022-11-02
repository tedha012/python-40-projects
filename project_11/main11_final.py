import pyautogui  # 마우스와 키보드 자동 제어
import pyperclip  # 한글 클립보드 이용을 위해서
import time  # 시간 설정을 위해서

# 메시지 보내는 함수 선언
def send_message():
    # 평소 카톡 프로필 사진의 위치 검색
    picPosition = pyautogui.locateOnScreen("mouseOut.png")
    # Mouse On 일 경우 카톡창의 사진의 위치 검색
    if picPosition is None:
        picPosition = pyautogui.locateOnScreen("mouseOn.png")
    # Mouse Click 일 경우 카톡창의 사진의 위치 검색
    if picPosition is None:
        picPosition = pyautogui.locateOnScreen("mouseClick.png")
    # 검색한 사진 위치의 중앙 clickPosition 변수 선언
    clickPosition = pyautogui.center(picPosition)
    pyautogui.doubleClick(clickPosition)  # clickPosition double 클릭
    # 텍스트 복사하여 붙여넣기
    pyperclip.copy("잠시 자리를 비웠습니다...")
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1.0)  # 1초 딜레이
    pyautogui.write(["enter"])
    time.sleep(1.0)  # 1초 딜레이
    pyautogui.write(["escape"])
    time.sleep(1.0)  # 1초 딜레이


# 사진 위치 못 찾을시 except pass
while True:
    try:
        send_message()
    except:
        pass
