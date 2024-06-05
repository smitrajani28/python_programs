import time
from win10toast import ToastNotifier
import datetime
import win32com.client
speaker = win32com.client.Dispatch("SAPI.spvoice")
  
  
def getTimeInput():
    hour = int(input("hours of interval :"))
    minutes = int(input("Mins of interval :"))
    seconds = int(input("Secs of interval :"))
    time_interval = seconds+(minutes*60)+(hour*3600)
    return time_interval
  
  
def log():
    now = datetime.datetime.now()
    start_time = now.strftime("%H:%M:%S")
    with open("log.txt", 'a') as f:
        f.write(f"You drank water {now} \n")
    
  
  
def notify():
    notification = ToastNotifier()
    notification.show_toast("Time to drink water")
    speaker.Speak("Time to drink water")
    log()
    
  
  
def starttime(time_interval):
    while True:
        time.sleep(time_interval)
        notify()
  
  
if __name__ == '__main__':
    time_interval = getTimeInput()
    starttime(time_interval)





# li = []
# n = int(input("enter number of shoutout do you want to give :"))
# for i in range(n):
#     name = input(f"enter name of {i+1} person :")
#     li.append(name)

# for i in range(n):