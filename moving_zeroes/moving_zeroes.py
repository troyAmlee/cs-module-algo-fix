'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    count = 0
    for j,i in enumerate(arr):
        while((arr[j] == 0) and j+1 != len(arr)):
            count += 1
            j+=1
        if(j != len(arr)):
            temp = arr[j]
            arr[j] = arr[j-count]
            arr[j-count] = temp
            count = 0
        if(i != 0):
            pass

                


    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")