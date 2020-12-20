## 키보드로 입력하기 
## 메모장 찾아 글자 입력하기 
##### https://automatetheboringstuff.com/2e/chapter20/   참고 
##### 키보드 키 입력하기( esc, ctrl, enter 등등 ... )

import pyautogui
w = pyautogui.getWindowsWithTitle("new 1")[0]       # 메모장 1개 띄운 상태에서 가져옴. 
w.activate()            # 바로 글자 입력할 수 있도록 깜박 거린다. 클릭 필요없음. 

pyautogui.write("12345")
pyautogui.write("Nadocoding", interval=0.25)       # 글자마다 0.25 초씩 기다림. 
# pyautogui.write("나도코딩")                       # 한글 입력은 불가 

pyautogui.write(["t","e","s","t","left","left","right","right","l","a","enter","enter"], interval = 0.25)
#  t e s t 순서대로 적고, 왼쪽 방향키 두번, 오른쪽 방향키 두번, l a 순서대로 적고 엔터 

# 특수문자
# shift 4 --> $ 
pyautogui.keyDown("shift")      # shift key를 누른 상태에서 
pyautogui.press("4")            # 숫자 4를 입력하고, 
pyautogui.keyUp("shift")        # shift key를 뗀다. 

# 조합키 (Hot Key)   
# ctrl + A 
pyautogui.keyDown("ctrl")
pyautogui.keyDown("a")
pyautogui.keyUp("a")
pyautogui.keyUp("ctrl")

pyautogui.press("delete")

# 간편한 조합키 
# pyautogui.hotkey("ctrl","alt","shift","a")  # ctrl 누름, alt 누름, shift누름, a 누름, a 뗌, shift 뗌, alt 뗌, ctrl 뗌. 
pyautogui.write("aaaa", interval=0.25)
pyautogui.hotkey("ctrl","a")                # ctrl + A 누르기 
pyautogui.press("delete")

###############################################
#################  한글 입력하기  ############## 
###############################################
## pip install pyperclip
import pyperclip  
pyperclip.copy("나도코딩")      # "나도코딩" 글자를 클립보드에 저장 
pyautogui.hotkey("ctrl","v")
pyautogui.press("enter")

# 한글쓰는 함수 
def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl","v")

my_write("댕글코딩")

# #  자동화 프로그램 종료 
# 방법 1. 마우스를 네 귀퉁이로 가져간다. 
# 방법 2. 키보드 
#     win : ctrl + alt + del 
#     mac : cmd + shift + option + q 

