from plyer import notification
import time

if __name__== '__main__':
    while True:
        notification.notify(
            title="Reminder to drink water",
            message="It's time for you to drink water.", 
            app_name="Clock",
            timeout=5) # type: ignore
        print("Reminder Sent")
        time.sleep(3600 ) # 1 second * 60 * 60 => 1 hour





