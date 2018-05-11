## This solution provides the longest length achievable as well as subsequence itself


## Example--- list = [5,7,4,-3,9,1,10,4,5,8,9,3]
## LIS is -3,1,4,5,8,9
## maximum LIS length is 6


list = [5,7,4,-3,9,1,10,4,5,8,9,3]
length = []
nums = []

def LIS(list):
    for i in range (0,len(list)):
        ## Length of one item is one
        length.append(1)
        nums.append([list[i]])
        for x in range (0,i):
         ## If list item that comes before item list[i] is less than list[i], than you know you can append list[i] to end (if length would be longer than current LIS for item i)
              if list[x] < list[i] and length[i] < 1 + length[x]:
                  length.pop(i)
                  length.append(1 + length[x])
                  nums.pop(i)
                  nums.append(nums[x] + [list[i]])

                  
    maxVal = 1
    maxIndex = 0
    for i in range(0,len(length)):
        if length[i] > maxVal:
            maxVal = length[i]
            maxIndex = i
    
    
    print 'Length of the Longest Increasing Subsequence is ',maxVal
    print 'LIS is ',nums[maxIndex]
    return maxVal
              
      
LIS(list)


