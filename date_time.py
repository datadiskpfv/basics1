import time

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
time.sleep(10)
end_time = time.time()

print("Start Time: {}".format(time.localtime(start_time)))
print("End Time: {}".format(time.localtime(end_time)))
