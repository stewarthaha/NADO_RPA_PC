### 전체 화면에서 원하는 부분(예: 클릭할 부분)의 이미지를 저장하고,
### 원하는 이미지가 전체 화면에서 어느 위치에 있는지 검사 후 
### 마우스를 해당 위치로 이동 후 작업(예: 클릭) 실행

import pyautogui
import time 


#### file 메뉴 클릭하기 

# file_menu = pyautogui.locateOnScreen("file_menu.png")  ## 전체 화면에서 해당 이미지가 어디에 있는지 리턴함. 

# ## win + shift + S     
# ## win + R  "mspaint"
# print(file_menu)                # Box(left=40, top=2, width=27, height=23)
# pyautogui.click(file_menu)      


###### trash 아이콘 위치 찾아 그곳으로 마우스 이동하기  
# trash_icon = pyautogui.locateOnScreen("trash_icon.png")     # locationOnScreen :일치하는 첫번째 이미지 정보 반환 
# pyautogui.moveTo(trash_icon)    

# #### 해당 위치 못 찾으면 None 반환 
# screenshot = pyautogui.locateOnScreen("screenshhot.png")
# print(screenshot)    # None

### 주의 : 화면 해상도 일치해야 한다. 

#### 일치하는 것 2개 이상일때 
#### https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox  에서 모든 체크박스 체크하기

# ### 일치하는 모든 체크박스 클릭
# for i in pyautogui.locateAllOnScreen("checkbox.png"):
#     print(i)
#     pyautogui.click(i)

### 첫번째 일치하는 것만 클릭 

# checkbox = pyautogui.locateOnScreen("checkbox.png")
# pyautogui.click(checkbox)

#### 속도 개선 ####
# t1 = time.time()
# trash_icon = pyautogui.locateOnScreen("trash_icon.png")     # locationOnScreen :일치하는 첫번째 이미지 정보 반환 
# pyautogui.moveTo(trash_icon)    
# t2 = time.time()
# print("Elapsed Time : {}".format(t2-t1))        # 9 sec

#### 속도 개선 1. Gray scale 
# t1 = time.time()
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", grayscale=True)     # locationOnScreen :일치하는 첫번째 이미지 정보 반환 
# pyautogui.moveTo(trash_icon)    
# t2 = time.time()
# print("Elapsed Time : {}".format(t2-t1))        # 3 sec

#### 속도 개선 2. 범위 지정  
# pyautogui.mouseInfo()
# 1272,437 127,30,127 #7F1E7F  : trash icon 마우스 정보 
# t1 = time.time()
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", region=(1100, 400, 300,100))     # region ( x,y,width, height)
# pyautogui.moveTo(trash_icon)    
# t2 = time.time()
# print("Elapsed Time : {}".format(t2-t1))        # 0.5 sec


#### 속도 개선 3. 정확도 조절 
# # pip install opencv-python
# t1 = time.time()
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", confidence=0.6 )       # 정확도 60% , 정확도가 많이 낮으면 오류발생
# pyautogui.moveTo(trash_icon)    
# t2 = time.time()
# print("Elapsed Time : {}".format(t2-t1))        # 0.4 sec


###### 자동화 대상이 바로 보여지지 않는 경우 ##### 
file_menu_npp = pyautogui.locateOnScreen("file_menu_npp.png")
# if file_menu_npp: 
#     pyautogui.click(file_menu_npp)
# else : 
#     print("발견실패")         ### npp 가 실행이 안 되어 발견 못 할때는 발견 실패 뜸. 

###### 자동화 대상이 바로 보여지지 않는 경우 1 : 계속 기다리기 
# while file_menu_npp is None:    # 찾지 못하면 찾을때까지 검사
#     file_menu_npp = pyautogui.locateOnScreen("file_menu_npp.png")
#     print("발견실패")
# pyautogui.click(file_menu_npp)  # 발견하면 파일 메뉴 클릭 

###### 자동화 대상이 바로 보여지지 않는 경우 2 : 일정 시간동안 기다리기 
import time 
import sys 

# timeout = 10  # 10 초 대기 
# start = time.time() # 시작 시간 설정 
# file_menu_npp = None 
# while file_menu_npp  is None : 
#     file_menu_npp = pyautogui.locateOnScreen("file_menu_npp.png")
#     end = time.time()   # 종료 시간 설정 
#     if end - start > timeout:    #  지정한 시간을 초과하면 ... 
#         print("시간종료")
#         sys.exit()

# pyautogui.click(file_menu_npp)
#####   ----> 이것을 함수로 만들자. 
def find_target(img_file, timeout=30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target

def my_click(img_file, timeout = 30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[TTimeout {timeout}s] Target not found ({img_file}). Terminate program.")
        sys.exit()

my_click("file_menu_npp.png", 10)   # 10초 동안 찾기 








