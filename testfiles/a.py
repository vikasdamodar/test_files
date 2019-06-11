import random
from datetime import datetime

t = ["02/24/1946", "01/29/1946", "03/29/1945", "03/29/1949", "02/29/1946"]
timestamps = ['2011-06-2', '2011-08-05', '2011-02-04', '2010-1-14',
              '2010-12-13', '2010-1-12', '2010-2-11', '2010-2-07',
              '2010-12-02', '2011-11-30', '2010-11-26', '2010-11-23',
              '2010-11-22', '2010-11-16']

# l = sorted(t, key=lambda d: tuple(map(datetime, d.split('/'))))


def get_earliest(kwargs):
    earliest_date = min(list(datetime.strptime(i, "%Y-%m-%d") for i in kwargs)).date()
    return str(earliest_date)


# k = get_earliest("02/24/1946", "01/29/1946", "03/29/1945", "03/28/1945")
m = get_earliest(timestamps)
print(m)

# import os.path,subprocess
# from subprocess import STDOUT,PIPE
#
# java_class, ext = os.path.splitext('a.java')
# cmd = ['java', java_class]
# proc = subprocess.Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
# print(proc.__dict__)
# stdout, stderr = proc.communicate()
# k = 29411.899999999998
# k = (k*100)/100
# l = (k*15)/100
# k -= l
# print(k)


def get_e(*kwargs):
    n = [list(map(int, i.split("/"))) for i in kwargs]
    sorted_list = sorted(n, key=lambda x: (x[2], x[0], x[1]))
    print("/".join(map(str,sorted_list[0])))


get_e("02/24/1946", "01/29/1946", "03/29/1945")


from collections import Counter

f = Counter(["aaa", "bbb", "ccc", "aaa"])
print(f)
print(["ww", "dd","ww"].count("ww"))
print(set([1, 1, 2, 2, 3, 2]))


def compact(kwargs):
    h = [i for i in kwargs if kwargs.__next__()!=i]
    print(h)

compact(n**2 for n in [1, 2, 2])