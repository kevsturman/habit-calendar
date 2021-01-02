import datetime
import calendar

def getdays(year,month):
    month = calendar.monthcalendar(year,month)
    weekday = ["Mo","Tu","We","Th","Fr","Sa","Su"]
    monthlist = []
    for week in month:
        for i, day in enumerate(week):
            if day != 0:
                monthlist.append({"day":weekday[i],"number":day})

    return monthlist



