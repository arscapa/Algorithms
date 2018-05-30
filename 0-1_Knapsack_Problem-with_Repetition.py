## Knapsack 0-1 Problem w/t Repetition

## Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. 
## Items can be used multiple times 
import copy

wt = [1,3,4,5]
val = [1,5,5,7]
W = 7             ## Total capacity of knapsack

T = [0 for x in range(W+1)]
items = [[] for x in range(W+1)]

for w in range(1,W+1):
    for i in range(len(val)):
        if wt[i] <= w and T[w] < val[i] + T[w-wt[i]]:
            T[w] = val[i] + T[w-wt[i]]
            temp = copy.copy(items[w-wt[i]])
            temp.append(val[i])
            items[w] = temp
   
print(T)
print(items)
print("\n Maximum value attainable with weight capacity of " + str(W) + " is value " + str(T[W]))
print("\n ...attained using items with values " + str(items[W]))    


	
    

