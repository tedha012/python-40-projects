import pyupbit
import sqlite3
import datetime


def date_range(start, end):
    start = datetime.datetime.strptime(start, "%Y-%m-%d")
    start = start + datetime.timedelta(days=1)
    end = datetime.datetime.strftime(end, "%Y-%m-%d")
    end = end + datetime.timedelta(days=1)
    dates = [
        (start + datetime.timedelta(days=i)).strftime("%Y-%m-%d")
        for i in range((end - start).days + 1)
    ]
    return dates


dates = date_range("2022-10-31", "2022-11-02")

print(dates)
