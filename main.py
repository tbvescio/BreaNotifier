from win10toast import ToastNotifier
import time

toaster = ToastNotifier()

while True:
    time.sleep(1800) #waits 30 minutes
    toaster.show_toast("Breath","Wake up and strech yourself.")
    time.sleep(300) #waits 5 minutes
    toaster.show_toast("Work","You can get back to work!")
