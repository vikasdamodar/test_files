import pytz

t = "Thursday, June 6th 2019, 12:00:00 am"
old = pytz.timezone("Pacific Time")
new = pytz.timezone("US/Pacific")
my_timestamp_in_new_timezone = old.localize(t).astimezone(new)

# print(pytz.common_timezones)
import collections
import datetime as DT
import pytz

tzones = collections.defaultdict(set)
abbrevs = collections.defaultdict(set)

for name in pytz.all_timezones:
    tzone = pytz.timezone(name)
    for utcoffset, dstoffset, tzabbrev in getattr(
            tzone, '_transition_info', [[None, None, DT.datetime.now(tzone).tzname()]]):
        tzones[tzabbrev].add(name)
        abbrevs[name].add(tzabbrev)
print(tzones['EST'])
# print(abbrevs)

eastern = pytz.timezone('US/Eastern')
print(eastern.tzname(DT.datetime.now()))