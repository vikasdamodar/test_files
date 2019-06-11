from timeit import default_timer
import sys


def timing(method):
    def time_calc(*args, **kwargs):
        st = default_timer()
        result = method(*args, **kwargs)
        et = default_timer()
        print("elapsed time : ", (et-st)*1000)
        return result
    return time_calc


@timing
def func_ls(ls):
    print(ls[59], sys.getsizeof(ls))


@timing
def func_ls2(ls):
    for i in ls:
        if 59 == i:
            print(i, sys.getsizeof(ls))


@timing
def func_dict(dt):
    try:
        print(dt[19], sys.getsizeof(dt))
    except Exception:
        pass


@timing
def func_dict2(dt):
    for i, j in dt.items():
        if j == 20:
            print(i, sys.getsizeof(dt))


@timing
def func_set(st):
    print(5 in st, sys.getsizeof(st))


@timing
def func_set2(st):
    for i in st:
        if 59 == i:
            print(i, sys.getsizeof(st))


ls_var = list(range(1000000))
ls_var2 = list(range(100))
dt_var = {i: i+1 for i in range(1000000)}
dt_var2 = {i: i+1 for i in range(100)}
st_var = set(range(1000000))
st_var2 = set(range(100))

# func_ls(ls_var)
# func_ls2(ls_var)
# func_ls2(ls_var2)
# func_ls2(list(range(1000)))
# func_ls2(list(range(10000)))
# func_ls2(list(range(100000)))
# func_ls2(list(range(200000)))
print("Time Complexity for list :")
print("\tBest case search element: O(1)")
print("\tWorst case finding the element: O(n)")
# func_dict(dt_var)
# func_dict2(dt_var)
# func_dict2(dt_var2)
# func_dict2({i: i+1 for i in range(1000)})
# func_dict2({i: i+1 for i in range(10000)})
# func_dict2({i: i+1 for i in range(100000)})
print("Time Complexity for dict: ")
print("\tBest case for access value: O(1)")
print("\tWorst case access value: O(n)")
# func_set(st_var)
# func_set2(st_var)
# func_set2(st_var2)
# func_set2(set(range(1000)))
# func_set2(set(range(10000)))
# func_set2(set(range(100000)))
# func_set2(set(range(200000)))
print("Complexity for sets: ")
print("\tBest case search elements: O(1)")
print("\tWorst case search elements: O(n)")
