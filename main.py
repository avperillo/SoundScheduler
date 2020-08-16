import logging as log
import time
import argparse
from datetime import datetime
import os

from apscheduler.schedulers.background import BackgroundScheduler
from playsound import playsound

MINUTES: int= 20
SOUND_FILE: str= 'echo.mpeg'

def run():
    log.info("Running SoundScheduler")

    now = datetime.now()
    start_date = now.strftime('%Y-%m-%d') + " " + now.strftime('%H') + ":00:00" #:%M:%S')

    scheduler = BackgroundScheduler()
    scheduler.add_job(play_sound
        , 'interval'
        , id = "sound_scheduler"
        , start_date= start_date
        , seconds= MINUTES)
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
    root_path = os.path.dirname(os.path.realpath(__file__))
    sound_path = os.path.join(root_path, SOUND_FILE)
    playsound(sound_path)

if __name__ == "__main__":
    configure_log()
    run()

    # for to keep the app running
    while True:
        time.sleep(0.3)