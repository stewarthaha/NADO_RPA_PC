import pyautogui

print("곧 시작합니다. ")
pyautogui.countdown(3)  # 3초동안 대기 
print("자동화 시작")

### 사용자가 자동화 프로그램에 개입이 필요한 경우 사용 

pyautogui.alert("자동화 수행에 실패하였습니다.","경고")     # 화인 버튼만 있는 팝업 , "경고" : 타이틀 
result = pyautogui.confirm("계속 진행하시겠습니까?", "확인")    # 확인(OK), 취소(Cancel) 버튼 , "확인","타이틀"
print(result)     

result = pyautogui.prompt("파일명을 무엇으로 하시겠습니까?","입력")     # 사용자 입력
print(result)                                               # 사용자 입력 내용이 result 에 저장됨. 

result = pyautogui.password("비밀번호를 입력하세요.")       # 암호 입력, 입력하는 중에는 * 로 표시됨. 
print(result)                                                  
