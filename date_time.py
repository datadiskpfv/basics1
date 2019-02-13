import time
import datetime

print(time.gmtime(0))       # the start epoch time 1st jan 1970
print(time.localtime())
print(time.time())          # seconds since epoch

time_now = time.localtime()         # a tuple is returned
print(time_now)
print("Year: ", time_now.tm_year)   # can also use time_now[0]
print("Month: ", time_now.tm_mon)   # can also use time_now[1]
print("Day: ", time_now.tm_mday)    # can also use time_now[2]

print("-------------------------------------------------------------")
start_time = time.time()
time.sleep(1)
end_time = time.time()

print("Start Time: {}".format(time.localtime(start_time)))
print("End Time: {}".format(time.localtime(end_time)))

# Timezones
print("The epoch on this system starts at " + time.strftime('%c', time.gmtime(0)))

print("The current timezone is {0} with an offset of {1}".format(time.tzname[0], time.timezone))

if time.daylight != 0:
    print("\tDaylight saving time is in effect for this location")
    print("\tThe DST timezone is " + time.tzname[1])

print("local time is " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
print("UTC time is " + time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))

# use datetime module
print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())
