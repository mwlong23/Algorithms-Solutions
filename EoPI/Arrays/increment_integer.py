# Written in Python 3

# Prompt: write a function that takes an array of integers representing a digit,
# increments an arbitrary length integer by 1,
# Outputs: An array of the input plus one
# Input: [1,2,9]
# Output [1,3,0]


def plus_one(arr):
    arr[-1] +=1

    for i in reversed(range(1, len(arr))):
        if arr[i] != 10:
            break
        arr[i] = 0
        arr[i-1] += 1
    if arr[0] == 10:
        arr[0] = 0
        arr.insert(0, 1)
    print(arr)
    return arr



if __name__ == "__main__":

    added = plus_one([9,9,9,9,9])
    print(added)