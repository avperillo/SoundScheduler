import logging as log
import time
import argparse
from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from playsound import playsound

MINUTES: int= 1
SOUND_FILE: str= './echo.mpeg'

def run(minutes: int, sound_file: str):
    log.info("Running SoundScheduler")

    now = datetime.now()
    start_date = now.strftime('%Y-%m-%d') + " " + now.strftime('%H') + ":00:00" #:%M:%S')

    scheduler = BackgroundScheduler()
    scheduler.add_job(play_sound
        , 'interval'
        , id = "sound_scheduler"
        , start_date= start_date
        , minutes= minutes)
    scheduler.start()

def configure_log():
    root_logger = log.getLogger()
    root_logger.setLevel(log.INFO)
    formatter = log.Formatter(
        "%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")

    handler = log.StreamHandler()
    handler.setFormatter(formatter)
    root_logger.addHandler(handler)

def play_sound():
    log.info('playing sound')
    playsound(SOUND_FILE)

if __name__ == "__main__":
    configure_log()

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-m', '--minutes', type=int, metavar='minutes', default= 30 
                            help='time elapsed in minutes')
    parser.add_argument('-s', '--file', type=str, metavar='sound_file', default= './echo.mpeg' 
                            help='sound file')
    args = my_parser.parse_args()

    run(args.minutes, args.sound_file)

    # for to keep the app running
    while True:
        time.sleep(0.3)