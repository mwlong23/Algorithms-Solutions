# Python 3
# Interview Practice: delete dups from an array
# I: [2,3,5,5,7,11,11,11,13]
# O: [2,3,5,7,11,13]


def delete_dups(arr):

    if not arr:
        return 0

    write_index = 1
    for i in range(1,len(arr)):
        if arr[write_index-1] == arr[i]:
            arr[write_index] = arr[i]
            write_index += 1
    return write_index

if __name__ == '__main__':
    arr = [2, 3, 5, 5, 7, 11, 11, 11, 13]
    print(delete_dups(arr))

