# 파일로 로그 남기기 


####### 터미널에 로그 남기기 ######
# import logging

# logging.basicConfig(level=logging.INFO, format = "%(asctime)s [%(levelname)s] %(message)s")    # 시간 [로그레벨] 메시지

# # 로그 레벨 단계 
# # debug < info < warning < error < critical 
# # level 에서 지정한 단계 이상의 로그만 남긴다. 
# # 배포 단계에서  logging level 을 INFO 로 바꾸면 debug 레벨의 로그는 안 남긴다. 

# logging.debug("아 이거 누가 짠거야~~ ")     # 개발단계에서 사용 
# logging.info("자동화 수행 준비")
# logging.warning("이 스크립트는 조금 오래 되었습니다. 문제가 발생할 수 있습니다.")
# logging.error("에러가 발생했습니다. 에러 코드는 ...")
# logging.critical("복구가 불가능한 심각한 문제가 발생했습니다..... ")

#####################################
####  터미널과 파일로 로그 남기기 #####
#####################################
import logging 
from datetime import datetime
#### 시간 [로그레벨] 메시지
loggFormatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")  
logger = logging.getLogger()
# 로그 레벨 설정 
logger.setLevel(logging.DEBUG)

# 스트림 (터미널)
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(loggFormatter)
logger.addHandler(streamHandler)

# 파일 
filename = datetime.now().strftime("mylogfile_%Y%m%d%H%M%S.log")    # mylogfile_20201212101011.log 형식 
fileHandler = logging.FileHandler(filename, encoding="utf-8")
fileHandler.setFormatter(loggFormatter)
logger.addHandler(fileHandler)

logger.debug("로그를 남겨보는 테스트를 진행합니다.")
# 2020-12-20 14:14:18,080 [DEBUG] 로그를 남겨보는 테스트를 진행합니다.