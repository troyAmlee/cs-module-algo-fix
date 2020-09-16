'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    count = 0
    output = []
    for i in range(len(nums)):
        if(len(nums[count:k+i]) == k):
            print(nums[count:k+i])
            for j in range(len(nums[count:k+i])):
                if(j == 0):
                    maximum = nums[count:k+i][j]
                else:
                    if(maximum <= nums[count:k+i][j]):
                        maximum = nums[count:k+i][j]
            output.append(maximum)
        count+=1
    print(output)
    return output
    


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")


            #         if(j != 0):
            #         sum = sum*nums[count:k+i][j]
            # output.append(sum)
            # sum = 1
