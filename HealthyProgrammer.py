"""
Healthy Programmer Software
Office Hours : 9 am to 5 pm
Water - 3.5 litres to be consumed between offc hrs and play reminder music after every 30 mins and maintain water log - DrankLog
Eyes - eye exercise every 40 mins and play reminder music and maintain eyes log - EyDoneLog
Physical activity - exercise every 45 mins and play reminder music and maintain exercise log - ExDoneLog

water calculation - 3.5 ltrs = 3500 ml = approx 18 glasses of 200 ml (reminds every 30 mins)
"""
import pygame
from pygame import mixer
import time

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()


def getdate():
    import datetime
    timestamp1 = datetime.datetime.now()
    timestampStr = timestamp1.strftime("%d-%b-%Y (%H:%M:%S)")
    return timestampStr


def getCurrTime():
    import datetime
    time = datetime.datetime.now()
    hour = str(time.hour)
    minute = str(time.minute)
    return hour + ":" + minute


eye_reminders = ["09:00", "09:40", "10:20", "11:00", "11:40", "12:20", "13:00", "13:40", "14:20",
                   "15:00", "15:40", "16:20", "17:00"]
water_reminders = ["09:00", "09:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00",
                 "13:30", "14:00", "14:30", "15:00", "15:30", "16:00", "16:30", "17:00"]
exercise_reminders = ["09:00", "09:45", "10:30", "11:15", "12:00", "12:45", "13:30", "14:15",
                      "15:00", "15:45", "16:30"]

hr = time.localtime().tm_hour
print("*" * 150)
print("Welcome to Healthy programmer app. Reminds you of your body's basic needs")
print("*" * 150)


def callLog(activityType):
    if activityType == "DRANK":
        filename = "WaterLog.txt"
        writeIntoFile(filename, activityType)
    elif activityType == "EYDONE":
        filename = "EyeLog.txt"
        writeIntoFile(filename, activityType)
    elif activityType == "EXDONE":
        filename = "ExerciseLog.txt"
        writeIntoFile(filename, activityType)


def writeIntoFile(filename, activityType):
    fp = open(filename, "a")
    LogAc = getdate() + " : " + activityType + "\n"
    fp.write(LogAc)
    print(f"{filename} logged...")
    fp.close()


def loadMusic(musicFile):
    pygame.mixer.music.load(musicFile)
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)


def conditionCheck(activityType):
    if activityType == "DRANK":
        pygame.mixer.music.stop()
        callLog(activityType)
    elif activityType == "EYDONE":
        pygame.mixer.music.stop()
        callLog(activityType)
    elif activityType == "EXDONE":
        pygame.mixer.music.stop()
        callLog(activityType)


while (hr >= 9) and (hr <= 17):
    time_string = getCurrTime()
    print(time_string)
    if time_string in water_reminders:
        loadMusic('water.mp3')
        water = input("Please write DRANK after sipping the water\n")
        conditionCheck(water)
    if time_string in exercise_reminders:
        loadMusic('physical.mp3')
        exer = input("Did you do physical exercise? Key-in EXDONE if your answer is yes\n")
        conditionCheck(exer)
    if time_string in eye_reminders:
        loadMusic('eyes.mp3')
        eyes = input("Did you do eye exercise? Key-in EYDONE if your answer is yes\n")
        conditionCheck(eyes)
    time.sleep(60)
