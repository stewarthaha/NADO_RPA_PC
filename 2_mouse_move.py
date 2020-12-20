import pyautogui

# 마우스 이동 ( 절대 죄표 이용) 

pyautogui.moveTo(500,100)   # 왼쪽 위가 0, 0 
pyautogui.moveTo(100,300, duration=2)   # 2초 동안 지정한 죄표로 이동함. 
print(pyautogui.position()) # Point(x,y)  : 현재 마우스의 위치를 반환함. 
pyautogui.moveTo(200,400, duration=3)   # 3초 동안 지정한 죄표로 이동함. 
print(pyautogui.position()) # Point(x,y)  : 현재 마우스의 위치를 반환함. 
pyautogui.moveTo(600,200, duration=4)   # 4초 동안 지정한 죄표로 이동함. 
print(pyautogui.position()) # Point(x,y)  : 현재 마우스의 위치를 반환함. 

# 상대 좌표로 마우스 이동 ( 현재 커서가 있는 위치로부터)

pyautogui.move(100,100, duration = 2)
print(pyautogui.position()) # Point(x,y)  : 현재 마우스의 위치를 반환함. 
pyautogui.move(100,100, duration = 2)
print(pyautogui.position()) # Point(x,y)  : 현재 마우스의 위치를 반환함. 

p = pyautogui.position()
print(p[0], p[1])  # x,y
print(p.x, p.y)    # x,y  위와 같은 결과 
