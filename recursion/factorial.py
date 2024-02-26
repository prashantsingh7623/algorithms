# using recursion
def factorial_using_recur(n: int) -> int:
    if n < 1:
        return 1;
    return n * factorial_using_recur(n-1)

# using for loop
def factorial_using_for_loop(n: int) -> int:
    for i in range(n-1,1,-1):
        n = n * i
    return n

if __name__ == '__main__':
    fact_using_recur = factorial_using_recur(5)
    fact_using_for_loop = factorial_using_for_loop(6)
    print('factrial of {} is {}'.format(5,fact_using_recur))
    print('factrial of {} is {}'.format(6,fact_using_for_loop))