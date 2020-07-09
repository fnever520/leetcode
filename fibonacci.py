def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

def fib_dp(n):
    if n <= 2:
        return 1
    
    bot = [None for i in range(n+2)]
    bot[1] = 1
    bot[2] = 1

    for i in range(3, n+1):
        bot[i] = bot[i-1] + bot[i-2]

    return bot[n]