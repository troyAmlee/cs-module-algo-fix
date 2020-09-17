'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, c = None):
    # [2 raised to (n-1) - 1] (N+R-1)!/((R-1)!*(N)!)

    #[4], [1 + 1 + 1 + 1], [1 + 2 + 1], [2 + 2], [2 + 1 + 1], [1 + 1 + 2], [1 + 3], [3 + 1]

    if(n < 0):
        return 0
    
    elif(n == 0):
        return 1

    elif c and c[n] > 0:
        return c[n]
    else:
        if not c:
            c = {i: 0 for i in range(n+1)}
        c[n] = eating_cookies(n - 1, c) + eating_cookies(n - 2, c) + eating_cookies(n - 3, c)
    return c[n]
    
    
        

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 7

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
