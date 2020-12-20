import pyautogui

# pyautogui.FAILSAFE = False  # 동작을 멈출때 창의 네 귀퉁이중에 한 곳으로 마우스를 가져가면 자동으로 종료됨. 
# 이 옵션 해제 
pyautogui.PAUSE = 1 # 모든 동작에 1초씩 sleep 적용

pyautogui.mouseInfo()  # F1 누르면 좌표, 색상 정보가 저장된다.  ( 3초 정도 대기 후  ctrl + v ) 
### 예 : 80,229 46,75,142 #2E4B8E  

for i in range(10):
    pyautogui.move(100,100)
