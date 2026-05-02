# Datetime in python is a module that provides classes for manipulating dates and times. It allows you to work with dates and times in both simple and complex ways. The datetime module provides various classes such as datetime, date, time, timedelta, and more.
# time module provides various time-related functions. It allows you to work with time in both simple and complex ways. The time module provides various functions such as time(), sleep(), and more.
# calendar module provides functions related to the calendar. It allows you to work with calendars in both simple and complex ways.
# timedelta is a class in the datetime module that represents a duration, the difference between two dates or times. It is used to perform arithmetic operations on dates and times, such as adding or subtracting a certain amount of time from a date or time.
# arrow is a library that provides a simple and intuitive way to work with dates and times in Python. It is built on top of the datetime module and provides additional functionality such as parsing, formatting, and manipulation of dates and times. Arrow allows you to easily convert between different date and time formats, perform arithmetic operations on dates and times, and handle time zones.


import arrow

brewing_time = arrow.utcnow()
print(brewing_time)
