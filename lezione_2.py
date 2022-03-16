my_list = [2, 4, 4]

def sum_list(my_list):
    return sum(my_list)

def raw_sum_list(my_list):
    tot = 0
    for item in my_list:
        tot += item
    return tot

print("SUM Built-in Function Result: {}".format(sum_list(my_list)))
print("RawSum User Function Result: {}".format(raw_sum_list(my_list)))