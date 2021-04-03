# Uses python3
import sys

def optimal_weight(W, w):
    """Problem IntroductionYou are given a set of bars of gold and your goal is 
    to take as much gold as possible intoyour bag. There is just one copy of 
    each bar and for each bar you can either take it or not (hence you cannot take
    a fraction of a bar).
    Given 𝑛 gold bars, find the maximum weight of gold that fits into a bag of 
    capacity 𝑊.
    
    Input Format
    The first line of the input contains the capacity 𝑊 of a knapsack and the 
    number 𝑛 of bars of gold. The next line contains 𝑛 integers 𝑤0, 𝑤1, ... , 𝑤𝑛−1 
    defining the weights of the bars of gold.
    
    Constraints
    1 ≤ 𝑊 ≤ 10^4
    1 ≤ 𝑛 ≤ 300
    0 ≤ 𝑤0, ... , 𝑤𝑛−1 ≤ 10^5
    
    Output Format
    Output the maximum weight of gold that fits into a knapsack of capacity 𝑊"""

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

    # return max weight when capcity is W and all items considered
    return T[-1][-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
