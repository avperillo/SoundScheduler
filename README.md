# Sound Scheduler
Allows you to schedule the playback of the sound.mps file

## Principal libraries:
1. [Apscheduler](https://apscheduler.readthedocs.io/en/stable/) -> this library lets schedule jobs to be executed periodically. 
2. [Playsound](https://github.com/TaylorSMarks/playsound) -> Pure Python, cross platform, single function module with no dependencies for playing sounds.

## Configure execution time for scheduler

Docs [here](https://apscheduler.readthedocs.io/en/stable/modules/triggers/cron.html#module-apscheduler.triggers.cron)

Add time argument that you need. 
available arguments can be found [here](https://apscheduler.readthedocs.io/en/stable/modules/triggers/cron.html#module-apscheduler.triggers.cron)

Example
```python
scheduler.add_job(play_sound
        , 'interval'
        , id = "sound_scheduler"
        , start_date= start_date
        , hour= 1
        , minutes= 30)
```