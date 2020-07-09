def maxProfit(prices):
    maxprofit = 0

    for index in range(1, len(prices)):
        if prices[index] > prices[index-1]:
            maxprofit += prices[index] - prices[index-1]

    return maxprofit


# def rotateArray(num, k):
#     # must copy the data to another memory space, otherwise they both share the data in the same memory sapce
#     new_num = num[:]

#     for i in range(0,len(num)):
#         new_num[(i+k)%len(num)] = num[i]
    
#     for i in range(len(num)):
#         num[i] = new_num[i]

