## Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. 
## Items can only be used once (no-repetition)

wt = [1,3,4,5]
val = [1,4,5,7]
W = 7             ## Total capacity of knapsack

T = [[0 for wts in range(W+1)] for vals in range(len(val)+1)]
print T

for i in range (len(wt)+1):
        for x in range(W+1):
            ## Base cases
            if i == 0 or x == 0:
                T[i][x] = 0
                
            ## Fill out table 
            elif (wt[i-1] <= x):
                T[i][x] = max(val[i-1] + T[i-1][x-wt[i-1]], T[i-1][x])
            else:
                T[i][x] = T[i-1][x]
print(T)                
print T[len(wt)][W]
    

