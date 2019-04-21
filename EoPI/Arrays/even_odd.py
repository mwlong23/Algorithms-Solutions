# Uses Python 3
# By Mitch Long 04-21-2019
import copy

def even_odd(arr):
    if not arr:
        return 'Please Enter an Array'
    even_marker, odd_marker = 0, len(arr)-1
    while even_marker < odd_marker:

        if arr[even_marker] % 2 == 0:
            even_marker += 1
        if arr[odd_marker] % 2 == 1:
            odd_marker -= 1
        if arr[even_marker] % 2 != 0 and arr[odd_marker] % 2 != 1:
            arr[even_marker], arr[odd_marker] = arr[odd_marker], arr[even_marker]
            even_marker += 1
            odd_marker -= 1
    return arr


def even_odd_better(arr):
    even_marker, odd_marker = 0, len(arr)-1
    while even_marker < odd_marker:
        if arr[even_marker] % 2 == 0:
            even_marker += 1
        else:
            arr[even_marker], arr[odd_marker] = arr[odd_marker], arr[even_marker]
            odd_marker -= 1
    return arr

def main():
    arr = [2, 3, 6, 4, 5, 7, 11, 2, 6]
    test_case = copy.deepcopy(arr)
    test_case2 = copy.deepcopy(test_case)
    divided_arr = even_odd(test_case)
    print(divided_arr)
    print(even_odd_better(test_case2))


if __name__ == '__main__':
    main()
