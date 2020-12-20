### 실행된 프로그램의 위치 찾기 

import pyautogui

# #### 현재 활성화 된 창의 정보 
# fw = pyautogui.getActiveWindow()  # 현재 활성화 된 창 ( VSCode )
# print (fw.title)                    # 창의 제목 정보 
# print (fw.size)                     # 창의 크기 정보 ( width, height )
# print (fw.left, fw.top, fw.right, fw.bottom) # 창의 좌표 정보 
# pyautogui.click(fw.left + 25, fw.top + 20 )

# ##### # 모든 윈도우 가져오기 
# for w in pyautogui.getAllWindows():
#     print(w) # 모든 윈도우 가져오기 

####### 특정 정보를 제목으로 가진 윈도우 가져오기 
w = pyautogui.getWindowsWithTitle("new 1")[0]
print(w) 
if w.isActive == False:     # 현재 활성화가 되지 않았다면 
    w.activate()            # 활성화 ( 맨 앞으로 가져오기 ) 

pyautogui.sleep (1) 
if w.isMaximized == False : # 현재 최대화가 되지 않았다면 
    w.maximize()            # 최대화 

pyautogui.sleep (1) 
if w.isMinimized == False : #  현재 최소화가 되지 않았다면 
    w.minimize()            # 최소화 

pyautogui.sleep (1) 
w.restore()                 # 화면 원복  

w.close()                   # 윈도우 닫기 