import time
import winsound
print("Timer")
def myAlarm():
    try:
        mytime=list(map(int,input("Enter Time in hr min sec: ").split()))
        if len(mytime)==3:
            total_sec=mytime[0]*60*60+mytime[1]*60+mytime[2]
            time.sleep(total_sec)
            frequency=2500
            duration=1000
            winsound.Beep(frequency,duration)
        else:
            print("Please enter time in correct format")
            myAlarm()
    except Eception as e:
        print("This is the exception: ",e,"So! Please enter correct details")
        myAlarm()
myAlarm()
