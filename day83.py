import win32com.client
names=["Soniya","Sanjay","Varnika","Vishwam","Sumitra","Jaydev"]


speaker = win32com.client.Dispatch("SAPI.SpVoice")


for name in names:
    speaker.Speak(f"Shoutout to {name}")
