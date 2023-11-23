import telegram
import asyncio
#import schedule -> 일반적인 schedule 모듈은 오류 발생
from apscheduler.schedulers.background import BackgroundScheduler #비동기 스케줄러인 APScheduler 사용
import time
import pytz
import datetime

token = "6824706855:AAEGeRWBJ3hNAslgVLBhZN-FKNLoIPPL4sI"
bot = telegram.Bot(token = token)
public_chat_name = "@opensw_yoon_test"
chat_id = "6917261069"

def job():
    now = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    if now.hour >= 23 or now.hour < 6:
        return
    id_channel = asyncio.run(bot.sendMessage(public_chat_name, text=str(now))).chat_id

schedule = BackgroundScheduler()
schedule.add_job(job, 'interval', minutes=10) # 10분마다 job()을 실행하도록 설정 -> 30분마다로 설정하려 했으나 계속되는 "raise TimedOut() from error telegram.error.TimedOut: Timed out" 오류로 10분으로 수정..
schedule.start() #설정한 BackgroundScheduler 실행
#schedule.every(1).minutes.do(job) -> 일반 scehdule로 사용했을시  "ValueError: a coroutine was expected, got <telegram.message.Message object at 0x000001E24A3500F8>" 발생

while True:
    time.sleep(1)

'''
<약간의 미완전한 부분..?>
비동기 스케줄러인 APScheduler로 변경했을시에도 
ValueError: a coroutine was expected, got <telegram.message.Message object at 0x0000021DB9F1B968>
오류는 반복적으로 발생하지만 Telegram chat은 정상적으로 출력되고 있음..
'''