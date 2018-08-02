## Coin Change Variation 2  - Limited Supply of Coins

## Given a total and coins of values specified, determine least number of coins necessary to make change
## Can only use each coin ONCE

import copy


def coin_change(coin,total):
        ## Initialize empty array to store coint count necessary to make change
        T = [[0 for x in range(total+1)] for y in range(len(coin))]
        ## To store coin denominations necessary to make change
        change = [[ [] for x in range(total+1)] for y in range(len(coin))]

        
        ## Build table from left to right
        for val in range(len(coin)):
                for subtotal in range(1,total+1):
                        print "current coin is",val, " with value of ", coin[val]
                        print "current subtotal",subtotal   
                    
                        ## If subtotal equals coin value exactly, can make change with single coin
                        if subtotal == coin[val]:
                                T[val][subtotal] = 1
                                ## Add coin denomination to change necessary
                                change[val][subtotal] = [coin[val]]
                  


                        ## If total is greater than coin value and you're able to make change with the leftover total amount after subtracting coin value..       
                        elif subtotal > coin[val] and T[val-1][subtotal-coin[val]] <> 0:
                                if T[val-1][subtotal] > 0 :
                                        ## Update coin count
                                        T[val][subtotal] = min(1+T[val-1][subtotal-coin[val]],T[val-1][subtotal])

                                        ## Update change necesasry
                                        if T[val][subtotal] == (1+T[val-1][subtotal-coin[val]]):
                                                temp = copy.copy(change[val-1][subtotal-coin[val]])
                                                temp.append(coin[val])
                                                change[val][subtotal] = temp
                                        else:
                                                change[val][subtotal] = change[val-1][subtotal]
                                else:
                                        T[val][subtotal] = 1+T[val-1][subtotal-coin[val]]

                                        ## Update change necessary
                                        temp = copy.copy(change[val-1][subtotal-coin[val]])
                                        temp.append(coin[val])
                                        change[val][subtotal] = temp

                        else:
                                ## Don't take current coin
                                T[val][subtotal] = T[val-1][subtotal]

                                ## update change necessary
                                change[val][subtotal] = change[val-1][subtotal]
                        print T
                      
                                
                

        return T[len(coin)-1][total], change[len(coin)-1][total]


coin_input = [1,5,10,20]
total_input = 16


answer = coin_change(coin_input,total_input)

print "Given unlimited coins with denominations ",coin_input
print "You can make change for",total_input
print "with a minimum of",answer[0], "coins"
print "Using coin denominations ",answer[1]

