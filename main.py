import logging as log
import time
import argparse
import os
from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from playsound import playsound

MINUTES: int= 30
SOUND_FILE: str= 'echo.mpeg'

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))

def run():
    log.info("Running SoundScheduler")

    now = datetime.now()
    start_date = now.strftime('%Y-%m-%d') + " " + now.strftime('%H') + ":00:00" #:%M:%S')

    scheduler = BackgroundScheduler()
    scheduler.add_job(play_sound
        , 'interval'
        , id = "sound_scheduler"
        , start_date= start_date
        , minutes= MINUTES)
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
    sound_path = os.path.join(ROOT_PATH, SOUND_FILE)
    log.info(f'playing sound file {sound_path}')
    playsound(sound_path)

if __name__ == "__main__":
    configure_log()
    run()

    # for to keep the app running
    while True:
        time.sleep(0.3)
