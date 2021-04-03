# Uses python3
import sys
import itertools

def partition3(A):
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0

def knapsack_0_1(w, W):
    # import pandas as pd

    # initialise table
    # BASE CASES: when n = 0 --> no items to take --> 0 for all w
    # when w = 0 --> cannot take any items --> 0 for all n

    T = [[0 for j in range(W + 1)] for n in range(len(w) + 1)]

    # fix the item(s) considered and iterate through each weight to populate table
    for n in range(1, len(w) + 1):
        for j in range(1, W + 1):
            # table has a null item but the input array does not include this
            # need to shift the index by one
            w_n = w[n-1]

            # check effect of taking the item on capacity
            if T[n-1][max(0, j - w_n)] + w_n > j:
                # cannot take item as it will exceed capacity
                T[n][j] = T[n-1][j]

            elif T[n-1][max(0, j - w_n)] + w_n == j:
                # taking the item maximises capacity
                T[n][j] = j
            else:
                # max of 3 possibilities: 
                T[n][j] = max(T[n-1][max(0, j - w_n)] + w_n, T[n-1][j], T[n][j-1])

    # to print table nicely
    # df = pd.DataFrame(T, index=[0] + (w))
    # print(df)

    # return max weight when capcity is W and all items considered
    return T

def backtrace(T, w, W):
    i = len(w) 
    j = W 
    items = []
    while i > 0 and j > 0:

        w_i = w[i-1]
        
        # 2 possibilities -> item was taken or not
        if T[i][j] == T[i-1][j]:
            # item was not taken
            i -= 1
            
        else:
  
            j = max(0, j-w_i)
            items.append(w_i)
            i -= 1
            
            
   
    return items

def partition3_dp(A):
    
    # don't even try if sum of all elements is not divisible by 3
    if sum(A) % 3 != 0 or len(A) < 3:
        return 0

    target_sum = sum(A) // 3
    
    # imagine problem of maximising weight (target value) of a knapsack given items of 
    # various weights (values of souvenirs)
    # if knapsack cannot be filled to its capacity -> there does not exist a subset of A
    # that adds to target sum

    T1 = knapsack_0_1(A, target_sum)

    if T1[-1][-1] != target_sum:
        return 0
    else:
        # print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in T1]))
        # backtrace table to find which souvenirs were selected 
        # remove them from the list and repeat knapsack with the filtered list
        items = backtrace(T1, A, target_sum) # implement backtrace function
        for item in items:
            A.remove(item) # remove selected souvenirs
        T2 = knapsack_0_1(A, target_sum)

        if T2[-1][-1] != target_sum:
            return 0

        else:
            
            # Repeat one more time
            items = backtrace(T2, A, target_sum)  # implement backtrace function
            for item in items:
                A.remove(item) # remove selected souvenirs

            if sum(A) != target_sum:
                return 0

            # else 3 distinct subsets were found to add up to the target sum!
            return 1

            
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3_dp(A))

