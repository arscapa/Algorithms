## Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. 
## Items can only be used once (no-repetition)
import copy

def knapsack(wt,val,W):
        T = [[0 for wts in range(W+1)] for vals in range(len(val)+1)]
        nums = [[ [] for wts in range(W+1)] for vals in range(len(val)+1)]


        for i in range (len(wt)+1):
                for x in range(W+1):
                    ## Base cases
                    if i == 0 or x == 0:
                        T[i][x] = 0
                
                    ## Fill out table 
                    elif (wt[i-1] <= x) and (val[i-1] + T[i-1][x-wt[i-1]] > T[i-1][x]):
                        T[i][x] = val[i-1] + T[i-1][x-wt[i-1]] ## update max value

                        temp = copy.copy(nums[i-1][x-wt[i-1]])
                        temp.append(val[i-1])
                        nums[i][x]= temp                      ## update knapsack contents                                                
                
                    else:
                        T[i][x] = T[i-1][x]

                        temp = copy.copy(nums[i-1][x])
                        nums[i][x] = temp
                
        print len(wt),"items \n", "with weights:", "\n", wt,"\n\n","and values:", "\n", val,"\n"
        print "Knapsack capacity = ",W, "\n"

        print "Maxiumum achievable value is", T[len(wt)][W]
        print "Knapsack consists of items with values", nums[len(wt)][W]
        return T[len(wt)][W]




weights = [2,3,4,6]
values = [9,14,16,30]
maxW = 10             ## Total capacity of knapsack

knapsack(weights,values,maxW)
    

