import pytz
import datetime

country = 'Europe/Moscow'

tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)
print("The time in {} is {}".format(country, local_time))
print("UTC is {}".format(datetime.datetime.utcnow()))

# for tz in pytz.all_timezones:
#     print(tz)
#
# for tz in sorted(pytz.country_names):
#     print(tz + ": " + pytz.country_names[tz])

# for tz in sorted(pytz.country_names):
#     print("{}: {}: {}".format(tz, pytz.country_names[tz], pytz.country_timezones.get(tz)))

for country in sorted(pytz.all_timezones):
    tz_to_display = pytz.timezone(country)
    local_time = datetime.datetime.now(tz=tz_to_display)
    print("The time in {} is {}".format(country, local_time))

