from project import Project
import schedule
import time

if __name__ == '__main__':
    p = Project()

    schedule.every().day.at("07:50",'Europe/Moscow').do(p.send,index=0)
    schedule.every().day.at("08:50",'Europe/Moscow').do(p.send,index=1)
    schedule.every().day.at("09:55",'Europe/Moscow').do(p.send,index=2)
    schedule.every().day.at("11:05",'Europe/Moscow').do(p.send,index=3)
    schedule.every().day.at("12:15",'Europe/Moscow').do(p.send,index=4)
    schedule.every().day.at("13:15",'Europe/Moscow').do(p.send,index=5)

    half_day = 12 * 60 * 60

    for i in range(half_day):
        schedule.run_pending()
        time.sleep(1)
