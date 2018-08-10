## Given an array of numbers, returns length of the longest palindromic subsequence possible

def pal(list):
        T = [[1 for i in range(len(list))] for vals in range(len(list))]


        for i in range(1,len(list)):
                for j in range(len(list)-i):
                        ## print "Finding longest palindrome from position ",j,"to",j+i
                        if i == 1 and list[j] == list[j+i]:
                                T[j][j+i] = 2
                        else:
                                if list[j] == list[j+i]:
                                        T[j][j+i] = 2 + T[j+1][j+i-1]
                                else:
                                        T[j][j+i] = max(T[j+1][j+i],T[j][j+i-1])
                                
        return T[0][len(list)-1]




letters = ["a","g","b","d","b","a"]

print pal(letters)



