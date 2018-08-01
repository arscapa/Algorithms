## Given a total and coins of values specified, determine least number of coins necessary to make change
## Assume an unlimited supply of coins of each denomination
import copy


def coin_change(coin,total):
        ## Initialize empty array to store values
        T = [[0 for x in range(total+1)] for y in range(len(coin))]
        print T
        ## Build table from left to right, top down
        for val in range(len(coin)):
                for subtotal in range(1,total+1):
                        print "current coin is",val, " with value of ", coin[val]
                        print "current subtotal",subtotal   
                    
                        ## If subtotal equals coin value exactly, can make change with single coin
                        if subtotal == coin[val]:
                                print "Setting current subtotal for coin = 1"
                                T[val][subtotal] = 1


                        ## If total is greater than coin value and you're able to make change with the leftover total amount after subtracting coin value..       
                        ## 1st And condition necessary --> if you take coin and solution to smaller subtotal is 0 then you can't make exact change
                        ## 2nd And condition necessary --> don't want to take min if answer to subtotal at previous value was 0 
                        elif subtotal > coin[val] and T[val][subtotal-coin[val]] <> 0:
                                ## Compare prior solution only if was able to make change 
                                if T[val-1][subtotal] > 0 :
                                        print "Compare prior solution and take min "
                                        T[val][subtotal] = min(1+T[val][subtotal-coin[val]],T[val-1][subtotal])
                                else:
                                        ## Was unable to make change with previous coins only, take only possible solution
                                        T[val][subtotal] = 1+T[val][subtotal-coin[val]]

                        else:
                                print "else condition"
                                T[val][subtotal] = T[val-1][subtotal]
                        print T
                        
        return T


coin_input = [2,5,10]
total_input = 9


print coin_change(coin_input,total_input)
    

