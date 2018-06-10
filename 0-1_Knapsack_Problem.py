## Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. 
## Items can only be used once (no-repetition)
import copy

wt = [1,3,4,5]
val = [1,4,5,7]
W = 7             ## Total capacity of knapsack

T = [[0 for wts in range(W+1)] for vals in range(len(val)+1)]
nums = [[ [] for wts in range(W+1)] for vals in range(len(val)+1)]


for i in range (len(wt)+1):
        for x in range(W+1):
            ## Base cases
            if i == 0 or x == 0:
                T[i][x] = 0
                
            ## Fill out table 
            elif (wt[i-1] <= x):
                ## When i = 0 val[i] references first item in list
                ## and when i=1 val[i] references second item in list
                ## thus "val[i-1]" necesary to get correct list item
                T[i][x] = max(val[i-1] + T[i-1][x-wt[i-1]], T[i-1][x])

                if (val[i-1] + T[i-1][x-wt[i-1]] > T[i-1][x]):
                        temp = copy.copy(nums[i-1][x-wt[i-1]])
                        temp.append(val[i-1])
                        nums[i][x]= temp
                else:
                        temp = copy.copy(nums[i-1][x])
                        nums[i][x] = temp
                        
                        
                
            else:
                T[i][x] = T[i-1][x]

                temp = copy.copy(nums[i-1][x])
                nums[i][x] = temp
                
print len(wt),"items \n", "with weights:", "\n", wt,"\n\n","and values:", "\n", val,"\n"
print "Knapsack capacity = ",W, "\n"

print "Maxiumum achievable value is", T[len(wt)][W]
print "Knapsack consists of items with values", nums[len(wt)][W]
    

