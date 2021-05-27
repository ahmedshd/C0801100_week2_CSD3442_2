import radius
from radius import circle
import studentname
from studentname import student

if __name__ == '__main__':
    radius.circle()
    studentname.student()

    from datetime import datetime

    dateTime = datetime.now()
    dateTime = dateTime.strftime("%Y-%m-%d %H:%M:%S")
    print("Date and time: ")
    print(dateTime)

