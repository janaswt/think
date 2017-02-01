def seq_3_np1(n):
    """Print 3n+1 sequence from n, terminating when it reaches 1"""
    while n !=1:
        print(n)
        if n % 2 ==0:
            n = n // 2
        else:
            n = n*3 +1
    print(n)
seq_3_np1(9)