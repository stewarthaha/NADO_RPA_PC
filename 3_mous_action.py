import pyautogui

# pyautogui.sleep(3) # 3초 대기 
# print(pyautogui.position())

# # pyautogui.click(64, 17, duration = 1)  # 1초 동안 64, 17 자표로 이동 후 마우스 클릭

# pyautogui.click()  #  click = mouseDown + mouseUp   : 마우스 드래그 등 
# pyautogui.mouseDown()
# pyautogui.mouseUp()

# pyautogui.doubleClick()
# pyautogui.click(clicks=500)  # 빠르게 500 번 클릭 clicks = 2 : doubleClick() 과 같다. 

# # 그림판을 열고 실행하면 200,200 --> 300,300 까지 선이 그려진다. 
# pyautogui.sleep(3) # 3초 대기 
# pyautogui.moveTo(200,200)
# pyautogui.mouseDown()       # 마우스 누른 상태
# pyautogui.moveTo(300,300, duration=2)
# pyautogui.mouseUp()         # 마우스 버튼 뗀 상태 

# pyautogui.sleep(3) # 3초 대기 
# pyautogui.rightClick()
# pyautogui.sleep(3) # 3초 대기 
# pyautogui.middleClick() # 휠 클릭

# # 메모장을 열고 제목 표시줄 위치로 마우스 이동 후 그 위치의 좌표를 얻고,  drag/dragTo 실행 
# pyautogui.sleep(3) # 3초 대기 
# print(pyautogui.position())
# pyautogui.moveTo()
# pyautogui.drag(100,0, duration=0.5) # 현재 위치 기준으로 x 100 만큼,  y 0 만큼 드래그 
# pyautogui.dragTo(400,400, duration=0.5) # 절대 위치로 드래그 

# 마우스 스크롤 하기 
pyautogui.scroll(300)  # 위 방향으로 300 만큼 스크롤 , 양수면 위 방향, 음수면 아래방향 스크롤 



