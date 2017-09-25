"""
Given an integer, find the next largest integer using ONLY the digits from the given integer.
Input Description

An integer, one per line.
Output Description

The next largest integer possible using the digits available.
Example

Given 292761 the next largest integer would be 296127.
Challenge Input

1234
1243
234765
19000
Challenge Output

1243
1324
235467
90001
"""
"""
Methodology:
Start from the rightmost digit
Insert that digit on the left of the first digit that it's greater than. This ensures a greater number.
Then the digits to the right of it must be in the smallest order. From your pool of numbers right of the current digit,
pick the smallest one, then recursively choose on the remaining pool of numbers.

Data Structure:
easiest way would be to just stored the number into an array
"""

#given a int,
def num_input(num):
    num_list = list(int(i) for i in str(num))
    res_tup = r_digit_left_check(num_list)
    num_list = rest_shuffle(res_tup[0], res_tup[1])
    res_string = ""
    for i in num_list:
        res_string += str(i)
    print(res_string)


def r_digit_left_check(num_list):
    """
    takes the right most digit and inserts it self immediate left of the first smallest digit it finds
    :param num_list: 
    :return: a num array with right most digit inserted, and index right of newly inserted postion
    """
    r_digit = num_list[-1]
    dig = 2
    while r_digit == 0:
        r_digit = num_list[-dig]
        dig +=1
    rev_num_list = list(reversed(num_list))
    index_small = None
    for i in rev_num_list:
        if i < r_digit and i!= 0:
            index_small = rev_num_list.index(i)
            break
    # found the index of the 1st smallest digit in the reversed list; now subtract len of array by index to get
    # position in the original array
    try:
        index_small = len(rev_num_list) - 1 - index_small
        num_list.insert(index_small, r_digit)
        num_list = num_list[0:-1]
    except TypeError:
        print("No index found")
        return num_list, i+1

    return num_list, index_small+1


def rest_shuffle(num_array, index):
    """
    :param num_array: 
    :param index: 
    :return: a final array with the rest of the array arranged to lowest number
    """
    # base case
    if len(num_array) == 0:
        return []
    if len(num_array) == index - 1:
        return num_array
    i = sorted(num_array[index:])[0]
    retrieved_num = num_array[index:].pop(num_array[index:].index(i))
    return num_array[0:index] + [retrieved_num] + rest_shuffle(num_array[index+1:], index)


num_input(235467)
