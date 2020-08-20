# Sound Scheduler
Allows you to schedule the playback of the sound.mps file

## Principal libraries:
1. [Apscheduler](https://apscheduler.readthedocs.io/en/stable/) -> this library lets schedule jobs to be executed periodically. 
2. [Playsound](https://github.com/TaylorSMarks/playsound) -> Pure Python, cross platform, single function module with no dependencies for playing sounds.

## Configure execution time for scheduler
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

# Install
1. Download code
```sh
cd /bin
git clone https://github.com/avperillo/SoundScheduler
```
2. Install python libraries
```sh
cd SoundScheduler
sudo pip3 install -r requirements.txt
```
3. Run for to try
```sh
python3 main.py
```
Press Ctrl+C for close script

# Configure on system startup
1. Create sound_scheduler.service
```sh
sudo nano /lib/systemd/user/sound_scheduler.service
```
Copy next text
```
[Unit]
Description=Run SoundScheduler python script
After=default.target

[Service]
WorkingDirectory=/usr/bin/SoundScheduler
Type=simple
ExecStart=python3 /usr/bin/SoundScheduler/main.py &
Restart=on-failure

[Install]
WantedBy=default.target
```
2. Enable service
```sh
systemctl --user daemon-reload
systemctl --user enable sound_scheduler.service
systemctl --user start sound_scheduler.service
```
3. Check log for service
```sh
systemctl --user status sound_scheduler.service
sound_scheduler.service - Run SoundScheduler python script
     Loaded: loaded (/usr/lib/systemd/user/sound_scheduler.service; enabled; vendor preset: enabled)
     Active: active (running) since Thu 2020-08-20 14:30:17 UTC; 11min ago
   Main PID: 2546 (python3)
     CGroup: /user.slice/user-1000.slice/user@1000.service/sound_scheduler.service
             └─2546 /usr/bin/python3 /usr/bin/SoundScheduler/main.py &

Aug 20 14:30:17 orangepilite systemd[1294]: Started Run SoundScheduler python script.
Aug 20 14:30:18 orangepilite python3[2546]: 2020-08-20 14:30:18,977 [MainThread  ] [INFO ]  Running SoundScheduler
Aug 20 14:30:19 orangepilite python3[2546]: 2020-08-20 14:30:19,300 [MainThread  ] [INFO ]  Adding job tentatively -- it will be properly scheduled when the scheduler starts
Aug 20 14:30:19 orangepilite python3[2546]: 2020-08-20 14:30:19,307 [MainThread  ] [INFO ]  Added job "play_sound" to job store "default"
Aug 20 14:30:19 orangepilite python3[2546]: 2020-08-20 14:30:19,308 [MainThread  ] [INFO ]  Scheduler started

```
4. If Active is "active (running) since...", it's ok. Reboot the system and the service should run
```sh
reboot
```
