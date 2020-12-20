###### 파일 기본 
import pyautogui
import os 
print(os.getcwd())  # current working directory 
os.chdir("Desktop_Auto")
print(os.getcwd())  # current working directory 
os.chdir("..")      # 부모폴더로 이동 
print(os.getcwd())  # current working directory 
os.chdir("../..")   # 조부모 폴더로 이동 
print(os.getcwd())  # current working directory 
os.chdir("C:/")     # 주어진 절대 경로로 이동 
print(os.getcwd())  # current working directory 
os.chdir("C:\\Users\\bibibig\\01_pystudy\\NADO_Coding\\RPA")
print(os.getcwd())  # current working directory 


# 파일 경로 
# 절대 경로로 파일 만들기 
file_path = os.path.join(os.getcwd(), "my_file.txt")        # 절대 경로 생성 
print(file_path) 

# 파일 경로에서 폴더 정보 가져오기 
print(os.path.dirname(r"C:\Users\bibibig\01_pystudy\NADO_Coding\RPA\my_file.txt"))

# 파일 정보 가져오기 
import time
import datetime

# 파일 생성날짜 
ctime = os.path.getctime("quiz_1.xlsx")
print(ctime)
print(datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S"))

# 파일 수정날짜
mtime = os.path.getmtime("quiz_1.xlsx")
print(datetime.datetime.fromtimestamp(mtime).strftime("%Y%m%d %H:%M:%S"))

# 마지막 접근 날짜 
atime = os.path.getatime("quiz_1.xlsx")
print(datetime.datetime.fromtimestamp(atime).strftime("%Y%m%d %H:%M:%S"))

# 파일 크기 
size = os.path.getsize("quiz_1.xlsx")
print(size)                         # 바이트 단위로 파일 크기 가져오기 

# 파일 목록 가져오기 
print(os.listdir()) # 모든 폴더, 파일 목록 가져오기 
print(os.listdir("Desktop_Auto"))   # 주어진 폴더 밑에서 모든 폴더, 파일 목록 가져오기 

# 파일 목록 가져오기 (하위 폴더 모두 포함)   , 입력한 폴더 기준으로 경로를 보여준다. 
result = os.walk("C:\\Users\\bibibig\\01_pystudy\\ML_일반")
print(result)           # 알아 볼 수 없는 형태로 나온다. 

for root, dirs, files in result:
    print(root,dirs,files)

#######################################################
######## 만약 폴더 내에서 특정 파일들을 찾으려면 #########
#######################################################
name = "11_file_system.py"
result = []
# for root, dirs, files in os.walk("."):             # 상대 경로로 출력
for root, dirs, files in os.walk(os.getcwd()):       # 절대 경로를 얻기 

    if name in files:
        result.append(os.path.join(root,name))
print(result)           # ['.\\Desktop_Auto\\11_file_system.py']   상대경로 출력 예

#######################################################
######## 폴더내 특정 패턴을 가진 파일들을 찾으려면 #######
#######################################################
print( "##### 폴더내 특정 패턴을 가진 파일들을 찾으려면 #####")
import fnmatch
pattern = "fi*.png"        #  "*.py" : .py로 끝나는 모든 파일 
result = []
for root, dirs, files in os.walk("."):       
    for name in files:
        if fnmatch.fnmatch(name, pattern):      # 이름과 패턴이 일치하면
            result.append(os.path.join(root, name))
print(result)

#######################################################
######## 주어진 경로가 파일인지? 폴더인지 확인 , 존재하지 않으면 False 반환  #######
#######################################################
print( "##### 주어진 경로가 파일인지? 폴더인지 확인  #####")
print(os.path.isdir("Desktop_Auto")) # Desktop_Auto 가 폴더인가 ? True
print(os.path.isfile("Desktop_Auto")) # Desktop_Auto 가 파일인가 ? False
print(os.path.isdir("checkbox.png")) # Desktop_Auto 가 폴더인가 ? False
print(os.path.isfile("checkbox.png")) # Desktop_Auto 가 폴더인가 ? True


#######################################################
######## 주어진 경로가 존재 하는지 확인            #######
#######################################################
print( "##### 주어진 경로가 존재 하는지 확인  #####")
if os.path.exists("01.py"):
    print("파일 또는 폴더가 존재합니다.")
else :
    print("파일 또는 폴더가 존재하지 않습니다.")

#######################################################
######## 파일/폴더 만들기 ,이름 변경 , 삭제       #######
#######################################################
print( "##### 파일 만들기  #####")
open("new_file.txt","a").close()                    # 빈 파일 생성 
pyautogui.sleep(3)
os.rename("new_file.txt","new_file_rename.txt")     # 파일명 변경하기 
pyautogui.sleep(3)                                  
os.remove("new_file_rename.txt")                    # 파일 삭제 
pyautogui.sleep(3)                                  
os.mkdir("new_folder")                              # 폴더 만들기, 절대 경로도 직접 넣으면 가능하다. 
#### 여러 하위 폴더를 가지는 폴더 생성 : mkdir 은 에러 발생함. --> os.makedirs 사용 
os.makedirs("multi_folders/a/b/c")

pyautogui.sleep(3)                                  
### 폴더명 변경하기 
os.rename("new_folder", "new_folder_rename")

### 폴더 지우기 (폴더가 없으면 에러 발생)
pyautogui.sleep(3)                                  
os.rmdir("new_folder_rename")       # 폴더 안이 비었을 때만 삭제 가능 
pyautogui.sleep(3)       

### 폴더 안에 다른 파일/폴더가 있을경우 삭제 
import shutil       # shell utilities
shutil.rmtree("multi_folders")      # 폴더 안이 비어있지 않아도 완전 삭제 가능 ##### 사용주의 ##### 







