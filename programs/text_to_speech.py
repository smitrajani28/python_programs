import win32com.client

li = []
n = int(input("enter number of shoutout do you want to give :"))
for i in range(n):
    name = input(f"enter name of {i+1} person :")
    li.append(name)

speaker = win32com.client.Dispatch("SAPI.spvoice")
for i in range(n):
    speaker.Speak(f"shoutout to {li[i]}")