import pyautogui
import cv2
import numpy as np
import time

# 찾을 이미지 파일 경로
target_image_path = 'test.png'

# 대기 시간 설정 (초)
wait_time = 0.3  # 0.3초마다 이미지를 찾음

def find_and_click_image(image_path):
    # 대상 이미지 로드
    target_image = cv2.imread(image_path)
    target_height, target_width, _ = target_image.shape

    while True:
        try:
            # 화면 캡처
            screenshot = pyautogui.screenshot()
            screenshot = np.array(screenshot)
            screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

            # 이미지 매칭
            result = cv2.matchTemplate(screenshot, target_image, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

            # 일치하는 이미지 발견 시 클릭
            if max_val > 0.8:  # 일치율 조정 가능 (0.8은 예시)
                target_loc = max_loc
                target_x, target_y = target_loc[0] + target_width // 2, target_loc[1] + target_height // 2
                pyautogui.moveTo(target_x, target_y)
                pyautogui.click()

            time.sleep(wait_time)

        except pyautogui.ImageNotFoundException:
            print("대상 이미지를 찾을 수 없습니다.")
        except Exception as e:
            print(f"에러 발생: {str(e)}")

# 이미지 계속 찾기
find_and_click_image(target_image_path)
