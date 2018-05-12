## Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. 

wt = [1,3,4,5]
val  [1,4,5,7]
W = 7             ## Total capacity of knapsack

T = [0 for wts in wt][0 for j in range(0,W+1)]


for i in range (0,len(wt)+1):
		for x in range(0,W+1):
			## Base cases
			if i == 0:
				T[i][x] = 0
			if x == 0:
				T[i][x] = 0
			## Fill out table 
			elif (wt[i] <= x):
				T[i][x] = max(val[i] + T[i-1][x-wt[i]], T[i-1][x])
			else:
				T[i][x] = T[i-1][x]
	print T
return T[len(wt)][W]
	

