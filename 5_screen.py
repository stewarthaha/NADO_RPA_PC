import pyautogui

# 스크린 샷 찍기
# img = pyautogui.screenshot()
# img.save("screenshhot.png") # 파일로 저장 

# 실제 클릭하는 곳의 RGB 값을 확인 후 그 곳이 맞는지 확인하기 

# pyautogui.mouseInfo()
# 77,209 81,154,186 #519ABA
pixel = pyautogui.pixel(77,209)
print(pixel)    # 81,154,186

print(pyautogui.pixelMatchesColor(77,209, pixel))       # True
print(pyautogui.pixelMatchesColor(77,209,(81,154,186)))  # 해당 위치의 rgb 값이 같으면 True
print(pyautogui.pixelMatchesColor(77,209,(80,154,186)))  # 해당 위치의 rgb 값이 다르면 False 