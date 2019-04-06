# Uses python3
def edit_distance(s, t):
    solution = edit_distance_helper(list(s), list(t))
    return solution


def edit_distance_helper(arr1,arr2):
    graph = [[0 for _ in range(len(arr1)+1)] for _ in range(len(arr2)+1)]

    # initialize graph
    for i in range(len(arr1)+1):
        graph[0][i] = i
    for j in range(len(arr2)+1):
        graph[j][0] = j
    # iterate over each row
    for j in range(1,len(arr2)+1):
        # Then Columns
        for i in range(1, len(arr1)+1):

            insert = graph[j][i-1] + 1
            delete = graph[j-1][i] + 1
            mismatch = graph[j-1][i-1] + 1
            match = graph[j-1][i-1]

            if arr1[i-1] == arr2[j-1]:
                graph[j][i] = min(match, delete, insert)
            else:
                graph[j][i] = min(mismatch, delete, insert)
    # print_2D(graph)
    return graph[len(arr2)][len(arr1)]

# Utility function to print 2D Lists
def print_2D(graph):
    print('[')
    for row in graph:
        print('  ' + str(row))


if __name__ == "__main__":
    print(edit_distance(input(), input()))







