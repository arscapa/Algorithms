## Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. 

wt = [1,3,4,5]
val = [1,5,5,7]
W = 7             ## Total capacity of knapsack

T = [0 for x in range(W+1)]


T[0] = 0

for w in range(1,W+1):
    for i in range(len(val)):
        if wt[i] <= w and T[w] < val[i] + T[w-wt[i]]:
            T[w] = val[i] + T[w-wt[i]]
   #print ("At weight capacity of "+str(w)+" max attainable value = "+str(T[w]))
print(T)
print("\n Maximum value attainable with weight capacity of " + str(W) + " is value " + str(T[w]))
    


	
    

